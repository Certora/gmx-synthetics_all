// SPDX-License-Identifier: BUSL-1.1

import "../../contracts/utils/Precision.sol";

pragma solidity ^0.8.0;

library PrecisionHarness {
    
    function mulDiv(uint256 value, int256 numerator, uint256 denominator) external pure returns (int256) {
        return Precision.mulDiv(value, numerator, denominator);
    }
}