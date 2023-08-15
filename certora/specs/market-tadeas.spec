using WNT as wnt;
using DummyERC20A as DummyERC20Long;
using DummyERC20B as DummyERC20Short;
using MarketFactory as MF;


methods{
    // // ERC20
    // function _.name()                                external  => DISPATCHER(true);
    // function _.symbol()                              external  => DISPATCHER(true);
    // function _.decimals()                            external  => DISPATCHER(true);
    // function _.totalSupply()                         external  => DISPATCHER(true);
    // function _.balanceOf(address)                    external  => DISPATCHER(true);
    // function _.allowance(address,address)            external  => DISPATCHER(true);
    // function _.approve(address,uint256)              external  => DISPATCHER(true);
    // function _.transfer(address,uint256)             external  => DISPATCHER(true);
    // function _.transferFrom(address,address,uint256) external  => DISPATCHER(true);
    // //Datastore
    // function _.setBool(bytes32,bool) external => DISPATCHER(true);
    // function _.getUint(bytes32) external => DISPATCHER(true);
    // function _.getAddress(bytes32) external => DISPATCHER(true);
    // //RoleStore
    // function _.hasRole(address,bytes32) external => NONDET;
    // function _.revokeRole(address,bytes32) external => NONDET;
    // function _.grantRole(address,bytes32) external => NONDET;
    // function _.getRoleCount() external => NONDET;



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
    //function _.getUncompactedOracleBlockNumbers(uint256[] memory,uint256) internal => NONDET;
    function _.executeOrderFeatureDisabledKey(address,uint256) internal => NONDET;
    function _.getErrorSelectorFromData(bytes memory) internal => NONDET;
    function _.isOracleError(bytes4) internal => NONDET;
    function _.revertWithCustomError(bytes memory) internal => NONDET;
    //function _.getRevertMessage(bytes memory) internal => NONDET;


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

function getMarketParams(address market, address account) returns BaseOrderUtils.CreateOrderParams
{
    BaseOrderUtils.CreateOrderParams params;

    address uiFeeReceiver;
    address initialCollateralToken;

    uint256 sizeDeltaUsd;
    uint256 initialCollateralDeltaAmount;
    uint256 triggerPrice;
    uint256 acceptablePrice;
    uint256 executionFee;
    uint256 callbackGasLimit;
    uint256 minOutputAmount;

    require params.orderType == Order.OrderType.MarketDecrease;
    require params.decreasePositionSwapType == Order.DecreasePositionSwapType.NoSwap;

    //require params.numbers.sizeDeltaUsd == 

    require params.addresses.receiver == account;
    require params.addresses.callbackContract == 0;
    require params.addresses.uiFeeReceiver == uiFeeReceiver;
    require params.addresses.market == market;  // we have to verify in separate rule
                                                // no interference between markets
    require params.addresses.initialCollateralToken == initialCollateralToken;
    require params.addresses.swapPath.length == 0;

    require params.numbers.sizeDeltaUsd == sizeDeltaUsd;
    require params.numbers.initialCollateralDeltaAmount == initialCollateralDeltaAmount;
    require params.numbers.triggerPrice == triggerPrice;
    require params.numbers.acceptablePrice == acceptablePrice;
    require params.numbers.executionFee == executionFee;
    require params.numbers.callbackGasLimit == callbackGasLimit;
    require params.numbers.minOutputAmount == minOutputAmount;


    // require indexToken
    // require longToken
    // require reserveFactor < 1

    // Save this state

    // create order (decrease order type) and get its key
    // execute the order with the key above - if it passed it means solvent

    return params;   
}


function getOracleParams() returns OracleUtils.SetPricesParams
{
    OracleUtils.SetPricesParams params;
        // params.signerInfo;
        // params.tokens;
        // params.compactedMinOracleBlockNumbers;
        // params.compactedMaxOracleBlockNumbers;
        // params.compactedOracleTimestamps;
        // params.compactedDecimals;
        // params.compactedMinPrices;
        // params.compactedMinPricesIndexes;
        // params.compactedMaxPrices;
        // params.compactedMaxPricesIndexes;
        // params.signatures;
        // params.priceFeedTokens;
    return params;
}

rule sanity(method f) {
    env e;
    calldataarg args;
    f(e, args);
    assert false;
}

rule GMXmaxPNLFactorLessOneMeansSolventMarket(env e) {
    address account;
    address indexToken;
    address longToken;
    require longToken == DummyERC20Long;
    address shortToken;
    require shortToken == DummyERC20Short;
    bytes32 marketType;

    // index token != long token
    require indexToken != longToken;
    // TODO: max pnl factor for traders<1
    //

    address market;
    Market.Props marketProps = MF.createMarket(e, indexToken, longToken, shortToken, marketType);
    BaseOrderUtils.CreateOrderParams params = getMarketParams(market, account);

    // Assume market is solvent: Assume, that a perticular order can be executed: {
    bytes32 order_key = createOrder(e, account, params);
    
    storage initState = lastStorage;

    OracleUtils.SetPricesParams oracle_params = getOracleParams();
    
    executeOrder(e, order_key, oracle_params);
    // }

    // Change state before executing and change price and in resulting state try again execution.
    // TODO: Change price (how to require the ratio of longToken/shortToken changes)?



    // {
    executeOrder@withrevert(e, order_key, oracle_params);
    bool secondReverted = lastReverted;
    assert !secondReverted;
}




rule GMXMarketAlwaysSolventReserveFactor(env e) {
    address account;
    address market;
    address uiFeeReceiver;
    address initialCollateralToken;

        uint256 sizeDeltaUsd;
        uint256 initialCollateralDeltaAmount;
        uint256 triggerPrice;
        uint256 acceptablePrice;
        uint256 executionFee;
        uint256 callbackGasLimit;
        uint256 minOutputAmount;

    BaseOrderUtils.CreateOrderParams params;

    require params.orderType == Order.OrderType.MarketDecrease;
    require params.decreasePositionSwapType == Order.DecreasePositionSwapType.NoSwap;

    //require params.numbers.sizeDeltaUsd == 

    require params.addresses.receiver == account;
    require params.addresses.callbackContract == 0;
    require params.addresses.uiFeeReceiver == uiFeeReceiver;
    require params.addresses.market == market;  // we have to verify in separate rule
                                                // no interference between markets
    require params.addresses.initialCollateralToken == initialCollateralToken;
    require params.addresses.swapPath.length == 0;

    require params.numbers.sizeDeltaUsd == sizeDeltaUsd;
    require params.numbers.initialCollateralDeltaAmount == initialCollateralDeltaAmount;
    require params.numbers.triggerPrice == triggerPrice;
    require params.numbers.acceptablePrice == acceptablePrice;
    require params.numbers.executionFee == executionFee;
    require params.numbers.callbackGasLimit == callbackGasLimit;
    require params.numbers.minOutputAmount == minOutputAmount;

    OracleUtils.SetPricesParams oracle_params = getOracleParams();

    // require indexToken
    // require longToken
    // require reserveFactor < 1

    // Save this state

    // create order (decrease order type) and get its key
    // execute the order with the key above - if it passed it means solvent
    bytes32 key = createOrder(e, account, params);
    executeOrder(e, key, oracle_params);

    // Go back to state above
    
    // change oracle prices

    // create order (decrease order type) and get its key
    // execute the order with the key above - if it passed it means solvent
    assert false;

}