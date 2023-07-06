// import "../openzeppelin/specs/EnumerableSet.spec";

methods {
    // RoleStore.sol
    function _.hasRole(address, bytes32) external => DISPATCHER(true);
}

use builtin rule sanity;
use builtin rule deepSanity;