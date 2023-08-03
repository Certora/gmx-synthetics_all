// SPDX-License-Identifier: BUSL-1.1
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

import "../../contracts/deposit/DepositUtils.sol";
import "../../contracts/data/DataStore.sol";
import "../../contracts/data/Keys.sol";

import "../../contracts/event/EventEmitter.sol";

import "../../contracts/deposit/DepositVault.sol";
import "../../contracts/deposit/DepositStoreUtils.sol";
import "../../contracts/deposit/DepositEventUtils.sol";

import "../../contracts/nonce/NonceUtils.sol";

import "../../contracts/gas/GasUtils.sol";
import "../../contracts/callback/CallbackUtils.sol";
import "../../contracts/utils/AccountUtils.sol";

contract DepositUtilsHarness {

    struct CreateDepositParams {
        address receiver;
        address callbackContract;
        address uiFeeReceiver;
        address market;
        address initialLongToken;
        address initialShortToken;
        address[] longTokenSwapPath;
        address[] shortTokenSwapPath;
        uint256 minMarketTokens;
        bool shouldUnwrapNativeToken;
        uint256 executionFee;
        uint256 callbackGasLimit;
    }

    struct Flags {
        bool shouldUnwrapNativeToken;
    }

    struct Props {
        Addresses addresses;
        Numbers numbers;
        Flags flags;
    }

       struct Addresses {
        address account;
        address receiver;
        address callbackContract;
        address uiFeeReceiver;
        address market;
        address initialLongToken;
        address initialShortToken;
        address[] longTokenSwapPath;
        address[] shortTokenSwapPath;
    }

    struct Numbers {
        uint256 initialLongTokenAmount;
        uint256 initialShortTokenAmount;
        uint256 minMarketTokens;
        uint256 updatedAtBlock;
        uint256 executionFee;
        uint256 callbackGasLimit;
    }

    function createDepositFn(
        DataStore dataStore,
        EventEmitter eventEmitter,
        DepositVault depositVault,
        address account,
        DepositUtils.CreateDepositParams memory params
    ) external returns (bytes32) {
        return DepositUtils.createDeposit(dataStore, eventEmitter, depositVault, account, params);
    }

    function cancelDepositFn(
        DataStore dataStore,
        EventEmitter eventEmitter,
        DepositVault depositVault,
        bytes32 key,
        address keeper,
        uint256 startingGas,
        string memory reason,
        bytes memory reasonBytes
    ) external {
        DepositUtils.cancelDeposit( dataStore, eventEmitter, depositVault, key, keeper, startingGas, reason, reasonBytes);
    }

    function getMaxSwapPathLength(DataStore dataStore) external view returns (uint256) {
        return dataStore.getUint(Keys.MAX_SWAP_PATH_LENGTH);
    }


}
