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
<<<<<<< HEAD
      /*  if (value < 0) {
            console.log(label, "-", (-value).toUint256());
        } else {
            console.log(label, "+", value.toUint256());
        }*/
=======
        if (value < 0) {
            console.log(
                "%s -%s",
                label,
                (-value).toUint256()
            );
        } else {
            console.log(
                "%s +%s",
                label,
                value.toUint256()
            );
        }
>>>>>>> 3f17dd59b482e202b52652f8191581ca3827b18e
    }
}
