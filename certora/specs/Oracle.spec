methods {
    //RoleStore
    function _.hasRole(address,bytes32) external => DISPATCHER(true);
    function _.revokeRole(address,bytes32) external => DISPATCHER(true);
    function _.grantRole(address,bytes32) external => DISPATCHER(true);

    //DataStore
    function _.getUint(bytes32) external => DISPATCHER(true);
    function _.getBytes32(bytes32) external => DISPATCHER(true);
    function _.getAddress(bytes32) external => DISPATCHER(true);
    // function _.setAddress(bytes32,address) external => DISPATCHER(true);
    // function _.Uint(bytes32,uint256) external => DISPATCHER(true);
    // function _.setBool(bytes32,bool) external => DISPATCHER(true);

    //OracleStore
    function _.getSigner(uint256) external => DISPATCHER(true);
    // function _.addSigner(address) external => DISPATCHER(true);
    // function _.removeSigner(address) external => DISPATCHER(true);

    //MockPriceFeed
    function _.latestRoundData() external => DISPATCHER(true);
}

rule sanity(method f) {
    env e;
    calldataarg args;
    f(e, args);
    assert false;
}