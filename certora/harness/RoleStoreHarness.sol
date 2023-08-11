/// SPDX-License-Identifier: Apache-2.0
pragma solidity 0.8.19;

import "../../contracts/role/RoleStore.sol";
import { Role } from "../../contracts/role/Role.sol";

contract RoleStoreHarness is RoleStore {
    constructor() RoleStore() {}

    function castToBytes32(address val) external pure returns (bytes32 b) {
        b = bytes32(uint256(uint160(val)));
    }

    function ROLE_ADMIN() external pure returns (bytes32) { return Role.ROLE_ADMIN; }
}
