// SPDX-License-Identifier: BUSL-1.1

pragma solidity ^0.8.0;

import "../../contracts/role/Role.sol";

contract RoleHarness {
    function CONTROLLER() external pure returns (bytes32) {
        return Role.CONTROLLER;
    }
}
