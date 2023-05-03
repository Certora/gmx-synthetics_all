import "erc20.spec";

methods {
    // DataStore.sol
    function _.getAddress(bytes32) external => DISPATCHER(true);
    function _.getUint(bytes32) external => DISPATCHER(true);
    // RoleStore.sol
    function _.hasRole(address, bytes32) external => DISPATCHER(true);
    // IWNT.sol
    function _.withdraw(uint256) external => DISPATCHER(true);
    function _.deposit() external => DISPATCHER(true);
    // Receiver.sol
    function _.sendTo() external => DISPATCHER(true);
    function _.sendToDoubleReturn() external => DISPATCHER(true);
}

rule complexity_check {
    method f; env e; calldataarg args;

    f(e, args);

    assert false, "this assertion should fail";
}