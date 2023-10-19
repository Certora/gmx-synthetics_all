using DecreaseOrderUtilsHarness as decreaseOrderUtils;
using ArrayHarness as Array;
using GetPositionKeyHarness as positionKeyHarness;
using PositionStoreUtils as PositionStoreUtils;

methods {
    //Datastore
    function _.getUint(bytes32 key) external => NONDET;
    function _.setUint(bytes32 key, uint256 value) external => NONDET;
    function _.removeUint(bytes32 key) external => NONDET;
    function _.applyDeltaToUint(bytes32 key, int256 value, string) external => DISPATCHER(true);
    function _.applyDeltaToUint(bytes32 key, uint256 value) external => DISPATCHER(true);
    function _.applyBoundedDeltaToUint(bytes32 key, int256 value) external => DISPATCHER(true);
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
    function _.getBool(bytes32 key) external => DISPATCHER(true);
    function _.setBool(bytes32 key, bool value) external => NONDET;
    function _.removeBool(bytes32 key) external => NONDET;
    function _.getString(bytes32 key) external => NONDET;
    function _.setString(bytes32 key, string) external => NONDET;
    function _.removeString(bytes32 key) external => NONDET;
    function _.getBytes32(bytes32 key) external => DISPATCHER(true);
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

    // PositionUtils
    function PositionUtils.getPositionKey(address account, address market, address collateralToken, bool isLong) internal returns (bytes32) => NONDET;
    // PositionUtils.UpdatePositionParams TODO

    // PositionStoreUtils.sol
    function PositionStoreUtils.get(address dataStore, bytes32 key) external returns (Position.Props) optional => NONDET;

    // DecreasePositionUtils
    function DecreasePositionUtils.decreasePosition(
        PositionUtils.UpdatePositionParams params
    ) external returns (DecreasePositionUtils.DecreasePositionResult) => NONDET;

    // SwapUtils
    function SwapUtils.swap(SwapUtils.SwapParams params) external returns (address, uint256) => NONDET;
}

// Arrays are not allowed arguments of ghost functions in CVL
// ghost areGreaterThanOrEqualToGhost(uint256[], uint256) returns bool;


// TODO if this does not perform well, try specifying using individual array indices.
rule decrease_executed_with_right_block_prices1 {
    env e;
    BaseOrderUtils.ExecuteOrderParams params;

    decreaseOrderUtils.processOrder(e, params);

    require (params.order.numbers.orderType == Order.OrderType.MarketDecrease);
        
    assert Array.areLessThanOrEqualTo(e,
            params.minOracleBlockNumbers, params.order.numbers.updatedAtBlock);
    assert Array.areGreaterThanOrEqualTo(e,
            params.maxOracleBlockNumbers, params.order.numbers.updatedAtBlock);
}

rule decrease_executed_with_right_block_prices2 {
    env e;
    BaseOrderUtils.ExecuteOrderParams params;

    decreaseOrderUtils.processOrder(e, params);

    Order.Props order = params.order;
    bytes32 positionKey = positionKeyHarness.getPositionKey(e, order.addresses.account, order.addresses.market, order.addresses.initialCollateralToken, order.flags.isLong);
    Position.Props position = PositionStoreUtils.get(e, params.contracts.dataStore, positionKey);

    uint256 positionIncreasedAtBlock = position.numbers.increasedAtBlock;
    
    uint256 latestUpdatedAtBlock = 
        params.order.numbers.updatedAtBlock > positionIncreasedAtBlock ? 
        params.order.numbers.updatedAtBlock : 
        positionIncreasedAtBlock;
    require params.order.numbers.orderType == Order.OrderType.LimitDecrease ||
            params.order.numbers.orderType == Order.OrderType.StopLossDecrease;
    assert Array.areGreaterThanOrEqualTo(e,
            params.minOracleBlockNumbers, latestUpdatedAtBlock);
}

rule decrease_executed_with_right_block_prices3 {
    env e;
    BaseOrderUtils.ExecuteOrderParams params;

    decreaseOrderUtils.processOrder(e, params);

    Order.Props order = params.order;
    bytes32 positionKey = positionKeyHarness.getPositionKey(e, order.addresses.account, order.addresses.market, order.addresses.initialCollateralToken, order.flags.isLong);
    Position.Props position = PositionStoreUtils.get(e, params.contracts.dataStore, positionKey);

    uint256 positionIncreasedAtBlock = position.numbers.increasedAtBlock;
    uint256 positionDecreasedAtBlock = position.numbers.decreasedAtBlock;
    uint256 latestUpdatedAtBlock = positionIncreasedAtBlock > positionDecreasedAtBlock ? positionIncreasedAtBlock : positionDecreasedAtBlock;

    require params.order.numbers.orderType == Order.OrderType.Liquidation;
    assert Array.areGreaterThanOrEqualTo(e,
            params.minOracleBlockNumbers, latestUpdatedAtBlock);
}