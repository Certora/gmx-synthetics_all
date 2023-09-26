
/**
 * Liquidation: allows liquidation of positions if the criteria for liquidation are met
 *
 * My interpretation:
 * a) if all criteria are met, the liquidation will go through.
 * b) if a liquidation goes through, all criteria were met.
 *
 * Basic structure for a: require the criteria, assert that liquidation works
 * Basic structure for b: require that liquidation works, assert the criteria
 */

//using DataStore as _DataStore;
//using Keys as _Keys;
using Position as _Position;
using LiquidationHandlerHarness as _LiquidationHandlerHarness;
//using PositionStoreUtils as _PositionStoreUtils;
//using PositionUtils as _PositionUtils;

methods {
    function executeLiquidation(
        address account,
        address market,
        address collateralToken,
        bool isLong,
        OracleUtils.SetPricesParams oracleParams
    ) external;

    // Summarize FeatureUtils.validateFeature()
    function _.validateFeature(address, bytes32) external => NONDET;
    function _.get(address, bytes32 key) external => NONDET;
}

rule liquidationWorksIfConditionsAreMet() {
    env e;
    address account;
    address market;
    address collateralToken;
    bool isLong;
    OracleUtils.SetPricesParams oracleParams;

    // take any position
    Position.Props position;

    // Model liquidation criteria as defined in https://gmx-io.notion.site/gmx-io/GMX-Technical-Overview-47fc5ed832e243afb9e97e8a4a036353
    // > A position can be liquidated by keepers if the losses of the position
    // > reduces the collateral to the point where position size / remaining
    // > collateral is more than the max allowed leverage.
    uint256 positionSize = _LiquidationHandlerHarness.position__sizeInUsd(e, position);
    uint256 collateralAmount = _LiquidationHandlerHarness.position__collateralAmount(e, position);
    uint256 minLeverageFactor; // = _DataStore.getUint(e, _Keys.minCollateralFactorKey(e, market));
    require(to_mathint(positionSize) > minLeverageFactor * collateralAmount);

    executeLiquidation@withrevert(e, account, market, collateralToken, isLong, oracleParams);

    bool didRevert = lastReverted;
    assert(!didRevert);
}


rule liquidationConditionsAreMetIfItWorks() {
    env e;
    address account;
    address market;
    address collateralToken;
    bool isLong;
    OracleUtils.SetPricesParams oracleParams;

    // take any position
    Position.Props position;

    executeLiquidation(e, account, market, collateralToken, isLong, oracleParams);

    // Model liquidation criteria as defined in https://gmx-io.notion.site/gmx-io/GMX-Technical-Overview-47fc5ed832e243afb9e97e8a4a036353
    // > A position can be liquidated by keepers if the losses of the position
    // > reduces the collateral to the point where position size / remaining
    // > collateral is more than the max allowed leverage.
    uint256 positionSize = _LiquidationHandlerHarness.position__sizeInUsd(e, position);
    uint256 collateralAmount = _LiquidationHandlerHarness.position__collateralAmount(e, position);
    uint256 minLeverageFactor; // = _DataStore.getUint(e, _Keys.minCollateralFactorKey(e, market));
    assert(to_mathint(positionSize) > minLeverageFactor * collateralAmount);
}
