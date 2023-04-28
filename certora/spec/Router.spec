methods {
    // RoleStore.sol
    function _.hasRole(address, bytes32) external => DISPATCHER(true);

    function _.transferFrom(address,address,uint256) external => DISPATCHER(true);
}

rule complexity_check {
    method f; env e; calldataarg args;

    f(e, args);

    assert false, "this assertion should fail";
}