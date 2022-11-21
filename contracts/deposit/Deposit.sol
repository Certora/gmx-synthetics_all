// SPDX-License-Identifier: BUSL-1.1

pragma solidity ^0.8.0;

library Deposit {
    struct Props {
        address account;
        address receiver;
        address callbackContract;
        address market;
        uint256 longTokenAmount;
        uint256 shortTokenAmount;
        uint256 minMarketTokens;
        uint256 updatedAtBlock;
        bool shouldUnwrapNativeToken;
        uint256 executionFee;
        uint256 callbackGasLimit;
        bytes data;
    }
}
