using SwapOrderUtilsHarness as swapOrderUtils;
using ArrayHarness as Array;

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

    swapOrderUtils.processOrder(e, params);

    require (params.order.numbers.orderType == Order.OrderType.MarketSwap);
        
    assert Array.areLessThanOrEqualTo(e,
            params.minOracleBlockNumbers, params.order.numbers.updatedAtBlock);
    assert Array.areGreaterThanOrEqualTo(e,
            params.maxOracleBlockNumbers, params.order.numbers.updatedAtBlock);
}

rule decrease_executed_with_right_block_prices2 {
    env e;
    BaseOrderUtils.ExecuteOrderParams params;

    swapOrderUtils.processOrder(e, params);

    require params.order.numbers.orderType == Order.OrderType.LimitSwap;
    assert Array.areGreaterThanOrEqualTo(e,
            params.minOracleBlockNumbers, params.order.numbers.updatedAtBlock);
}