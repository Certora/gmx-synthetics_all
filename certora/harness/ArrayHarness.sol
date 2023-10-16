// SPDX-License-Identifier: BUSL-1.1

import "../../contracts/utils/Array.sol";

pragma solidity ^0.8.0;

contract ArrayHarness {
    function areGreaterThanOrEqualTo(uint256[] memory arr, uint256 value) external pure returns (bool) {
        return Array.areGreaterThanOrEqualTo(arr, value);
    }

    function areLessThanOrEqualTo(uint256[] memory arr, uint256 value) external pure returns (bool) {
        return Array.areLessThanOrEqualTo(arr, value);
    }
}