using Oracle as oracle;
using MarketUtils as MarketUtils;
methods {
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

    //Datastore
    function _.setBool(bytes32,bool) external => DISPATCHER(true);
    function _.getUint(bytes32) external => DISPATCHER(true);
    function _.getAddress(bytes32) external => DISPATCHER(true);
    function _.getBool(bytes32) external => DISPATCHER(true);
    function _.getBytes32(bytes32) external => DISPATCHER(true);
    function _.incrementUint(bytes32 key, uint256 value) external => DISPATCHER(true);
    function _.applyBoundedDeltaToUint(bytes32 key, int256 value) external => DISPATCHER(true);
    function _.applyDeltaToUint(bytes32 key, uint256 value) external => DISPATCHER(true);
    function _.applyDeltaToUint(bytes32 key, int256 value) external => DISPATCHER(true);
    function _.applyDeltaToUint(bytes32, int256, string) external => DISPATCHER(true);


    //Oracle
    function _.getPrimaryPrice(address) external => DISPATCHER(true);

    //RoleStore
    function _.hasRole(address,bytes32) external => DISPATCHER(true);
    function _.revokeRole(address,bytes32) external => DISPATCHER(true);
    function _.grantRole(address,bytes32) external => DISPATCHER(true);

    function _.applyFactor(uint256, uint256) external => DISPATCHER(true);

    // SwapPricingUtils
    function SwapPricingUtils.getSwapFees(address dataStore, address marketToken, uint256 amount, address uiFeeReceiver) internal returns (SwapPricingUtils.SwapFees memory) =>
        getSwapFeesOpaque(marketToken, amount, uiFeeReceiver);

}

// This is used to treat getSwapFees as an opaque function
function getSwapFeesOpaque(address marketToken, uint256 amount,
    address uiFeeReceiver) returns SwapPricingUtils.SwapFees {
    
    SwapPricingUtils.SwapFees ret;
    return ret;
}

//-----------------------------------------------------------------------------
// Integrity: Trading
//-----------------------------------------------------------------------------

// MarketSwap: swap token A to token B at the current market price if the order 
// was created at block n, it should be executed with the oracle prices at 
// block n The swap output amount, before fees and price impact, (amount of tokens in) * (token in price) / (token out price).

// MarketSwap orders are created and placed in OrderHandler
// OrderHandler eventually calls OrderUtils.processOrder as part of the
// implementation of executeOrder. This in turn calls 
// SwapOrderUtils.processOrder which calls SwapUtils.swap. SwapHandler.swap
// is just an alias of SwapUtils.swap with guards.

rule marketSwapIntegrity() {
    env e;
    
    // TODO set this up in the same way that OrderHandler does, potentially:
    // bytes32 key;
    // OracleUtils.SetPricesParams oracleParams;
    // use  Order.OrderType.MarketSwap to check for right order type
    
    address outputToken;
    uint256 outputAmount;
    SwapUtils.SwapParams swapParams;

    outputToken, outputAmount = swap(e, swapParams);

    // These are how the prices are defined in SwapUtils._swap :
    Price.Props tokenInPrice = oracle.getPrimaryPrice(e, swapParams.tokenIn);
    Price.Props tokenOutPrice = oracle.getPrimaryPrice(e, outputToken);

    // swap has an array of markets, and iterates through them calling _swap
    require swapParams.swapPathMarkets.length == 1;
    Market.Props market = swapParams.swapPathMarkets[0];

    // swap

    // NOTE: This is WIP 

    // fees is defined by SwapPricingUtils.getSwapFees
    // feeFactor can't acually be munged into a constant because it is really computed on-the-fly ... can't seem to call keccak256 here safely either...
    // bytes32 SWAP_FEE_FACTOR = 
    //     0x0820000000000000000000000000000000000000000000000000000000000000;

    // NOTE TO SELF: just summarize the "bigger" functions rather than zooming
    // into the details so much.
    
    SwapPricingUtils.SwapFees fees = getSwapFeesOpaque(
        market.marketToken,
        swapParams.amountIn,
        swapParams.uiFeeReceiver
    );


    uint256 finalAmountIn;

    // NOTE: via munging priceImpactedUsd == 1

    // This definition of swapParams comes from the implementation of _swap
    // if (priceImpactedUsd > 0) {
    finalAmountIn = fees.amountAfterFees;
    // } else {
    //     // This is defined by a call to applySwapImpactWithCap in SwapUtils._swap 
    //     int256 negativeImpactAmount; // TODO define this
    //     int256 impactOne = priceImpactUsd / tokenInPrice.max
    //     int256 maxImpactAmount = getSwapImpactPoolAmount(dataStore, market, tokenIn);

    //     finalAmountIn = fees_amountAfterFees - (-negativeImpactAmount).toUint256();
    // }

    require tokenOutPrice.max > 0;

    // added this as a separate var in case this gives more info
    // The following line is not actually the output. Instead of swapParams.
    // amountIn they use some function of that parameter and fees.
    // mathint expectedOutput = swapParams.amountIn * tokenInPrice.min / tokenOutPrice.max;
    mathint expectedOutput = finalAmountIn * tokenInPrice.min / tokenOutPrice.max;

    // In the implementation of SwapUtils._swap, the output amount uses tokenInPrice.min and tokenOutPrice.max
    assert outputAmount == require_uint256(expectedOutput);

}

rule sanity(method f) {
    env e;
    calldataarg args;
    f(e, args);
    assert false;
}