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

// Case 1: orderType == Order.OrderType.MarketIncrease
rule increase_executed_with_right_block_prices1 {
    env e;
    BaseOrderUtils.ExecuteOrderParams params;

    increaseOrderUtils.processOrder(e, params);

    require (params.order.numbers.orderType == Order.OrderType.MarketIncrease);
        
    satisfy array.areLessThanOrEqualTo(e,
            params.minOracleBlockNumbers, params.order.numbers.updatedAtBlock);
    satisfy array.areGreaterThanOrEqualTo(e,
            params.maxOracleBlockNumbers, params.order.numbers.updatedAtBlock);
}

// Case 2: orderType == Order.OrderType.LimitIncrease
rule increase_executed_with_right_block_prices2 {
    env e;
    BaseOrderUtils.ExecuteOrderParams params;

    increaseOrderUtils.processOrder(e, params);

    require (params.order.numbers.orderType == Order.OrderType.LimitIncrease);
    satisfy array.areGreaterThanOrEqualTo(e,
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
    satisfy params.minOracleBlockNumbers[i] <= params.order.numbers.updatedAtBlock;
    
    // all the maxOracleBlockNumbers are gte the block number at which
    // the order was updated
    // uint256 j;
    // require j < params.maxOracleBlockNumbers.length;
    // satisfy params.maxOracleBlockNumbers[j] >= params.order.numbers.updatedAtBlock;
}