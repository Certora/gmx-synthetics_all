// using MockSwapUtils as MSU;
using Market as M;
using EventEmitter as EE;
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
    function _.hasRole(address,bytes32) external => NONDET;
    function _.revokeRole(address,bytes32) external => NONDET;
    function _.grantRole(address,bytes32) external => NONDET;
    function _.getRoleCount() external => NONDET;

    //MarketUtils
    // function _.applyDeltaToPoolAmount(address, address, Market.Props, address, int256) external => DISPATCHER(true);
    // function _.applyDeltaToPoolAmount(address, address, Market.Props, address, int256) external => NONDET;
    // function _.applySwapImpactWithCap(address, address, address, address, Price.Props memory, int256) internal => NONDET;
    //PricingUtils
    // function _.applyImpactFactor(uint256, uint256, uint256) external => NONDET;
    //SwapPritingUtils
    function _.getPriceImpactUsd(SwapPricingUtils.GetPriceImpactUsdParams memory) internal => NONDET;
    // function _.getSwapFees(address, address, uint256, address) internal => NONDET;
    //FeeUtils
    // function _.incrementClaimableFeeAmount(address, address, address, address, address, uint256, bytes32) external => NONDET;

    // function incrementClaimableFeeAmount(
    //     address dataStore, address eventEmitter, address market, address token, uint256 delta, bytes32 feeType
    // ) external => setClaimableFees(delta);
    // EventEmitter
    // function EventEmitter._ external => NONDET;

}

// ghost uint256 claimableFees;

// function setClaimableFees(uint256 x) {
//     claimableFees = claimableFees + x;
// }

// ghost bool hasRoleGhost;
// function (address)





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


// Verified here:
// https://prover.certora.com/output/40577/78edc6a11f71416dac589acb947806ba/?anonymousKey=714823af94cf93f37fa604eabd27c1921c65263a
// With this NONDET:
// hasRole, revokeRole, grantRole, getRoleCount,
// applyDeltaToPoolAmount, applySwapImpactWithCap, applyImpactFactor, getPriceImpactUsd, getSwapFees, incrementClaimableFeeAmount
rule swapPayedByBankZeroMarkets(env e) {
    SwapUtils.SwapParams params;
    require params.amountIn == 1000;
    require params.shouldUnwrapNativeToken == false;
    require params.tokenIn == DummyERC20In;

    require params.swapPathMarkets.length == 0;

    address tokenOut;
    mathint amountReceived;

    mathint balanceBankBefore = DummyERC20In.balanceOf(e, params.bank);
    mathint balanceReceiverBefore = DummyERC20In.balanceOf(e, params.receiver);

    tokenOut, amountReceived = swap(e, params);

    mathint balanceBankAfter = DummyERC20In.balanceOf(e, params.bank);
    mathint balanceReceiverAfter = DummyERC20In.balanceOf(e, params.receiver);

    require balanceBankBefore + balanceReceiverBefore + balanceBankAfter + balanceReceiverAfter < max_uint256; 

    assert tokenOut == params.tokenIn;
    assert amountReceived >= to_mathint(params.minOutputAmount);
    assert params.receiver != params.bank => balanceBankBefore == balanceBankAfter + params.amountIn;
    assert params.receiver != params.bank => balanceReceiverAfter == balanceReceiverBefore + params.amountIn;
}

// Verified here:
// https://prover.certora.com/output/40577/20d981338f3841eaa73489a1401f1315/?anonymousKey=ab2a729aa9c406af03f97820e765e8549c830bd7
// With Role NONDET:
// hasRole, revokeRole, grantRole, getRoleCount and
// With NONDET:
// getPriceImpactUsd
rule swapPayedByBankOneMarket(env e) {
    SwapUtils.SwapParams params;
    require params.amountIn == 1000;
    require params.shouldUnwrapNativeToken == false;
    require params.tokenIn == DummyERC20In;

    require params.swapPathMarkets.length == 0;

    address tokenOut;
    mathint amountReceived;

    mathint balanceBankBefore = DummyERC20In.balanceOf(e, params.bank);
    mathint balanceReceiverBefore = DummyERC20In.balanceOf(e, params.receiver);

    tokenOut, amountReceived = swap(e, params);

    mathint balanceBankAfter = DummyERC20In.balanceOf(e, params.bank);
    mathint balanceReceiverAfter = DummyERC20In.balanceOf(e, params.receiver);

    require balanceBankBefore + balanceReceiverBefore + balanceBankAfter + balanceReceiverAfter < max_uint256; 

    assert tokenOut == params.tokenIn;
    assert amountReceived >= to_mathint(params.minOutputAmount);
    assert params.receiver != params.bank => balanceBankBefore == balanceBankAfter + params.amountIn;
    assert params.receiver != params.bank => balanceReceiverAfter == balanceReceiverBefore + params.amountIn;
}

rule swapPayedByBankMultipleMarkets(env e) {
    SwapUtils.SwapParams params;
    require params.amountIn == 1000;
    require params.shouldUnwrapNativeToken == false;
    require params.tokenIn == DummyERC20In;

    address tokenOut;
    mathint amountReceived;

    mathint balanceBankBefore = DummyERC20In.balanceOf(e, params.bank);
    mathint balanceReceiverBefore = DummyERC20In.balanceOf(e, params.receiver);

    tokenOut, amountReceived = swap(e, params);

    mathint balanceBankAfter = DummyERC20In.balanceOf(e, params.bank);
    mathint balanceReceiverAfter = DummyERC20In.balanceOf(e, params.receiver);

    require balanceBankBefore + balanceReceiverBefore + balanceBankAfter + balanceReceiverAfter < max_uint256; 

    assert amountReceived >= to_mathint(params.minOutputAmount);
    // assert params.receiver != params.bank => balanceBankBefore == balanceBankAfter + params.amountIn;
    assert params.receiver != params.bank => balanceReceiverAfter == balanceReceiverBefore + amountReceived;
}
