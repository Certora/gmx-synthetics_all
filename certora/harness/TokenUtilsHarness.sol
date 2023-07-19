// SPDX-License-Identifier: BUSL-1.1
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

import "../../contracts/token/TokenUtils.sol";
import "../../contracts/data/DataStore.sol";
import "../../contracts/data/Keys.sol";

contract TokenUtilsHarness {

    function wntFn(DataStore dataStore) public view returns (address) {
        return TokenUtils.wnt(dataStore);
    }

    function transferFn(
        DataStore dataStore,
        address token,
        address receiver,
        uint256 amount
    ) public {
        TokenUtils.transfer(dataStore, token, receiver, amount);
    }

    function depositAndSendWrappedNativeTokenFn(
        DataStore dataStore,
        address receiver,
        uint256 amount
    ) public {
        TokenUtils.depositAndSendWrappedNativeToken(dataStore, receiver, amount);
    }

    function withdrawAndSendNativeTokenFn(
        DataStore dataStore,
        address _wnt,
        address receiver,
        uint256 amount
    ) public {
        TokenUtils.withdrawAndSendNativeToken(dataStore, _wnt, receiver, amount);
    }

    function nonRevertingTransferWithGasLimitFn(
        IERC20 token,
        address to,
        uint256 amount,
        uint256 gasLimit
    ) public returns (bool, bytes memory) {
        return TokenUtils.nonRevertingTransferWithGasLimit(token, to, amount, gasLimit);
    }

    function getHoldingAddress(DataStore dataStore) public view returns (address) {
        return dataStore.getAddress(Keys.HOLDING_ADDRESS);
    }
}
