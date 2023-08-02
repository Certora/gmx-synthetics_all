// using MockSwapUtils as MSU;
using DataStore as DS;
using KeysHarness as KH;
using DummyERC20A as DummyERC20In;

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
    function _.getPrimaryPrice(address) external => DISPATCHER(true);

    //RoleStore
    function _.hasRole(address,bytes32) external => DISPATCHER(true);
    function _.revokeRole(address,bytes32) external => DISPATCHER(true);
    function _.grantRole(address,bytes32) external => DISPATCHER(true);

}


// function applyDeltaToPoolAmount(
//         DataStore dataStore,
//         EventEmitter eventEmitter,
//         Market.Props market,
//         address token,
//         int256 delta) returns uint256 {
//     zp = require_uint256(z + dz);
//     tp = require_uint256(ONE18() - t);
//     yp = BondsOutSharesIn(z,y,dz,t,c,mu);
//     require YSInvariant(z, zp, y, yp, mu, c, tp);
//     return require_uint256(y - yp);
// }

// function applyDeltaToPoolAmount(
// ) internal returns (uint256) {
//     uint256 nextValue = dataStore.applyDeltaToUint(
//         Keys.poolAmountKey(market.marketToken, token),
//         delta,
//         "Invalid state, negative poolAmount"
//     );

//     applyDeltaToVirtualInventoryForSwaps(
//         dataStore,
//         eventEmitter,
//         market,
//         token,
//         delta
//     );

//     MarketEventUtils.emitPoolAmountUpdated(eventEmitter, market.marketToken, token, delta, nextValue);

//     return nextValue;
// }

rule sanity(method f) {
    env e;
    calldataarg args;
    f(e, args);
    assert false;
}

// require params.receiver != 
//      in:
//          address tokenIn;
//          mathint amountIn;
//          address receiver;
//          bool unwrapNative;
// out:
//          returns (received token address, amount received)
rule swapIntegrity(env e) {
    SwapUtils.SwapParams params;
    require params.amountIn == 1000;
    require params.shouldUnwrapNativeToken == false;
    require params.tokenIn == DummyERC20In;
    require params.swapPathMarkets.length == 0;

    address tokenOut;
    mathint amountReceived;

    tokenOut, amountReceived = swap(e, params);

    // balanceInBefore = params.bank.balanceOf(e.msg.sender)
    assert amountReceived >= to_mathint(params.minOutputAmount);
    // assert
}

rule swapIntegrityZeroMarkets(env e) {
    SwapUtils.SwapParams params;
    require params.amountIn == 1000;
    require params.shouldUnwrapNativeToken == false;
    require params.tokenIn == DummyERC20In;
    // require params.receiver != 
    //      in:
    // address tokenIn;
    // mathint amountIn;
    // address receiver;
    // bool unwrapNative;
    // returns (received token address, amount received)
    require params.swapPathMarkets.length == 0;
    address tokenOut;
    mathint amountReceived;
    tokenOut, amountReceived = swap(e, params);
    // balanceInBefore = params.bank.balanceOf(e.msg.sender)
    assert amountReceived >= to_mathint(params.minOutputAmount);
    // assert
}

rule swapIntegrityOneMarket(env e) {
    SwapUtils.SwapParams params;
    require params.amountIn == 1000;
    require params.shouldUnwrapNativeToken == false;
    require params.tokenIn == DummyERC20In;
    // require params.receiver != 
    //      in:
    // address tokenIn;
    // mathint amountIn;
    // address receiver;
    // bool unwrapNative;
    // returns (received token address, amount received)
    require params.swapPathMarkets.length == 1;
    address tokenOut;
    mathint amountReceived;
    tokenOut, amountReceived = swap(e, params);
    // balanceInBefore = params.bank.balanceOf(e.msg.sender)
    assert amountReceived >= to_mathint(params.minOutputAmount);
    // assert
}

rule swapIntegrityTwoMarkets(env e) {
    SwapUtils.SwapParams params;
    require params.amountIn == 1000;
    require params.shouldUnwrapNativeToken == false;
    require params.tokenIn == DummyERC20In;
    // require params.receiver != 
    //      in:
    // address tokenIn;
    // mathint amountIn;
    // address receiver;
    // bool unwrapNative;
    // returns (received token address, amount received)
    require params.swapPathMarkets.length == 2;
    address tokenOut;
    mathint amountReceived;
    tokenOut, amountReceived = swap(e, params);
    // balanceInBefore = params.bank.balanceOf(e.msg.sender)
    assert amountReceived >= to_mathint(params.minOutputAmount);
    // assert
}

rule swapIntegrityThreeMarkets(env e) {
    SwapUtils.SwapParams params;
    require params.amountIn == 1000;
    require params.shouldUnwrapNativeToken == false;
    require params.tokenIn == DummyERC20In;
    // require params.receiver != 
    //      in:
    // address tokenIn;
    // mathint amountIn;
    // address receiver;
    // bool unwrapNative;
    // returns (received token address, amount received)
    require params.swapPathMarkets.length == 3;
    address tokenOut;
    mathint amountReceived;
    tokenOut, amountReceived = swap(e, params);
    // balanceInBefore = params.bank.balanceOf(e.msg.sender)
    assert amountReceived >= to_mathint(params.minOutputAmount);
    // assert
}

// rule swapUtilsCheck(env e) {
//     MSU.swap(...) // TODO: check these functions
// }
