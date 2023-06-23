methods {
    //RoleStore
    function _.hasRole(address,bytes32) external => DISPATCHER(true);
}

rule sanity(method f) {
    env e;
    calldataarg args;
    f(e, args);
    assert false;
}