
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

function closing_create_order_params_from_order(Order.Props props) returns BaseOrderParams.CreateOrderParams {
    BaseOrderParams.CreateOrderParams close_order_params;
    BaseOrderParams.CreateOrderParamsAddresses close_order_addresses;
    BaseOrderParams.CreateOrderParamsNumbers close_order_numbers;


    // addresses
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

    return close_order_params;
}

rule positions_can_be_closed_cancelWithdrawal(DataStore dataStore, bytes32 some_order_key) {
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

    // Used for both precond and postcond since we assume the
    // prices do not change
    OracleUtils.SimulatePricesParams oracle_price_params;

    //========================================================================
    // Require: positions can be closed before executing the call
    //========================================================================
    bytes32 some_order_key; 
    bool contains_key;
    // this key is in the list of orders
    contains_key = dataStore.containsBytes32(Keys.ORDER_LIST, some_order_key);
    Order.Props props = OrderStoreUtils.get(dataStore, some_order_key);
    BaseOrderParams.CreateOrderParams closing_order_params = closing_create_order_params_from_order(props);

    // Require: for any key in the list of order keys, it is possible
    // to create an order, and then also execute it.
    ExchangeRouter.createOrder@withrevert(e, closing_order_params);
    bool createOrderReverted = lastReverted;
    // Ideally, I would like to really call OrderHandler.executeOrder
    // with a caller that has keeper permissions, but I am not
    // exactly sure how to do this without overspecifying yet... will
    // pivot back
    ExchangeRouter.simulateExecuteOrder(e, oracle_price_params);
    bool executeOrderReverted = lastReverted;

    require (contains_key /* todo add conjunct specifying other reasonable conditions that prevent a revert */ => !createOrderReverted && !executeOrderReverted);
    
    //========================================================================
    // Execute the call: cancelWithdrawal
    //========================================================================

    //========================================================================
    // Assert: positions can be closed after executing the call
    //========================================================================

    // just sanity check for now
    assert false;
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

function solvency() returns bool {
    // TODO need real definition of this.
    return market_can_be_closed() && positions_can_be_closed() &&
        users_can_redeem_market_tokens() && !bank_run_scenario();
}

rule sanity_cancelWithdrawal{
    env e;
    bytes32 arg;
    cancelWithdrawal(e, arg);
    assert false;
}

rule solvency_invariant_cancelWithdrawal {
    env e;
    bytes32 arg;
    require solvency();
    cancelWithdrawal(e, arg);
    assert solvency();
}