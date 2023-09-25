// SPDX-License-Identifier: BUSL-1.1

pragma solidity ^0.8.0;

import "../../contracts/position/Position.sol";
import "../../contracts/position/PositionUtils.sol";

library LiquidationHandlerHarness {

    function positionutils__getPositionKey(address account, address market, address collateralToken, bool isLong) public pure returns (bytes32) {
        return PositionUtils.getPositionKey(account, market, collateralToken, isLong);
    }

    function position__sizeInUsd(Position.Props memory props) public pure returns (uint256) {
        return props.numbers.sizeInUsd;
    }
    function position__collateralAmount(Position.Props memory props) public pure returns (uint256) {
        return props.numbers.collateralAmount;
    }



}