using IncreaseOrderUtilsHarness as increaseOrderUtils;
using ArrayHarness as array;

methods {
    // Arrays are not allowed arguments of ghost functions in CVL
    
    //  external library function signatures may only have 'storage' locations
    // in summaries
    // function Array.areGreaterThanOrEqualTo(uint256[] memory arr, uint256 value) external returns (bool) envfree;
    // function Array.areLessThanOrEqualTo(uint256[] memory arr, uint256 value) external returns (bool) envfree;

    // Need to make library internal and then have external harness so it can
    // both be summarized but also called from the spec.

    function Array.areGreaterThanOrEqualTo(uint256[] memory arr, uint256 value) internal returns (bool) => areGreaterThanOrEqualToSummary(arr, value);
    function Array.areLessThanOrEqualTo(uint256[] memory arr, uint256 value) internal returns (bool) => areLessThanOrEqualToSummary(arr, value);
    // Try just munging these functions from array into the main contract ???

}

function areGreaterThanOrEqualToSummary(uint256[] arr, uint256 value) returns bool {
    // uninterpreted function
    bool ret;
    return ret;
}
function areLessThanOrEqualToSummary(uint256[] arr, uint256 value) returns bool {
    bool ret;
    return ret;
}

// TODO if this does not perform well, try specifying using individual array indices.

// Case 1: orderType == Order.OrderType.MarketIncrease
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

// Case 2: orderType == Order.OrderType.LimitIncrease
rule increase_executed_with_right_block_prices2 {
    env e;
    BaseOrderUtils.ExecuteOrderParams params;

    increaseOrderUtils.processOrder(e, params);

    require (params.order.numbers.orderType == Order.OrderType.LimitIncrease);
    assert array.areGreaterThanOrEqualTo(e,
            params.minOracleBlockNumbers, params.order.numbers.updatedAtBlock);
}

rule increase_blocks_case1variant2 {
    env e;
    BaseOrderUtils.ExecuteOrderParams params;

    increaseOrderUtils.processOrder(e, params);

    require (params.order.numbers.orderType == Order.OrderType.MarketIncrease);

    // all the minOracleBlockNumbers are less than the block number at which
    // the order was updated
    uint256 i;
    require i < params.minOracleBlockNumbers.length;
    assert params.minOracleBlockNumbers[i] <= params.order.numbers.updatedAtBlock;
    
    // all the maxOracleBlockNumbers are gte the block number at which
    // the order was updated
    // uint256 j;
    // require j < params.maxOracleBlockNumbers.length;
    // satisfy params.maxOracleBlockNumbers[j] >= params.order.numbers.updatedAtBlock;
}