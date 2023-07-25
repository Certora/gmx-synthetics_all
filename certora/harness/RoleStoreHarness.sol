/// SPDX-License-Identifier: Apache-2.0
pragma solidity 0.8.19;

import "../../contracts/role/RoleStore.sol";

contract RoleStoreHarness is RoleStore {
    constructor() RoleStore() {}

    function roleMembersAtRoleKeyContainsAccount(bytes32 roleKey, address account) external {
        return roleMembers[roleKey].contains(account);
    }
}
