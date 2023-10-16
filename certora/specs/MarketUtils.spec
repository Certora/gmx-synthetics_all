using MarketUtilsHarness as marketUtils;
using PrecisionHarness as precision;

methods {
    function MarketUtils.getPoolValueInfoMunged(address dataStore_address, Market.Props market, Price.Props indexTokenPrice, Price.Props longTokenPrice, Price.Props shortTokenPrice, bytes32 pnlFactorType, bool maximize) external returns (int256)  => getPoolValueInfoUnrollGhost(dataStore_address, market.marketToken, market.indexToken, market.longToken, market.shortToken);
    function PrecisionHarness.mulDiv(uint256 value, int256 numerator, uint256 denominator) external returns (int256) envfree;
    function Precision.mulDiv(uint256 value, int256 numerator, uint256 denominator) internal returns (int256) => mulDivOpaque(value, numerator, denominator);
}

// This is not allowed because it needs to operate on Structs...
// It would be easier to do modular verification if we could support structs
// ghost getPoolValueInfoGhost(address,
//         Market.Props,
//         Price.Props,
//         Price.Props,
//         Price.Props,
//         bytes32,
//         bool) returns MarketPoolValueInfo.Props;

// Also not allowed :( -- return function can't be that struct
// ghost getPoolValueInfoUnrollGhost(
//     address, // datastore address
//     address, // market.marketToken
//     address, // market.longToken
//     address // market.shortToken
// ) returns MarketPoolValueInfo.Props;

ghost getPoolValueInfoUnrollGhost(
    address, // datastore address
    address, // market.marketToken
    address, // market.indexToken
    address, // market.longToken
    address // market.shortToken
) returns int256;
// limitation may actually be that params/returns cannot be a combination of structs/arrays. Example in hristo branch / order handler.

// start out by summarizing as uninterpreted to see if this is actually
// the issue, then try adding a def to improve the rule.
function mulDivOpaque(uint256 value, int256 numerator, uint256 denominator) returns int256 {
    int256 result;
    return result;
}

rule market_pricing_correct_satisfy {
    env e;
    address dataStore;
    Market.Props market;
    Price.Props indexTokenPrice;
    Price.Props longTokenPrice;
    Price.Props shortTokenPrice;
    bytes32 pnlFactorType;
    bool maximize;

    int256 tokenPrice;
    MarketPoolValueInfo.Props marketPoolProps;
    tokenPrice, marketPoolProps = marketUtils.getMarketTokenPrice(e, dataStore, market, indexTokenPrice, longTokenPrice, shortTokenPrice, pnlFactorType, maximize);

    uint256 marketTokenSupply = marketUtils.marketTokenTotalSupply(e, market.marketToken);

    int256 poolValueInfo;
    // TODO: plan is to try to specify getPoolValueInfo
    // as a totally opaque (ghost) function and try to get the proof
    // to go through in terms of the opaque function.

    satisfy tokenPrice == require_int256(poolValueInfo / marketTokenSupply);
}

rule market_pricing_correct {
    env e;
    address dataStore;
    Market.Props market;
    Price.Props indexTokenPrice;
    Price.Props longTokenPrice;
    Price.Props shortTokenPrice;
    bytes32 pnlFactorType;
    bool maximize;

    uint256 WEI_PRECISION = 1000000000000000000;

    int256 tokenPrice = marketUtils.getMarketTokenPriceMunged(e, dataStore, market, indexTokenPrice, longTokenPrice, shortTokenPrice, pnlFactorType, maximize);

    uint256 marketTokenSupply = marketUtils.marketTokenTotalSupply(e, market.marketToken);

    int256 poolValueInfo = getPoolValueInfoUnrollGhost(
        dataStore, market.marketToken, market.indexToken, market.longToken, market.shortToken);

    assert tokenPrice == precision.mulDiv(WEI_PRECISION, poolValueInfo, marketTokenSupply);
}