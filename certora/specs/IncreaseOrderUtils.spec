using IncreaseOrderUtilsHarness as increaseOrderUtils;
using ArrayHarness as array;

methods {
    //  external library function signatures may only have 'storage' locations
    // function Array.areGreaterThanOrEqualTo(uint256[] memory arr, uint256 value) external returns (bool) envfree;
    // function Array.areLessThanOrEqualTo(uint256[] memory arr, uint256 value) external returns (bool) envfree;
    // Arrays are not allowed arguments of ghost functions in CVL
}

// Arrays are not allowed arguments of ghost functions in CVL
// ghost areGreaterThanOrEqualToGhost(uint256[], uint256) returns bool;


// TODO if this does not perform well, try specifying using individual array indices.
rule increase_executed_with_right_block_prices1 {
    env e;
    BaseOrderUtils.ExecuteOrderParams params;

    increaseOrderUtils.processOrder(e, params);

    require (params.order.numbers.orderType == Order.OrderType.MarketIncrease);
        
    assert array.areLessThanOrEqualTo(e,
            params.minOracleBlockNumbers, params.order.numbers.updatedAtBlock);
    assert array.areGreaterThanOrEqualTo(e,
            params.maxOracleBlockNumbers, params.order.numbers.updatedAtBlock);
}

rule increase_executed_with_right_block_prices2 {
    env e;
    BaseOrderUtils.ExecuteOrderParams params;

    increaseOrderUtils.processOrder(e, params);

    require (params.order.numbers.orderType == Order.OrderType.LimitIncrease);
    assert array.areGreaterThanOrEqualTo(e,
            params.minOracleBlockNumbers, params.order.numbers.updatedAtBlock);
}