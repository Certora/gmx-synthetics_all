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

    function getMarketTokenPrice(
        address dataStore_addr,
        Market.Props memory market,
        Price.Props memory indexTokenPrice,
        Price.Props memory longTokenPrice,
        Price.Props memory shortTokenPrice,
        bytes32 pnlFactorType,
        bool maximize
    ) external view returns (int256, MarketPoolValueInfo.Props memory) {
        DataStore dataStore = DataStore(dataStore_addr);
        return MarketUtils.getMarketTokenPrice(dataStore, market, indexTokenPrice, longTokenPrice, shortTokenPrice, pnlFactorType, maximize);
    }

    function getMarketTokenPriceMunged(
        address dataStore_addr,
        Market.Props memory market,
        Price.Props memory indexTokenPrice,
        Price.Props memory longTokenPrice,
        Price.Props memory shortTokenPrice,
        bytes32 pnlFactorType,
        bool maximize
    ) external view returns (int256) {
        DataStore dataStore = DataStore(dataStore_addr);
        return MarketUtils.getMarketTokenPriceMunged(dataStore, market, indexTokenPrice, longTokenPrice, shortTokenPrice, pnlFactorType, maximize);
    }

    function marketTokenTotalSupply(address marketTokenAddr) external view returns (uint256) {
        MarketToken marketToken = MarketToken(payable(marketTokenAddr));
        return marketToken.totalSupply();
    }

}