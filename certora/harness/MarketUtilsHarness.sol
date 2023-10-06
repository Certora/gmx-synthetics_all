// SPDX-License-Identifier: BUSL-1.1

pragma solidity ^0.8.0;

import "../../contracts/market/MarketUtils.sol";

contract MarketUtilsHarness {
        
    function getPoolValueInfo(
        address dataStore,
        Market.Props memory market,
        Price.Props memory indexTokenPrice,
        Price.Props memory longTokenPrice,
        Price.Props memory shortTokenPrice,
        bytes32 pnlFactorType,
        bool maximize
    ) public view returns (MarketPoolValueInfo.Props memory) {
        return MarketUtils.getPoolValueInfo(dataStore, market, indexTokenPrice, longTokenPrice, shortTokenPrice, pnlFactorType, maximize);
    }


}