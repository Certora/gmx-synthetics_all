/// SPDX-License-Identifier: Apache-2.0
pragma solidity 0.8.19;

import { Keys } from "../../contracts/data/Keys.sol";

contract KeysHarness {

    function FEE_RECEIVER() external pure returns (bytes32) { return Keys.FEE_RECEIVER; }
    function HOLDING_ADDRESS() external pure returns (bytes32) { return Keys.HOLDING_ADDRESS; }

    function claimableFeeAmountKey(address market, address token) external pure returns (bytes32) {
        bytes32 result = Keys.claimableFeeAmountKey(market, token);
        return result;
    }
}
