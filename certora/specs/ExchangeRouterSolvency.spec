using ExchangeRouter as exchangeRouter;
using DataStore as dataStore;
using KeysHarness as keys;
using OrderStoreUtils as orderStoreUtils;
// Solvency:
// * The market can be fully closed
// * All positions can be closed
// * All users can redeem market tokens
// * There is no bank run scenario
//         meaning the first to withdraw gets a higher value per market token
//         than last to withdraw

// We aim to prove that, as long as the price is held constant, no sequence
// of user actions can break solvency. Actions: increase/decrease position,
// swap, deposit, withdraw, collect funding/borrowing fees.

// Strategy: give a definition for "solvency" for a market 
// in terms of either the internal state of the system or the observable
// behavior of the system (i.e. ability for calls to succeed). For each
// function that is callable by the public: prove that assuming the market
// "is solvent" initially, prove that after the call the market "is solvent"

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

//=============================================================================
// Solvency
//=============================================================================
// Solvency is broken down into a few smaller invariants:
// 1) All open positions can be closed
// 2) The market can be closed (all money can be withdrawn)
// 3) Users can redeem market tokens (all fees can be collected)
// 4) There is no bank run scenario
//=============================================================================

// function ORDER_LIST() returns bytes32 {
//     // hex is 1c0ed28dbf4dbab6e3b05ec6984dab52b8bf44cf925b113e5c131897d38539e6
//     // bytes32 order_list =  12690948807470286051617335600493479205455250750719689145299770941367493409254;
//     bytes32 order_list =  0x1c0ed28dbf4dbab6e3b05ec6984dab52b8bf44cf925b113e5c131897d38539e6;
//     return order_list;
// }

function closing_create_order_params_from_order(Order.Props props) returns BaseOrderUtils.CreateOrderParams {
    BaseOrderUtils.CreateOrderParams close_order_params;
    BaseOrderUtils.CreateOrderParamsAddresses close_order_addresses;
    BaseOrderUtils.CreateOrderParamsNumbers close_order_numbers;


    // Pending JIRA bug: https://certora.atlassian.net/browse/CERT-2886?atlOrigin=eyJpIjoiYjRlNGM5YWFjZTNiNGVmYjhjNmUyOWFmZjhlOTZkYzIiLCJwIjoiamlyYS1zbGFjay1pbnQifQ
    // addresses
    /*
    close_order_addresses.receiver = props.addresses.receiver;
    close_order_addresses.callbackContract = props.addresses.callbackContract;
    close_order_addresses.uiFeeReceiver = props.addresses.uiFeeReceiver;
    close_order_addresses.market = props.addresses.market;
    close_order_addresses.initialCollateralToken= props.addresses.initialCollateralToken;
    close_order_addresses.swapPath = props.addresses.swapPath;
    close_order_params.addresses = close_order_addresses;

    // numbers
    close_order_numbers.sizeDeltaUsd = props.numbers.sizeDeltaUsd;
    close_order_numbers.initialCollateralDeltaAmount = props.numbers.initialCollateralDeltaAmount;
    close_order_numbers.triggerPrice = props.numbers.triggerPrice;
    close_order_numbers.acceptablePrice = props.numbers.acceptablePrice;
    close_order_numbers.executionFee = props.numbers.executionFee;
    close_order_numbers.callbackGasLimit = props.numbers.callbackGasLimit;
    close_order_numbers.minOutputAmount = props.numbers.minOutputAmount;
    close_order_params.numbers = close_order_numbers;

    close_order_orderType = props.orderType;
    close_order_decreasePositionSwapType = props.decreasePositionSwapType;

    // Note: a close order should be in the opposite direction
    close_order_params.isLong = !props.flags.isLong;
    close_order_params.shouldUnwrapNativeToken = props.flags.shouldUnwrapNativeToken;
    */

    return close_order_params;
}

rule positions_can_be_closed_cancelWithdrawal {
    // TODO need real definition of this.
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

function market_can_be_closed() returns bool {
    // TODO need real definition of this.
    // Initial version of this:
    // * withdrawals can be created for all deposits executed
    // * all the created withdrawals can be executed
    // withdrawals are created by calling WithdrawlStoreUtils.set(datastore,key,withdrawl) where withdrawal is a large struct.
    // deposits are created by calling DepositStoreUtils.set(datastore, key, deposit), where again a deposit is a large struct.
    // executed ? ...
    return true;
}


function users_can_redeem_market_tokens() returns bool {
    // TODO need real definition of this.
    // Is it: all the fees can be collected ?
    return true;
}

function bank_run_scenario() returns bool {
    // TODO need real definition of this.
    return false;
}

// function solvency() returns bool {
//     // TODO need real definition of this.
//     return market_can_be_closed() && positions_can_be_closed() &&
//         users_can_redeem_market_tokens() && !bank_run_scenario();
// }

rule sanity_cancelWithdrawal{
    env e;
    bytes32 arg;
    cancelWithdrawal(e, arg);
    assert false;
}