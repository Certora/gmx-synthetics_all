
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

using DataStore as _DataStore;
using Keys as _Keys;
using Position as _Position;
using LiquidationHandlerHarness as _LiquidationHandlerHarness;

function array_identity(uint256[] a) returns uint256[] {
    return a;
}

methods {
    function executeLiquidation(address, address, address, bool, OracleUtils.SetPricesParams) external;

    // ##### Top-Down #####

    function _.validateFeature(address, bytes32) external => NONDET;
    function _.executeOrder(address) external => NONDET;
    function OracleUtils.getUncompactedOracleBlockNumbers(uint256[] memory a, uint256 length) internal returns (uint256[] memory)=> array_identity(a);

    // ##### Bottom-Up #####

    // emit functions from MarketEventUtils
    function _.emitMarketPoolValueInfo(address, address, MarketPoolValueInfo.Props, uint256) external => NONDET;
    function _.emitPoolAmountUpdated(address, address, address, int256, uint256) external => NONDET;
    function _.emitSwapImpactPoolAmountUpdated(address, address, address, int256, uint256) external => NONDET;
    function _.emitPositionImpactPoolAmountUpdated(address, address, int256, uint256) external => NONDET;
    function _.emitOpenInterestUpdated(address, address, address, bool, int256, uint256) external => NONDET;
    function _.emitOpenInterestInTokensUpdated(address, address, address, bool, int256, uint256) external => NONDET;
    function _.emitVirtualSwapInventoryUpdated(address, address, bool, bytes32, int256, uint256) external => NONDET;
    function _.emitVirtualPositionInventoryUpdated(address, address, bytes32, int256, int256) external => NONDET;
    function _.emitCollateralSumUpdated(address, address, address, bool, int256, uint256) external => NONDET;
    function _.emitBorrowingFactorUpdated(address, address, bool, uint256, uint256) external => NONDET;
    function _.emitFundingFeeAmountPerSizeUpdated(address, address, address, bool, uint256, uint256) external => NONDET;
    function _.emitClaimableFundingAmountPerSizeUpdated(address, address, address, bool, uint256, uint256) external => NONDET;
    function _.emitClaimableFundingUpdated(address, address, address, address, uint256, uint256, uint256) external => NONDET;
    function _.emitFundingFeesClaimed(address, address, address, address, address, uint256, uint256) external => NONDET;
    function _.emitClaimableFundingUpdated(address, address, address, uint256, address, uint256, uint256) external => NONDET;
    function _.emitClaimableCollateralUpdated(address, address, address, uint256, address, uint256, uint256, uint256) external => NONDET;
    function _.emitCollateralClaimed(address, address, address, uint256, address, address, uint256, uint256) external => NONDET;
    function _.emitUiFeeFactorUpdated(address, address, uint256) external => NONDET;

    // emit functions from OrderEventUtils
    function _.emitOrderCreated(address, bytes32, Order.Props) external => NONDET;
    function _.emitOrderExecuted(address, bytes32) external => NONDET;
    function _.emitOrderUpdated(address, bytes32, uint256, uint256, uint256, uint256) external => NONDET;
    function _.emitOrderSizeDeltaAutoUpdated(address, bytes32, uint256, uint256) external => NONDET;
    function _.emitOrderCollateralDeltaAmountAutoUpdated(address, bytes32, uint256, uint256) external => NONDET;
    function _.emitOrderCancelled(address, bytes32, string, bytes) external => NONDET;
    function _.emitOrderFrozen(address, bytes32, string, bytes) external => NONDET;

    // emit functions from PositionEventUtils
    function _.emitPositionIncrease(address) external => NONDET;
    function _.emitPositionDecrease(address, bytes32, bytes32, Position.Props, uint256, uint256, Order.OrderType, address, Price.Props, Price.Props) external => NONDET;
    function _.emitInsolventCloseInfo(address, bytes32, uint256, int256, uint256) external => NONDET;
    function _.emitInsufficientFundingFeePayment(address, address, address, uint256, uint256) external => NONDET;
    function _.emitPositionFeesCollected(address, bytes32, address, address, uint256, bool, PositionPricingUtils.PositionFees) external => NONDET;
    function _.emitPositionFeesInfo(address, bytes32, address, address, uint256, bool, PositionPricingUtils.PositionFees) external => NONDET;
}

rule liquidationWorksIfConditionsAreMet() {
    env e;

    // executeLiquidation is not payable, hence e.msg.value == 0
    require(e.msg.value == 0);

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
    uint256 minLeverageFactor = _DataStore.getUint(e, _Keys.minCollateralFactorKey(e, market));
    require(to_mathint(positionSize) > minLeverageFactor * collateralAmount);

    // make sure we don't revert because of broken calldata or irrelevant modifiers
    executeLiquidationSetup(e, account, market, collateralToken, isLong, oracleParams);
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
