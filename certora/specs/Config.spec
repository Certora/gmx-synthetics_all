methods {
    //EventEmitter
    // function EventEmitter._ external => NONDET;
    // function EventUtils._ external => NONDET;
    // function EventUtils.initItems(EventUtils.AddressItems, uint256) internal => NONDET;
    // function EventUtils.setItem(EventUtils.AddressItems, uint256, string, address) internal  => NONDET;

    //RoleStore
    function _.hasRole(address,bytes32) external => DISPATCHER(true);
}

rule sanity(method f) {
    env e;
    calldataarg args;
    f(e, args);
    assert false;
}