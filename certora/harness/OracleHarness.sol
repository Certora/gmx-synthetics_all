// SPDX-License-Identifier: BUSL-1.1
pragma solidity ^0.8.0;

import {Oracle, DataStore, EventEmitter, RoleStore, OracleStore} from "../../contracts/Oracle/Oracle.sol";
import {OracleUtils} from "../../contracts/Oracle/OracleUtils.sol";

contract OracleHarness is Oracle {

    DataStore public immutable myDataStore;
    EventEmitter public immutable myEventEmitter;
    constructor(
        RoleStore _roleStore,
        OracleStore _oracleStore,
        DataStore _dataStore,
        EventEmitter _eventEmitter
    ) Oracle(_roleStore, _oracleStore) {
        myDataStore = _dataStore;
        myEventEmitter = _eventEmitter;
    }

    function setPrices(
        DataStore,
        EventEmitter,
        OracleUtils.SetPricesParams memory params
    ) public override {
        super.setPrices(myDataStore, myEventEmitter, params);
    }
}