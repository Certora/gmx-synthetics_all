// SPDX-License-Identifier: BUSL-1.1

pragma solidity ^0.8.0;

import "../../contracts/order/IncreaseOrderUtils.sol";

contract IncreaseOrderUtilsHarness {
    function processOrder(BaseOrderUtils.ExecuteOrderParams memory params) external returns (EventUtils.EventLogData memory) {
        return IncreaseOrderUtils.processOrder(params);
    }

}