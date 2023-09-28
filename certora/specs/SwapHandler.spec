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

    function SwapPricingUtils.getPriceImpactUsd(SwapPricingUtils.GetPriceImpactUsdParams memory priceImpactParams) internal returns (int256) =>
        getPriceImpactUsdSummary(priceImpactParams);

    // MarketUtils
    function MarketUtils.applySwapImpactWithCap(address dataStore, 
        address eventEmitter, address market, address token,
        Price.Props memory tokenPrice, int256 priceImpactUsd) internal returns (int256)=> 
            applySwapImpactWithCapSummary(market, token, 
                tokenPrice, priceImpactUsd);
}

// This is used to treat getSwapFees as an opaque function
function getSwapFeesOpaque(address marketToken, uint256 amount,
    address uiFeeReceiver) returns SwapPricingUtils.SwapFees {
    SwapPricingUtils.SwapFees ret;
    return ret;
}

function getPriceImpactUsdSummary(SwapPricingUtils.GetPriceImpactUsdParams params) returns int256 {
    int256 ret;
    return ret;
}

function applySwapImpactWithCapSummary(address market, address token, 
    Price.Props tokenPrice, int256 priceImpactUsd) returns int256 {
    int256 ret;
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

    // Here this is just an opaque function.
    SwapPricingUtils.GetPriceImpactUsdParams priceImpactParams;
    int256 priceImpactedUsd = getPriceImpactUsdSummary(priceImpactParams);

    SwapPricingUtils.SwapFees fees = getSwapFeesOpaque(
        market.marketToken,
        swapParams.amountIn,
        swapParams.uiFeeReceiver
    );

    mathint finalAmountIn;

    // This definition of swapParams comes from the implementation of _swap
    if (priceImpactedUsd > 0) {
        finalAmountIn = fees.amountAfterFees;
    } else {
        int256 negativeImpactAmount = applySwapImpactWithCapSummary(
            market.marketToken, swapParams.tokenIn, tokenInPrice, 
            priceImpactedUsd);

        finalAmountIn = fees.amountAfterFees - require_uint256(-negativeImpactAmount);
    }

    require tokenOutPrice.max > 0;

    // added this as a separate var in case this gives more info
    // The following line is not actually the output. Instead of swapParams.
    // amountIn they use some function of that parameter and fees.
    // mathint expectedOutput = swapParams.amountIn * tokenInPrice.min / tokenOutPrice.max;
    mathint expectedOutput = finalAmountIn * tokenInPrice.min / tokenOutPrice.max;

    // In the implementation of SwapUtils._swap, the output amount uses tokenInPrice.min and tokenOutPrice.max
    assert outputAmount == require_uint256(expectedOutput);

}

rule marketSwapIntegritySatisfy() {
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

    mathint fee; // the fee calculation is something complicated.
    mathint expectedOutput = fee * tokenInPrice.min / tokenOutPrice.max;

    // In the implementation of SwapUtils._swap, the output amount uses tokenInPrice.min and tokenOutPrce.max
    satisfy outputAmount == require_uint256(expectedOutput);

}

rule sanity(method f) {
    env e;
    calldataarg args;
    f(e, args);
    assert false;
}