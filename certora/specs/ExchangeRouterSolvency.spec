// The goal of this spec is to mechanize the properties requested by GMX
// which are quoted here:
//=============================================================================
// GMX Request
//=============================================================================
// 1. if the price value is the same, no sequence of actions should result in a net profit, or another way to phrase it would be that markets should always be solvent if price does not change

// e.g. if the price of a token remains at $5000, then a user could increase position / swap / deposit / decrease position / withdraw / collect funding fees / collect borrowing fees, but the total input into the market should not exceed the total output


// 2. if the market has a long token that is the same as the index token and the reserveFactor is less than 1, then the market should always be solvent regardless of the price of the index token


// 3. if the market has a long token that is not the same as the index token and the max pnl factor for traders is less than 1, then the market should always be solvent regardless of the price of the index token

// solvent meaning the market can be fully closed, all positions can be closed and all users can redeem market tokens, and there is no bank run scenario, where the first to withdraw gets a higher value per market token than the last to withdrawn


// 4. if price does not change no sequence of actions should lead to a decrease in the market pool value, all funding fees  and protocol fees can be claimed and all market tokens can be redeemed

//=============================================================================
// Strategy
//=============================================================================
// Property 1 asks to ensure that no sequence of user actions can violate 
// solvency, and GMX also clarifies the meaning of solvency.
// Solvency:
// * The market can be fully closed
// * All positions can be closed
// * All users can redeem market tokens
// * There is no bank run scenario
//         meaning the first to withdraw gets a higher value per market token
//         than last to withdraw
//
// Properties 2 and 3 seem to be special cases of ensuring solvency holds.
// So we we may be able to prove a general property about solvency holding,
// and then show 2 and 3 as specific instances of the general property.
//
// Propery 4 is about ensuring fees can be collected. Since this is similarly
// a liveness condition, we can potentially fold fee collection into the def
// of solvency.

// Solvency appears to be a collection of liveness properties. We can define
// it by showing that the implied functions can be executed (i.e. with the right
// parameters and without reverting).

// We want to show that "Solvency" holds despite arbitrary (potentially 
// adversarial) user interactions. Users can interact with the system by
// making external calls. So we can specify Solvency is maintained despite
// arbitrary sequences of user calls as a proof by induction over an arbitrary 
// sequence. This should be possible so long as we prove an invariant over
// each of the individual public calls stating that: assuming "solvency"
// held before the call, it should still hold after the call.

// In this spec, "Solvency" is really broken into 4 invariants:
// - positions_can_be_closed_...
// - market_can_be_closed_...
// - users_can_redeem_market_tokens_...
// - no_bank_run_scenario_...

// The idea is we should write a rule that shows these invariants hold
// for all of the calls (and in principle we could use a parametric rule)
// but for now this is just done for cancelWithdrawal. (And probably
// the highest priority calls are really createOrder/executeOrder,
// since these include the user behaviors the client referenced explicitly)


using ExchangeRouter as exchangeRouter;
using DataStore as dataStore;
using KeysHarness as keys;
using PositionUtils as positionUtils;
using PositionStoreUtils as positionStoreUtils;
using GetPositionKeyHarness as positionKeyHarness;

methods {
    // ExchangeRouter

    function ExchangeRouter.simulateExecuteOrder(bytes32, OracleUtils.SimulatePricesParams) external => CONSTANT;

    function ExchangeRouter.createOrder(BaseOrderUtils.CreateOrderParams) external returns (bytes32) => CONSTANT;

    // PositionStoreUtils
    // function PositionStoreUtils.get(address, bytes32) external returns (Position.Props) => CONSTANT;

    // DataStore
    function _.containsBytes32(bytes32, bytes32) external => DISPATCHER;
    function _.getAddress(bytes32) external => DISPATCHER;
    function _.getUint(bytes32) external => DISPATCHER;
    function _.getBool(bytes32) external => DISPATCHER;

     
}

function closing_create_order_params_from_position(Position.Props position) returns BaseOrderUtils.CreateOrderParams {
    BaseOrderUtils.CreateOrderParams close_order_params;

    require close_order_params.orderType == Order.OrderType.MarketDecrease;

    // addresses
    require close_order_params.addresses.receiver == position.addresses.account;
    require close_order_params.addresses.market == position.addresses.market;
    require close_order_params.addresses.initialCollateralToken == position.addresses.collateralToken;

    // numbers
    // NOTE: price is underspecified here. This is currently
    // just used to show that it is possible to issue a close order.
    require close_order_params.numbers.sizeDeltaUsd == position.numbers.sizeInUsd;

    require close_order_params.isLong == position.flags.isLong;

    return close_order_params;
}

// this mirrors PositionUtils.validateNonEmptyPosition, but returns
// a bool rather than reverting if the position is empty
function isPositionEmpty(Position.Props position) returns bool {
    return position.numbers.sizeInUsd == 0 && position.numbers.sizeInTokens == 0 && position.numbers.collateralAmount == 0;
}

function positions_closable(env e, OracleUtils.SimulatePricesParams oracle_price_params) returns bool {
    address some_account;
    address some_market;
    address some_collateral_token;
    bool some_is_long;
    bytes32 some_position_key = positionKeyHarness.getPositionKey(e, some_account, some_market, some_collateral_token, some_is_long);
    Position.Props position = positionStoreUtils.get(e, dataStore, some_position_key);
    bool non_empty_position = !isPositionEmpty(position);
    closing_create_order_params_from_position(position);
    BaseOrderUtils.CreateOrderParams closing_order_params = closing_create_order_params_from_position(position);

    bytes32 closing_order_key = exchangeRouter.createOrder@withrevert(e, closing_order_params); 
    bool createOrderReverted = lastReverted;
    exchangeRouter.simulateExecuteOrder@withrevert(e, closing_order_key, oracle_price_params);
    bool executeOrderReverted = lastReverted;

    return non_empty_position => !createOrderReverted && !executeOrderReverted;
}

rule positions_can_be_closed(method f) {
    // A liveness property that all open positions can be closed, even
    // after arbitrary (potentially adversarial) user actions. More precisely,
    // for any public/external call, we prove an invariant that assuming
    // it was possible to close all open positions before the call, it is still
    // possible to close all open positions after the call.

    // A position is closed by issuing a decrease order (so that it is 
    // decreased to zero).

    env e;
    calldataarg args;

    // Used for both precond and postcond since we assume the
    // prices do not change
    OracleUtils.SimulatePricesParams oracle_price_params;

    // We need to save the state before positions_closable because
    // simulateExecuteOrder in positions_closable is state-changing.
    storage stateBeforePrecond = lastStorage;

    //========================================================================
    // Require: positions can be closed before executing the call
    //========================================================================
    require positions_closable(e, oracle_price_params);

    //========================================================================
    // Execute the call
    //========================================================================
    f(e, args) at stateBeforePrecond;

    //========================================================================
    // Assert: positions can be closed after executing the call
    //========================================================================
    assert positions_closable(e, oracle_price_params);
}

rule market_can_be_closed {
    // TODO: need real definition of "markets can be closed"
    // For now I think this could mean:
    // * for all existing deposits: a withdrawal can be created
    // for the total amount to the right account.
    // * all the created withdrawals can be executed (by a keeper
    // with the right permissions)

    // Rule structure:
    // Require: market can be closed before executing the call
    // Execute the call
    // Assert: market can be closed after executing the call

    // TODO WIP
    assert true;
}


rule users_can_redeem_market_tokens {
    // TODO need real definition of "users can redeem market tokens"
    // Perhaps this is about the ability to claim all the various fees
    // and rewards.
    // Slightly more concretely "users can redeem market tokens"
    // could mean, each of the following calls can be succesfully made
    // with the total amounts and towards the appropriate accounts based
    // on the state of the system:
    // * claimFundingFeeds
    // * claimCollateral
    // * claimAffiliateRewards
    // * claimUiFees

    // Rule Structure: 
    // Require: users can redeem market tokens before the call
    // Execute the call
    // Assert: market can be closed after the call
    assert true;
}

rule no_bank_run_scenario {
    // "there is no bank run scenario, where the first to withdraw gets a 
    // higher value per market token than the last to withdraw."

    // This may be the first one that we really need to specify as hypersafety
    // https://www.cs.cornell.edu/fbs/publications/HyperpropertiesCSFW.pdf
    // meaning that we need two executions to model the two different orderings
    // of withdrawal

    // First we need to define "Bank Run Freedom":
    // * To do so we create two systems (instances of ExchangeRouter)
    // with two different dataStores and all the other data structures
    // * Then, we want to model two different orderings of withdrawals:
    // - We instantiate two addresses.
    // - On instance 1 we call withdraw(address1); withdraw(address2).
    // - On instance 2 we call withdraw(address2); withdraw(address1).
    // - We assert that afterwards the value per market token for both
    // instances is the same
    // Ideally, we define "Bank Run Freedom" as a function that
    // takes 2 instances of ExchangeRouter and returns a bool

    // We then follow the same invariant pattern as with all the
    // other parts of the Solvency definition. However, now
    // we need to do this for two instances of the system

    // Rule Structure:
    // Make 2 instances of ExchangeRouter
    // Require BankRunFreedom(ER1, ER2)
    // Call the method under proof on each of ER1, ER2 
        // (e.g. call ER1.cancelWithdrawal(...), ER2.cancelWithdrawal(...)) 
    // Assert BankRunFreedom(ER1, ER2) on the post-states after executing
    // in each system

    assert true;
}