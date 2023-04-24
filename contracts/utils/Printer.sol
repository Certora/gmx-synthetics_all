// SPDX-License-Identifier: BUSL-1.1

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/math/SafeCast.sol";
//import "hardhat/console.sol";

/**
 * @title Printer
 * @dev Library for console functions
 */
library Printer {
    using SafeCast for int256;

    function log(string memory label, int256 value) internal view {
      /*  if (value < 0) {
            console.log(label, "-", (-value).toUint256());
        } else {
            console.log(label, "+", value.toUint256());
        }*/
    }
}
