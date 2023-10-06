using DecreaseOrderUtilsHarness as decreaseOrderUtils;
using ArrayHarness as Array;
using GetPositionKeyHarness as positionKeyHarness;
using PositionStoreUtils as PositionStoreUtils;

methods {
    //  external library function signatures may only have 'storage' locations
    // function Array.areGreaterThanOrEqualTo(uint256[] memory arr, uint256 value) external returns (bool) envfree;
    // function Array.areLessThanOrEqualTo(uint256[] memory arr, uint256 value) external returns (bool) envfree;
    // Arrays are not allowed arguments of ghost functions in CVL
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