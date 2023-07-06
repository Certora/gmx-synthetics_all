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

    function tokenBalances(address) external returns (uint256) envfree;
}

use builtin rule sanity;
use builtin rule deepSanity;

// 1. syncTokenBalance, afterTransferOut, and recordTransferIn should not change tokenBalances[token1] where token1 != token2
rule balanceIndependence(method f, env e, address token1, address token2) filtered {
    f -> f.selector == sig:recordTransferIn(address).selector 
        || f.selector == sig:afterTransferOut(address).selector
        || f.selector == sig:syncTokenBalance(address).selector
} {
    uint256 balanceBefore = tokenBalances(token2);

    if (f.selector == sig:recordTransferIn(address).selector) {
        recordTransferIn(e, token1);
    } else if (f.selector == sig:afterTransferOut(address).selector) {
        afterTransferOut(e, token1);
    } else if (f.selector == sig:syncTokenBalance(address).selector) {
        syncTokenBalance(e, token1);
    }

    uint256 balanceAfter = tokenBalances(e, token2); 
    assert (token2 != token1 => balanceBefore == balanceAfter);
} 

// Bank
// 1. transferOut must increase the tokens for receiver by amount
// 2. something about native tokens but not sure I know why they are special
// 3. roles should be checked too