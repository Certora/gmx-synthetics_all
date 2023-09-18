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

    //Oracle
    // function _.getPrimaryPrice(address) external => DISPATCHER(true);

    //RoleStore
    function _.hasRole(address,bytes32) external => DISPATCHER(true);
    function _.revokeRole(address,bytes32) external => DISPATCHER(true);
    function _.grantRole(address,bytes32) external => DISPATCHER(true);

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

    Price.Props tokenInPrice = swapParams.oracle.getPrimaryPrice(e, swapParams.tokenIn);
    Price.Props tokenOutPrice = swapParams.oracle.getPrimaryPrice(e, outputToken);

    assert outputAmount == swapParams.amountIn * tokenInPrice / tokenOutPrice;

}

rule sanity(method f) {
    env e;
    calldataarg args;
    f(e, args);
    assert false;
}