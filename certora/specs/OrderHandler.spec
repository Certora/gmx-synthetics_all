using WNT as wnt;

methods {  
    //OrderHandler - createOrder
    function _.createOrderFeatureDisabledKey(address,uint256) internal => NONDET;
    function _.validateFeature(address,bytes32) internal => NONDET;
    function _.createOrder(address,address,address,address,address,BaseOrderUtils.CreateOrderParams) external => NONDET;

    //OrderHandler - updateOrder
    function _.isMarketOrder(Order.OrderType) internal => NONDET;
    function _.wnt(address) internal => myWNT() expect address;
    function _.estimateExecuteOrderGasLimit(address, Order.Props memory) internal => NONDET;
    function _.validateExecutionFee(address,uint256,uint256) internal => NONDET;

    //OrderHandler - cancelOrder
    function _.cancelOrderFeatureDisabledKey(address,uint256) internal => NONDET;
    function _.validateRequestCancellation(address,uint256,string memory) internal => NONDET;
    function _.cancelOrder(address,address,address,bytes32,address,uint256,string,bytes) external => NONDET;

    //OrderHandler - simulateExecuteOrder
    function _._executeOrder(bytes32,OracleUtils.SetPricesParams,address) external => NONDET;
    // Oracle.setPrimaryPrice => NONDET (see below)

    //OrderHandler - executeOrder
    function _.getExecutionGas(address,uint256) internal => NONDET;
    function _handleOrderError(bytes32,uint256,bytes memory) internal => NONDET;
    function _.getUncompactedOracleBlockNumbers(uint256[] memory,uint256) internal => NONDET;
    function _.executeOrderFeatureDisabledKey(address,uint256) internal => NONDET;
    function _.getErrorSelectorFromData(bytes memory) internal => NONDET;
    function _.isOracleError(bytes4) internal => NONDET;
    function _.revertWithCustomError(bytes memory) internal => NONDET;
    function _.getRevertMessage(bytes memory) internal => NONDET;


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

    //Bank
    function _.transferOut(address,address,uint256,bool) external => DISPATCHER(true);
    function _.transferOut(address,address,uint256) external => DISPATCHER(true);

    //Datastore

    // function _.getUint(bytes32 key) external => DISPATCHER(true);
    // function _.setUint(bytes32 key, uint256 value) external => DISPATCHER(true);
    // function _.removeUint(bytes32 key) external => DISPATCHER(true);
    // function _.applyDeltaToUint(bytes32 key, int256 value, string) external => DISPATCHER(true);
    // function _.applyDeltaToUint(bytes32 key, uint256 value) external => DISPATCHER(true);
    // function _.applyBoundedDeltaToUint(bytes32 key, int256 value) external => DISPATCHER(true);
    // function _.incrementUint(bytes32 key, uint256 value) external => DISPATCHER(true);
    // function _.decrementUint(bytes32 key, uint256 value) external => DISPATCHER(true);
    // function _.getInt(bytes32 key) external => DISPATCHER(true);
    // function _.setInt(bytes32 key, int256 value) external => DISPATCHER(true);
    // function _.removeInt(bytes32 key) external => DISPATCHER(true);
    // function _.applyDeltaToInt(bytes32 key, int256 value) external => DISPATCHER(true);
    // function _.incrementInt(bytes32 key, int256 value) external => DISPATCHER(true);
    // function _.decrementInt(bytes32 key, int256 value) external => DISPATCHER(true);
    // function _.getAddress(bytes32 key) external => DISPATCHER(true);
    // function _.setAddress(bytes32 key, address value) external => DISPATCHER(true);
    // function _.removeAddress(bytes32 key) external => DISPATCHER(true);
    // function _.getBool(bytes32 key) external => DISPATCHER(true);
    // function _.setBool(bytes32 key, bool value) external => DISPATCHER(true);
    // function _.removeBool(bytes32 key) external => DISPATCHER(true);
    // function _.getString(bytes32 key) external => DISPATCHER(true);
    // function _.setString(bytes32 key, string) external => DISPATCHER(true);
    // function _.removeString(bytes32 key) external => DISPATCHER(true);
    // function _.getBytes32(bytes32 key) external => DISPATCHER(true);
    // function _.setBytes32(bytes32 key, bytes32 value) external => DISPATCHER(true);
    // function _.removeBytes32(bytes32 key) external => DISPATCHER(true);
    // function _.getUintArray(bytes32 key) external => DISPATCHER(true);
    // function _.setUintArray(bytes32 key, uint256[]) external => DISPATCHER(true);
    // function _.removeUintArray(bytes32 key) external => DISPATCHER(true);
    // function _.getIntArray(bytes32 key) external => DISPATCHER(true);
    // function _.setIntArray(bytes32 key, int256[]) external => DISPATCHER(true);
    // function _.removeIntArray(bytes32 key) external => DISPATCHER(true);
    // function _.getAddressArray(bytes32 key) external => DISPATCHER(true);
    // function _.setAddressArray(bytes32 key, address[]) external => DISPATCHER(true);
    // function _.removeAddressArray(bytes32 key) external => DISPATCHER(true);
    // function _.getBoolArray(bytes32 key) external => DISPATCHER(true);
    // function _.setBoolArray(bytes32 key, bool[]) external => DISPATCHER(true);
    // function _.removeBoolArray(bytes32 key) external => DISPATCHER(true);
    // function _.getStringArray(bytes32 key) external => DISPATCHER(true);
    // function _.setStringArray(bytes32 key, string[]) external => DISPATCHER(true);
    // function _.removeStringArray(bytes32 key) external => DISPATCHER(true);
    // function _.getBytes32Array(bytes32 key) external => DISPATCHER(true);
    // function _.setBytes32Array(bytes32 key, bytes32[]) external => DISPATCHER(true);
    // function _.removeBytes32Array(bytes32 key) external => DISPATCHER(true);
    // function _.containsBytes32(bytes32 setKey, bytes32 value) external => DISPATCHER(true);
    // function _.getBytes32Count(bytes32 setKey) external => DISPATCHER(true);
    // function _.getBytes32ValuesAt(bytes32 setKey, uint256 start, uint256 end) external => DISPATCHER(true);
    // function _.addBytes32(bytes32 setKey, bytes32 value) external => DISPATCHER(true);
    // function _.removeBytes32(bytes32 setKey, bytes32 value) external => DISPATCHER(true);
    // function _.containsAddress(bytes32 setKey, address value) external => DISPATCHER(true);
    // function _.getAddressCount(bytes32 setKey) external => DISPATCHER(true);
    // function _.getAddressValuesAt(bytes32 setKey, uint256 start, uint256 end) external => DISPATCHER(true);
    // function _.addAddress(bytes32 setKey, address value) external => DISPATCHER(true);
    // function _.removeAddress(bytes32 setKey, address value) external => DISPATCHER(true);
    // function _.containsUint(bytes32 setKey, uint256 value) external => DISPATCHER(true);
    // function _.getUintCount(bytes32 setKey) external => DISPATCHER(true);
    // function _.getUintValuesAt(bytes32 setKey, uint256 start, uint256 end) external => DISPATCHER(true);
    // function _.addUint(bytes32 setKey, uint256 value) external => DISPATCHER(true);
    // function _.removeUint(bytes32 setKey, uint256 value) external => DISPATCHER(true);



    function _.getUint(bytes32 key) external => NONDET;
    function _.setUint(bytes32 key, uint256 value) external => NONDET;
    function _.removeUint(bytes32 key) external => NONDET;
    function _.applyDeltaToUint(bytes32 key, int256 value, string) external => NONDET;
    function _.applyDeltaToUint(bytes32 key, uint256 value) external => NONDET;
    function _.applyBoundedDeltaToUint(bytes32 key, int256 value) external => NONDET;
    function _.incrementUint(bytes32 key, uint256 value) external => NONDET;
    function _.decrementUint(bytes32 key, uint256 value) external => NONDET;
    function _.getInt(bytes32 key) external => NONDET;
    function _.setInt(bytes32 key, int256 value) external => NONDET;
    function _.removeInt(bytes32 key) external => NONDET;
    function _.applyDeltaToInt(bytes32 key, int256 value) external => NONDET;
    function _.incrementInt(bytes32 key, int256 value) external => NONDET;
    function _.decrementInt(bytes32 key, int256 value) external => NONDET;
    function _.getAddress(bytes32 key) external => NONDET;
    function _.setAddress(bytes32 key, address value) external => NONDET;
    function _.removeAddress(bytes32 key) external => NONDET;
    function _.getBool(bytes32 key) external => NONDET;
    function _.setBool(bytes32 key, bool value) external => NONDET;
    function _.removeBool(bytes32 key) external => NONDET;
    function _.getString(bytes32 key) external => NONDET;
    function _.setString(bytes32 key, string) external => NONDET;
    function _.removeString(bytes32 key) external => NONDET;
    function _.getBytes32(bytes32 key) external => NONDET;
    function _.setBytes32(bytes32 key, bytes32 value) external => NONDET;
    function _.removeBytes32(bytes32 key) external => NONDET;
    function _.getUintArray(bytes32 key) external => NONDET;
    function _.setUintArray(bytes32 key, uint256[]) external => NONDET;
    function _.removeUintArray(bytes32 key) external => NONDET;
    function _.getIntArray(bytes32 key) external => NONDET;
    function _.setIntArray(bytes32 key, int256[]) external => NONDET;
    function _.removeIntArray(bytes32 key) external => NONDET;
    function _.getAddressArray(bytes32 key) external => NONDET;
    function _.setAddressArray(bytes32 key, address[]) external => NONDET;
    function _.removeAddressArray(bytes32 key) external => NONDET;
    function _.getBoolArray(bytes32 key) external => NONDET;
    function _.setBoolArray(bytes32 key, bool[]) external => NONDET;
    function _.removeBoolArray(bytes32 key) external => NONDET;
    function _.getStringArray(bytes32 key) external => NONDET;
    function _.setStringArray(bytes32 key, string[]) external => NONDET;
    function _.removeStringArray(bytes32 key) external => NONDET;
    function _.getBytes32Array(bytes32 key) external => NONDET;
    function _.setBytes32Array(bytes32 key, bytes32[]) external => NONDET;
    function _.removeBytes32Array(bytes32 key) external => NONDET;
    function _.containsBytes32(bytes32 setKey, bytes32 value) external => NONDET;
    function _.getBytes32Count(bytes32 setKey) external => NONDET;
    function _.getBytes32ValuesAt(bytes32 setKey, uint256 start, uint256 end) external => NONDET;
    function _.addBytes32(bytes32 setKey, bytes32 value) external => NONDET;
    function _.removeBytes32(bytes32 setKey, bytes32 value) external => NONDET;
    function _.containsAddress(bytes32 setKey, address value) external => NONDET;
    function _.getAddressCount(bytes32 setKey) external => NONDET;
    function _.getAddressValuesAt(bytes32 setKey, uint256 start, uint256 end) external => NONDET;
    function _.addAddress(bytes32 setKey, address value) external => NONDET;
    function _.removeAddress(bytes32 setKey, address value) external => NONDET;
    function _.containsUint(bytes32 setKey, uint256 value) external => NONDET;
    function _.getUintCount(bytes32 setKey) external => NONDET;
    function _.getUintValuesAt(bytes32 setKey, uint256 start, uint256 end) external => NONDET;
    function _.addUint(bytes32 setKey, uint256 value) external => NONDET;
    function _.removeUint(bytes32 setKey, uint256 value) external => NONDET;



    //Oracle
    function _.getPrimaryPrice(address) external => NONDET;
    function _.setPrices(address,address,OracleUtils.SetPricesParams) external => NONDET;
    function _.clearAllPrices() external => NONDET;
    function _.setPrimaryPrice(address,Price.Props) external => NONDET;

    //RoleStore
    function _.hasRole(address,bytes32) external => DISPATCHER(true);
    function _.revokeRole(address,bytes32) external => DISPATCHER(true);
    function _.grantRole(address,bytes32) external => DISPATCHER(true);

    //GlobalReentrancyGuard
    function _._nonReentrantBefore() internal => NONDET;
    function _._nonReentrantAfter() internal => NONDET;

    //RoleModule
    function _._validateRole(bytes32,string memory) internal => NONDET;

    //ArbSys
    function _.arbBlockNumber() external => NONDET;
    function _.arbBlockHash(uint256) external => NONDET;

    //DepositEventUtils
    function _.emitDepositCreated(address,bytes32,Deposit.Props) external => NONDET;

    //MarketStoreUtils
    function _.get(address, address) external => NONDET;

    //StrictBank
    function _.recordTransferIn(address) external => NONDET;

    //DepositStoreUtils
    function _.set(address,bytes32,Deposit.Props) external => NONDET;

}

ghost myWNT() returns address {
	init_state axiom myWNT() == wnt;
}

/*rule sanity(method f) {
    env e;
    calldataarg args;
    f(e, args);
    assert false;
}*/

/*rule claimFeesTest() {
    env e;
    calldataarg args;

    address[] markets;
    address[] tokens;

    require markets.length == 1;

    claimFees(e, markets, tokens);
    assert false;
}*/

rule createOrderOnly() {
    env e;
    calldataarg args;
    createOrder(e, args);
    assert false;
}

rule updateOrderOnly() {
    env e; calldataarg args;
    //updateOrder(e, args);
    
    bytes32 key;
    uint256 sizeDeltaUsd;
    uint256 acceptablePrice;
    uint256 triggerPrice;
    uint256 minOutputAmount;
    Order.Props order;

    require order.addresses.account == 0;
    require order.addresses.receiver == 0;
    require order.addresses.callbackContract == 0;
    require order.addresses.uiFeeReceiver == 0;
    require order.addresses.market == 0;
    require order.addresses.initialCollateralToken == 0;
    //require order.addresses.swapPath == address [0]; //not working

    //require order.numbers.orderType == MarketSwap; //not working
    //require order.numbers.decreasePositionSwapType == NoSwap; //not working
    require order.numbers.sizeDeltaUsd == 0;
    require order.numbers.initialCollateralDeltaAmount == 0;
    require order.numbers.triggerPrice == 0;
    require order.numbers.acceptablePrice == 0;
    require order.numbers.executionFee == 0;
    require order.numbers.callbackGasLimit == 0;
    require order.numbers.minOutputAmount == 0;
    require order.numbers.updatedAtBlock == 0;

    require order.flags.isLong == false;
    require order.flags.shouldUnwrapNativeToken == false;
    require order.flags.isFrozen == false;

    updateOrder(e, key, sizeDeltaUsd, acceptablePrice, triggerPrice, minOutputAmount, order);
    assert false;
}

rule cancelOrderOnly() {
    env e;
    calldataarg args;
    cancelOrder(e, args);
    assert false;
}

rule simulateExecuteOrderOnly() {
    env e;
    calldataarg args;
    simulateExecuteOrder(e, args);
    assert false;
}

rule executeOrderOnly() {
    env e;
    calldataarg args;
    executeOrder(e, args);
    assert false;
}

rule _executeOrderOnly() {
    env e;
    calldataarg args;
    _executeOrder(e, args);
    assert false;
}