
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

function market_can_be_closed() returns bool {
    // TODO need real definition of this.
    return true;
}

// Simple initial version of this... 
//    * withdrawals can be created for all deposits executed
//    * all the created withdrawals can be executed
function positions_can_be_closed() returns bool {
    // TODO need real definition of this.
    // withdrawals are created by calling WithdrawlStoreUtils.set(datastore,key,withdrawl) where withdrawal is a large struct.
    // deposits are created by calling DepositStoreUtils.set(datastore, key, deposit), where again a deposit is a large struct.
    // executed ? ...
    return true;
}

function users_can_redeem_market_tokens() returns bool {
    // TODO need real definition of this.
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