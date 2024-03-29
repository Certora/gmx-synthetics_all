// SPDX-License-Identifier: BUSL-1.1

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/utils/cryptography/ECDSA.sol";

import "../utils/Array.sol";
import "../utils/Bits.sol";
import "../price/Price.sol";
import "../utils/Printer.sol";

// @title OracleUtils
// @dev Library for oracle functions
library OracleUtils {
    using Array for uint256[];

    struct SetPricesParams {
        address[] tokens;
        address[] providers;
        bytes[] data;
    }

    struct ValidatedPrice {
        address token;
        uint256 min;
        uint256 max;
        uint256 timestamp;
        address provider;
    }

    struct SimulatePricesParams {
        address[] primaryTokens;
        Price.Props[] primaryPrices;
    }

    function isOracleError(bytes4 errorSelector) internal pure returns (bool) {
        if (isOracleBlockTimestampError(errorSelector)) {
            return true;
        }

        if (isEmptyPriceError(errorSelector)) {
            return true;
        }

        return false;
    }

    function isEmptyPriceError(bytes4 errorSelector) internal pure returns (bool) {
        if (errorSelector == Errors.EmptyPrimaryPrice.selector) {
            return true;
        }

        return false;
    }

    function isOracleBlockTimestampError(bytes4 errorSelector) internal pure returns (bool) {
        if (errorSelector == Errors.OracleTimestampsAreSmallerThanRequired.selector) {
            return true;
        }

        return false;
    }
}
