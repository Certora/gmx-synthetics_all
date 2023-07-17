
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
    // WithdrawalHandler
    function _.createWithdrawal(address, WithdrawalUtils.CreateWithdrawalParams)  external => NONDET;
    function _.cancelWithdrawal(bytes32) external => NONDET;
    function _.executeWithdrawal(bytes32, OracleUtils.SetPricesParams) external => NONDET;
    function _.simulateExecuteWithdrawal(bytes32, OracleUtils.SimulatePricesParams) external => NONDET;
    function _._executeWithdrawal(bytes32, OracleUtils.SetPricesParams) external => NONDET;
    function _._handleWithdrawalError(bytes32, uint256, bytes memory) internal => NONDET;

    // ERC20
    function _.name()                                external  => DISPATCHER(true);
    function _.symbol()                              external  => DISPATCHER(true);
    function _.decimals()                            external  => DISPATCHER(true);
    function _.totalSupply()                         external  => DISPATCHER(true);
    function _.balanceOf(address)                    external  => DISPATCHER(true);
    function _.allowance(address,address)            external  => DISPATCHER(true);
    function _.approve(address,uint256)              external  => DISPATCHER(true);
    function _.transfer(address,uint256)             external  => DISPATCHER(true);
    function _.transferFrom(address,address,uint256) external  => DISPATCHER(true);

    // WNT
    function _.deposit()                             external  => DISPATCHER(true);
    function _.withdraw(uint256)                     external  => DISPATCHER(true);

    // Bank
    function _.transferOut(address,address,uint256,bool) external => DISPATCHER(true);

    //Datastore
    // function _.setBool(bytes32,bool) external => DISPATCHER(true);
    // function _.getBool(bytes32 key) external => DISPATCHER(true);
    // function _.getUint(bytes32) external => DISPATCHER(true);
    // function _.setUint(bytes32,uint256) external => DISPATCHER(true);
    // function _.addBytes32(bytes32,bytes32) external => DISPATCHER(true);
    // function _.setAddress(bytes32,address) external => DISPATCHER(true);
    // function _.setAddressArray(bytes32, address[]) external => DISPATCHER(true);
    // function _.incrementUint(bytes32,uint256) external => DISPATCHER(true);
    // function _.getAddress(bytes32) external => DISPATCHER(true);
    // function _.containsBytes32(bytes32,bytes32) external => DISPATCHER(true);

    function _.getUint(bytes32 key) external => DISPATCHER(true);
    function _.setUint(bytes32 key, uint256 value) external => DISPATCHER(true);
    function _.removeUint(bytes32 key) external => DISPATCHER(true);
    function _.applyDeltaToUint(bytes32 key, int256 value, string) external => DISPATCHER(true);
    function _.applyDeltaToUint(bytes32 key, uint256 value) external => DISPATCHER(true);
    function _.applyBoundedDeltaToUint(bytes32 key, int256 value) external => DISPATCHER(true);
    function _.incrementUint(bytes32 key, uint256 value) external => DISPATCHER(true);
    function _.decrementUint(bytes32 key, uint256 value) external => DISPATCHER(true);
    function _.getInt(bytes32 key) external => DISPATCHER(true);
    function _.setInt(bytes32 key, int256 value) external => DISPATCHER(true);
    function _.removeInt(bytes32 key) external => DISPATCHER(true);
    function _.applyDeltaToInt(bytes32 key, int256 value) external => DISPATCHER(true);
    function _.incrementInt(bytes32 key, int256 value) external => DISPATCHER(true);
    function _.decrementInt(bytes32 key, int256 value) external => DISPATCHER(true);
    function _.getAddress(bytes32 key) external => DISPATCHER(true);
    function _.setAddress(bytes32 key, address value) external => DISPATCHER(true);
    function _.removeAddress(bytes32 key) external => DISPATCHER(true);
    function _.getBool(bytes32 key) external => DISPATCHER(true);
    function _.setBool(bytes32 key, bool value) external => DISPATCHER(true);
    function _.removeBool(bytes32 key) external => DISPATCHER(true);
    function _.getString(bytes32 key) external => DISPATCHER(true);
    function _.setString(bytes32 key, string) external => DISPATCHER(true);
    function _.removeString(bytes32 key) external => DISPATCHER(true);
    function _.getBytes32(bytes32 key) external => DISPATCHER(true);
    function _.setBytes32(bytes32 key, bytes32 value) external => DISPATCHER(true);
    function _.removeBytes32(bytes32 key) external => DISPATCHER(true);
    function _.getUintArray(bytes32 key) external => DISPATCHER(true);
    function _.setUintArray(bytes32 key, uint256[]) external => DISPATCHER(true);
    function _.removeUintArray(bytes32 key) external => DISPATCHER(true);
    function _.getIntArray(bytes32 key) external => DISPATCHER(true);
    function _.setIntArray(bytes32 key, int256[]) external => DISPATCHER(true);
    function _.removeIntArray(bytes32 key) external => DISPATCHER(true);
    function _.getAddressArray(bytes32 key) external => DISPATCHER(true);
    function _.setAddressArray(bytes32 key, address[]) external => DISPATCHER(true);
    function _.removeAddressArray(bytes32 key) external => DISPATCHER(true);
    function _.getBoolArray(bytes32 key) external => DISPATCHER(true);
    function _.setBoolArray(bytes32 key, bool[]) external => DISPATCHER(true);
    function _.removeBoolArray(bytes32 key) external => DISPATCHER(true);
    function _.getStringArray(bytes32 key) external => DISPATCHER(true);
    function _.setStringArray(bytes32 key, string[]) external => DISPATCHER(true);
    function _.removeStringArray(bytes32 key) external => DISPATCHER(true);
    function _.getBytes32Array(bytes32 key) external => DISPATCHER(true);
    function _.setBytes32Array(bytes32 key, bytes32[]) external => DISPATCHER(true);
    function _.removeBytes32Array(bytes32 key) external => DISPATCHER(true);
    function _.containsBytes32(bytes32 setKey, bytes32 value) external => DISPATCHER(true);
    function _.getBytes32Count(bytes32 setKey) external => DISPATCHER(true);
    function _.getBytes32ValuesAt(bytes32 setKey, uint256 start, uint256 end) external => DISPATCHER(true);
    function _.addBytes32(bytes32 setKey, bytes32 value) external => DISPATCHER(true);
    function _.removeBytes32(bytes32 setKey, bytes32 value) external => DISPATCHER(true);
    function _.containsAddress(bytes32 setKey, address value) external => DISPATCHER(true);
    function _.getAddressCount(bytes32 setKey) external => DISPATCHER(true);
    function _.getAddressValuesAt(bytes32 setKey, uint256 start, uint256 end) external => DISPATCHER(true);
    function _.addAddress(bytes32 setKey, address value) external => DISPATCHER(true);
    function _.removeAddress(bytes32 setKey, address value) external => DISPATCHER(true);
    function _.containsUint(bytes32 setKey, uint256 value) external => DISPATCHER(true);
    function _.getUintCount(bytes32 setKey) external => DISPATCHER(true);
    function _.getUintValuesAt(bytes32 setKey, uint256 start, uint256 end) external => DISPATCHER(true);
    function _.addUint(bytes32 setKey, uint256 value) external => DISPATCHER(true);
    function _.removeUint(bytes32 setKey, uint256 value) external => DISPATCHER(true);

    //Oracle
    function _.getPrimaryPrice(address) external => NONDET;
    function _.setPrices(address,address,OracleUtils.SetPricesParams) external  => NONDET;
    function _.clearAllPrices() external  => NONDET;

    //RoleStore
    function _.hasRole(address,bytes32) external => DISPATCHER(true);
    function _.revokeRole(address,bytes32) external => DISPATCHER(true);
    function _.grantRole(address,bytes32) external => DISPATCHER(true);
}

function market_can_be_closed() returns bool {
    return true;
}

// Simple initial version of this... 
//    * withdrawals can be created for all deposits executed
//    * all the created withdrawals can be executed
function positions_can_be_closed() returns bool {
    // withdrawals are created by calling WithdrawlStoreUtils.set(datastore,key,withdrawl) where withdrawal is a large struct.
    // deposits are created by calling DepositStoreUtils.set(datastore, key, deposit), where again a deposit is a large struct.
    // executed ? ...
    return true;
}

function users_can_redeem_market_tokens() returns bool {
    return true;
}

function bank_run_scenario() returns bool {
    return false;
}

function solvency() returns bool {
    return market_can_be_closed() && positions_can_be_closed() &&
        users_can_redeem_market_tokens() && !bank_run_scenario();
}

// rule sanity(method f) {
//     env e;
//     calldataarg args;
//     f(e, args);
//     assert false;
// }

rule sanity_cancelWithdrawal {
    env e;
    bytes32 arg;
    cancelWithdrawal(e, arg);
    assert false;
}