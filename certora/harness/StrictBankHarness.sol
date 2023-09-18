// SPDX-License-Identifier: BUSL-1.1

pragma solidity ^0.8.0;

import "../../contracts/bank/StrictBank.sol";

contract StrictBankHarness is StrictBank {
    constructor(RoleStore _roleStore, DataStore _dataStore) StrictBank(_roleStore, _dataStore) {}
    function _afterTransferOutHarness(address token) public {
        _afterTransferOut(token);
    }
    function _recordTransferInHarness(address token) public returns (uint256) {
        return _recordTransferIn(token);
    }
}