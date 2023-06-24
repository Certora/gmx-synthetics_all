methods {
    //RoleStore
    function _.hasRole(address,bytes32) external => DISPATCHER(true);
    function _.revokeRole(address,bytes32) external => DISPATCHER(true);
    function _.grantRole(address,bytes32) external => DISPATCHER(true);

    //DataStore
    function _.setAddress(bytes32,address) external => DISPATCHER(true);
    function _.Uint(bytes32,uint256) external => DISPATCHER(true);

    //OracleStore
    function _.addSigner(address) external => DISPATCHER(true);
    function _.removeSigner(address) external => DISPATCHER(true);
}

rule sanity(method f) {
    env e;
    calldataarg args;
    f(e, args);
    assert false;
}