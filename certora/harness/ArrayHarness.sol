// SPDX-License-Identifier: BUSL-1.1

pragma solidity ^0.8.0;

contract ArrayHarness {
    function areGreaterThanOrEqualTo(uint256[] memory arr, uint256 value) external pure returns (bool) {
        for (uint256 i; i < arr.length; i++) {
            if (arr[i] < value) {
                return false;
            }
        }

        return true;
    }

    function areLessThanOrEqualTo(uint256[] memory arr, uint256 value) external pure returns (bool) {
        for (uint256 i; i < arr.length; i++) {
            if (arr[i] > value) {
                return false;
            }
        }

        return true;
    }
}