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
}

rule sanity(method f) {
    env e;
    calldataarg args;
    f(e, args);
    assert false;
}


// StrictBank
// 1. syncTokenBalance should not change the tokenBalances[token'] where token' != token
// 2. _afterTransferOut should not change the tokenBalances[token'] where token' != token
// 3. should _recordTransferIn always be positive? (not sure)

// Bank
