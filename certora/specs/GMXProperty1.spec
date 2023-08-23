// The goal of this spec is to mechanize a property requested by GMX
// which is quoted here:
//=============================================================================
// GMX Request
//=============================================================================
// 1. if the price value is the same, no sequence of actions should result in a net profit, or another way to phrase it would be that markets should always be solvent if price does not change

/*
* Idea for implementation:
* a. assume oracle prices stay the same
* b. close arbitrary position anc check how much value you get (store this value)
* c. go back to the state before you closed the position above
* d. perform any arbitrary action (swap/withdraw/etc)
* e. close again the same position in b. and check the value you get
* f. assert that the end value in b. =< end value in e.
*/

using OrderHandler as orderHandler;
using DataStore as dataStore;
using KeysHarness as keys;
using PositionUtils as positionUtils;
using PositionStoreUtils as positionStoreUtils;
using GetPositionKeyHarness as positionKeyHarness;

methods {

    // Contracts that are included
    function DataStore._ external => NONDET;

    // OrderHandler
    function  OrderHandler._executeOrder(bytes32, OracleUtils.SetPricesParams, address) external => NONDET;
    function OrderHandler.createOrder(address, BaseOrderUtils.CreateOrderParams) external returns (bytes32) => NONDET;

    // ALL the libraries...
    function OrderUtils._ external => NONDET;
    function OrderStoreUtils._ external => NONDET;
    function DecreaseOrderUtils._ external => NONDET;
    function ErrorUtils._ external => NONDET;

    function OrderEventUtils._ external => NONDET;
    function Order._ external => NONDET;
    function TokenUtils._ external => NONDET;
    function BaseOrderUtils._ external => NONDET;
    function SwapOrderUtils._ external => NONDET;
    function IncreaseOrderUtils._ external => NONDET;
    function ReferralTier._ external => NONDET;
    function ReferralUtils._ external => NONDET;

    function GasUtils._ external => NONDET;
    function Deposit._ external => NONDET;
    function NonceUtils._ external => NONDET;
    function Position._ external => NONDET;
    function PositionUtils._ external => NONDET;
    function DecreasePositionUtils._ external => NONDET;
    function PositionStoreUtils._ external => NONDET;
    function DecreasePositionCollateralUtils._ external => NONDET;
    function PositionEventUtils._ external => NONDET;
    
    function IncreasePositionUtils._ external => NONDET;
    function Withdrawal._ external => NONDET;
    function OracleUtils._ external => NONDET;
    function SwapUtils._ external => NONDET;
    function Uint256Mask._ external => NONDET;
    function AccountUtils._ external => NONDET;
    function Array._ external => NONDET;
    function Calc._ external => NONDET;
    function Precision._ external => NONDET;
    function EnumerableValues._ external => NONDET;
    function Chain._ external => NONDET;
    
    function AdlUtils._ external => NONDET;
    function Price._ external => NONDET;
    function MarketPoolValueInfo._ external => NONDET;
    function MarketUtils._ external => NONDET;
    function MarketEventUtils._ external => NONDET;
    function MarketStoreUtils._ external => NONDET;
    function Market._ external => NONDET;
    function FeatureUtils._ external => NONDET;
    function CallbackUtils._ external => NONDET;
    function Keys._ external => NONDET;
    function PositionPricingUtils._ external => NONDET;
    function PricingUtils._ external => NONDET;
    function SwapPricingUtils._ external => NONDET;
    function EventUtils._ external => NONDET;

    // missed libs
    function SignedMath._ external => NONDET;
    function SafeCast._ external => NONDET;

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

function positions_closable(env e, OracleUtils.SetPricesParams oracle_price_params, uint256 close_value) returns bool {
    address some_account;
    address some_market;
    address some_collateral_token;
    bool some_is_long;
    bytes32 some_position_key = positionKeyHarness.getPositionKey(e, some_account, some_market, some_collateral_token, some_is_long);
    Position.Props position = positionStoreUtils.get(e, dataStore, some_position_key);
    // save whether or not the position is empty, but do NOT require it.
    // At the end of the rule, we require that if the position (any position),
    // is non-empty, then it must be possible to create and execute an order
    // that undoes it.
    bool non_empty_position = !isPositionEmpty(position);
    require non_empty_position;
    BaseOrderUtils.CreateOrderParams closing_order_params = closing_create_order_params_from_position(position);

    bytes32 closing_order_key = orderHandler.createOrder@withrevert(e, some_account, closing_order_params); 
    bool createOrderReverted = lastReverted;
    orderHandler.executeOrder@withrevert(e, closing_order_key, oracle_price_params);
    bool executeOrderReverted = lastReverted;

    // Assuming the created order goes through, the close_value is the
    // value returned.
    // NOTE: There are two prices in CreateOrderParams -- triggerPrice and 
    // acceptablePrice. I am not exactly sure which one is right for this.
    // It could also be that the price used depends on whether it is long 
    // or short?
    // The argument close_value is used to track the value returned from
    // closing the position before and after an order is made.
    require close_value == assert_uint256(closing_order_params.numbers.sizeDeltaUsd * 
        closing_order_params.numbers.triggerPrice);

    // If the position is non-empty, it is possible to create and execute an
    // an order 
    // return non_empty_position => !createOrderReverted && !executeOrderReverted;
    return !createOrderReverted && !executeOrderReverted;
}

/*
function withdrawal_params_from_position(env e, Position.Props position) 
    returns WithdrawalUtils.CreateWithdrawalParams {
    // TODO

    WithdrawalUtils.CreateWithdrawalParams withdrawal_params;
    return withdrawal_params;
}

function positions_closable_by_burning(env e, 
        OracleUtils.SetPricesParams oracle_price_params, 
        uint256 close_value) returns bool {
    address some_account;
    address some_market;
    address some_collateral_token;
    bool some_is_long;
    bytes32 some_position_key = positionKeyHarness.getPositionKey(e, some_account, some_market, some_collateral_token, some_is_long);
    Position.Props position = positionStoreUtils.get(e, dataStore, some_position_key);
    // save whether or not the position is empty, but do NOT require it.
    // At the end of the rule, we require that if the position (any position),
    // is non-empty, then it must be possible to withdraw it.
    bool non_empty_position = !isPositionEmpty(position);
    WithdrawalUtils.CreateWithdrawalParams burning_withdrawal_params = 
        withdrawal_params_from_position(e, position);

    bytes32 withdrawal_order_key = withdrawalHandler.createWithdrawal@withrevert(some_account, burning_withdrawal_params);
    bool createWithdrawalReverted = lastReverted;
    withdrawalHandler.executeOrder(e, withdrawal_order_key, oracle_price_params);
    bool withdrawalOrderReverted = lastReverted;

    // TODO
    require close_value == 0;

    return non_empty_position => !createWithdrawalReverted && !executeReverted;

}
*/

rule positions_can_be_closed {
    // A liveness property that all open positions can be closed, even
    // after arbitrary (potentially adversarial) user actions. More precisely,
    // for any public/external call, we prove an invariant that assuming
    // it was possible to close all open positions before the call, it is still
    // possible to close all open positions after the call.

    // A position is closed by issuing a decrease order (so that it is 
    // decreased to zero).

    env e;
    // This value is used to enforce that the value from closing a position
    // is the same before and after issuing the user command.
    uint256 position_close_value;

    // Used for both precond and postcond since we assume the
    // prices do not change
    OracleUtils.SetPricesParams oracle_price_params;

    // We need to save the state before positions_closable because
    // simulateExecuteOrder in positions_closable is state-changing.
    storage stateBeforePrecond = lastStorage;

    //========================================================================
    // Require: positions can be closed before executing the call
    //========================================================================
    require positions_closable(e, oracle_price_params, position_close_value);

    //========================================================================
    // Execute the call
    //========================================================================
    bytes32 key;
    OracleUtils.SetPricesParams oracleParams;
    orderHandler.executeOrder(e, key, oracleParams) at stateBeforePrecond;

    //========================================================================
    // Assert: positions can be closed after executing the call
    //========================================================================
    assert positions_closable(e, oracle_price_params, position_close_value);
}

/*
rule gmx_property1_strategy2 {
    env e;
    uint256 position_close_value;
    
    // Used for both precond and postcond since we assume the
    // prices do not change
    OracleUtils.SetPricesParams oracle_price_params;

    // We need to save the state before positions_closable because
    // simulateExecuteOrder in positions_closable is state-changing.
    storage stateBeforePrecond = lastStorage;

    //========================================================================
    // Require: positions can be closed before executing the call
    //========================================================================
    require positions_closable_by_burning(e, oracle_price_params, position_close_value);

    //========================================================================
    // Execute the call
    //========================================================================
    bytes32 key;
    OracleUtils.SetPricesParams oracleParams;
    orderHandler.executeOrder(e, key, oracleParams) at stateBeforePrecond;

    //========================================================================
    // Require: positions can be closed before executing the call
    //========================================================================
    assert positions_closable_by_burning(e, oracle_price_params, position_close_value);
}
*/

rule sanity_execute_order {
    env e;
    calldataarg args;
    orderHandler.executeOrder(e, args);
    assert false;
}