/// SPDX-License-Identifier: Apache-2.0
pragma solidity 0.8.19;

import { Role } from "../../contracts/role/Role.sol";

contract RoleMock {

    function ROLE_ADMIN() external pure returns (bytes32) { return Role.ROLE_ADMIN; }

}
