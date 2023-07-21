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
// - closing_create_order_params_from_order
// - market_can_be_closed_cancelWithdrawal
// - users_can_redeem_market_tokens_cancelWithdrawal
// - no_bank_run_scenario_cancelWithdrawal

// The idea is we should write a rule that shows these invariants hold
// for all of the calls (and in principle we could use a parametric rule)
// but for now this is just done for cancelWithdrawal. (And probably
// the highest priority calls are really createOrder/executeOrder,
// since these include the user behaviors the client referenced explicitly)


using ExchangeRouter as exchangeRouter;
using DataStore as dataStore;
using KeysHarness as keys;
using OrderStoreUtils as orderStoreUtils;

methods {
    // ExchangeRouter
    // function ExchangeRouter.cancelWithdrawal(/*key*/ bytes32) external => CONSTANT;
    // WithdrawalHandler
    // function _.createWithdrawal(address, WithdrawalUtils.CreateWithdrawalParams)  external => NONDET;
    function WithdrawalHandler.cancelWithdrawal(/*key*/ bytes32) external => CONSTANT;
    // function _.executeWithdrawal(bytes32, OracleUtils.SetPricesParams) external => NONDET;
    // function _.simulateExecuteWithdrawal(bytes32, OracleUtils.SimulatePricesParams) external => NONDET;
    // function _._executeWithdrawal(bytes32, OracleUtils.SetPricesParams) external => NONDET;
    // function _._handleWithdrawalError(bytes32, uint256, bytes memory) internal => NONDET;

    // // WithdrawalStoreUtils
    // // TODO clearly not right
    // function WithdrawalStoreUtils.get(DataStore, /*key*/ bytes32) external => CONSTANT;

    // // cancelWithdrawal's modifier functions from RoleStore. todo clearly not right.
    function _.hasRole(address, bytes32) internal => ALWAYS(true);
    function _._nonReentrantBefore() internal => CONSTANT;
    function _._nonReentrantAfter() internal => CONSTANT;

}

function closing_create_order_params_from_order(Order.Props props) returns BaseOrderUtils.CreateOrderParams {
    BaseOrderUtils.CreateOrderParams close_order_params;

    // addresses
    require close_order_params.addresses.receiver == props.addresses.receiver;
    require close_order_params.addresses.callbackContract == props.addresses.callbackContract;
    require close_order_params.addresses.uiFeeReceiver == props.addresses.uiFeeReceiver;
    require close_order_params.addresses.market == props.addresses.market;
    require close_order_params.addresses.initialCollateralToken == props.addresses.initialCollateralToken;
    // ERROR: could not type expression "close_order_params.addresses.swapPath == props.addresses.swapPath", message: type address[] is not comparable
    // require close_order_params.addresses.swapPath == props.addresses.swapPath;

    // numbers
    require close_order_params.numbers.sizeDeltaUsd == props.numbers.sizeDeltaUsd;
    require close_order_params.numbers.initialCollateralDeltaAmount == props.numbers.initialCollateralDeltaAmount;
    require close_order_params.numbers.triggerPrice == props.numbers.triggerPrice;
    require close_order_params.numbers.acceptablePrice == props.numbers.acceptablePrice;
    require close_order_params.numbers.executionFee == props.numbers.executionFee;
    require close_order_params.numbers.callbackGasLimit == props.numbers.callbackGasLimit;
    require close_order_params.numbers.minOutputAmount == props.numbers.minOutputAmount;

    require close_order_params.orderType == props.numbers.orderType;
    require close_order_params.decreasePositionSwapType == props.numbers.decreasePositionSwapType;

    // Note: a close order should be in the opposite direction
    require close_order_params.isLong == !props.flags.isLong;
    require close_order_params.shouldUnwrapNativeToken == props.flags.shouldUnwrapNativeToken;

    return close_order_params;
}

rule positions_can_be_closed_cancelWithdrawal {
    // A position is closed when an order of the opposite direction
    // of the position but with an equal amount is created.
    // So for a long order, this entails selling the security,
    // and for a short order this entails buying the security back.
    // Technically liquidation is the same thing, but in practice
    // these are done in different situations: closing is done
    // by the user to realize a gain/loss, whereas liquidation
    // is done by the protocol when limits are reached.

    // Using the opposite order way of specifying is likely
    // preferable because this
    // is the normal way a user will interact with the system.

    // Slightly closer to how this is mechanized: 
    // "For any position that is open, it is possible to create a new
    // order in the opposite direction and same amount, and excute
    // this order."

    env e;
    bytes32 withdrawalCancelKey;

    // Used for both precond and postcond since we assume the
    // prices do not change
    OracleUtils.SimulatePricesParams oracle_price_params;

    //========================================================================
    // Require: positions can be closed before executing the call
    //========================================================================
    bytes32 some_order_key; 
    // this key is in the list of orders
    bool precond_contains_key = dataStore.containsBytes32(e, keys.orderList(e), some_order_key);
    Order.Props precond_props = orderStoreUtils.get(e, dataStore, some_order_key);
    BaseOrderUtils.CreateOrderParams precond_closing_order_params = closing_create_order_params_from_order(precond_props);

    // Require: for any key in the list of order keys, it is possible
    // to create an order, and then also execute it.
    exchangeRouter.createOrder@withrevert(e, precond_closing_order_params);
    bool createOrderRevertedPre = lastReverted;
    // Ideally, I would like to really call OrderHandler.executeOrder
    // with a caller that has keeper permissions, but I am not
    // exactly sure how to do this without overspecifying yet... will
    // pivot back
    exchangeRouter.simulateExecuteOrder@withrevert(e, some_order_key, oracle_price_params);
    bool executeOrderRevertedPre = lastReverted;

    require (precond_contains_key /* todo add conjunct specifying other reasonable conditions that prevent a revert */ => !createOrderRevertedPre && !executeOrderRevertedPre);
    
    //========================================================================
    // Execute the call: cancelWithdrawal
    //========================================================================
    exchangeRouter.cancelWithdrawal(e, withdrawalCancelKey);

    //========================================================================
    // Assert: positions can be closed after executing the call
    //========================================================================
    bool postcond_contains_key = dataStore.containsBytes32(e, keys.orderList(e), some_order_key);
    Order.Props postcond_props = orderStoreUtils.get(e, dataStore, some_order_key);
    BaseOrderUtils.CreateOrderParams postcond_closing_order_params = closing_create_order_params_from_order(postcond_props);
    // Assert: for any key in the list of order keys, it is possible
    // to create an order, and then also execute it.
    exchangeRouter.createOrder@withrevert(e, postcond_closing_order_params);
    bool createOrderRevertedPost = lastReverted;
    exchangeRouter.simulateExecuteOrder@withrevert(e, some_order_key, oracle_price_params);
    bool executeOrderRevertedPost = lastReverted;
    assert postcond_contains_key == precond_contains_key;
    assert postcond_contains_key => !createOrderRevertedPost && !executeOrderRevertedPost;
}

rule market_can_be_closed_cancelWithdrawal {
    // TODO: need real definition of "markets can be closed"
    // For now I think this could mean:
    // * for all existing deposits: a withdrawals can be created
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


rule users_can_redeem_market_tokens_cancelWithdrawal {
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

rule no_bank_run_scenario_cancelWithdrawal {
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

rule sanity_cancelWithdrawal{
    env e;
    bytes32 arg;
    cancelWithdrawal(e, arg);
    assert false;
}