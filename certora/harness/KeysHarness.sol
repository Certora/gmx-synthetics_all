// SPDX-License-Identifier: BUSL-1.1

pragma solidity ^0.8.0;

import "../../contracts/data/Keys.sol";

contract KeysHarness {
    function DEPOSIT_LIST() external pure returns (bytes32) {
        return Keys.DEPOSIT_LIST;
    }

    function WNT() external pure returns (bytes32) {
        return Keys.WNT;
    }

    function MAX_PNL_FACTOR_FOR_TRADERS() external pure returns (bytes32) {
        return Keys.MAX_PNL_FACTOR_FOR_TRADERS;
    }
}
