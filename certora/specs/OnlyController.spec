
using DataStore as dataStore;
using DepositHandler as depositHandler;
using RoleStore as roleStore;
using RoleHarness as roles;
using DepositVault as depositVault;

methods {
    function RoleStore.hasRole(address, bytes32) external returns (bool) envfree;
    function RoleHarness.CONTROLLER() external returns (bytes32) envfree;

    // Auto-summarized as NONDET the following internal pure/view functions found to be difficult (threshold: 5)
    function MarketUtils.getPnl(address DataStore,Market.Props memory,Price.Props memory,bool,bool) internal returns (int256) => NONDET /* difficulty 54 */;
    function MarketUtils.getReservedUsd(address DataStore,Market.Props memory,MarketUtils.MarketPrices memory,bool) internal returns (uint256) => NONDET /* difficulty 36 */;
    function MarketUtils.getOpenInterest(address DataStore,Market.Props memory,bool) internal returns (uint256) => NONDET /* difficulty 14 */;
    function MarketUtils.validatePoolAmount(address DataStore,Market.Props memory,address) internal  => NONDET /* difficulty 9 */;
    function MarketUtils.getVirtualInventoryForSwaps(address DataStore,address) internal returns (bool,uint256,uint256) => NONDET /* difficulty 11 */;
    //function ExchangeUtils.validateRequestCancellation(address DataStore,uint256,string memory) internal  => NONDET /* difficulty 8 */;
    function MarketUtils.validateMarketTokenBalance(address DataStore,address) internal  => NONDET /* difficulty 68 */;
    function MarketUtils.getPnlToPoolFactor(address DataStore,Market.Props memory,MarketUtils.MarketPrices memory,bool,bool) internal returns (int256) => NONDET /* difficulty 139 */;
    function PricingUtils.applyImpactFactor(uint256,uint256,uint256) internal returns (uint256) => NONDET /* difficulty 119 */;
    function PRBMath.mulDivFixedPoint(uint256,uint256) internal returns (uint256) => NONDET /* difficulty 15 */;
    function MarketUtils.getOpenInterestInTokens(address DataStore,Market.Props memory,bool) internal returns (uint256) => NONDET /* difficulty 14 */;
    function Precision.applyExponentFactor(uint256,uint256) internal returns (uint256) => NONDET /* difficulty 51 */;
    function Math.mulDiv(uint256,uint256,uint256,Math.Rounding) internal returns (uint256) => NONDET /* difficulty 76 */;
    function MarketUtils.isPnlFactorExceeded(address DataStore,Market.Props memory,MarketUtils.MarketPrices memory,bool,bytes32) internal returns (bool,int256,uint256) => NONDET /* difficulty 147 */;
    function Precision.toFactor(uint256,uint256) internal returns (uint256) => NONDET /* difficulty 68 */;
    function Precision.toFactor(int256,uint256) internal returns (int256) => NONDET /* difficulty 70 */;
    function GasUtils.estimateExecuteDepositGasLimit(address DataStore,Deposit.Props memory) internal returns (uint256) => NONDET /* difficulty 21 */;
    function MarketUtils.validateSwapPath(address DataStore,address[] memory) internal  => NONDET /* difficulty 13 */;
    function GasUtils.adjustGasUsage(address DataStore,uint256) internal returns (uint256) => NONDET /* difficulty 74 */;
    function MarketUtils.getNextCumulativeBorrowingFactor(address DataStore,Market.Props memory,MarketUtils.MarketPrices memory,bool) internal returns (uint256,uint256) => NONDET /* difficulty 294 */;
    function PRBMathUD60x18.pow(uint256,uint256) internal returns (uint256) => NONDET /* difficulty 37 */;
    function MarketUtils.getExpectedMinTokenBalance(address DataStore,Market.Props memory,address) internal returns (uint256) => NONDET /* difficulty 18 */;
    function MarketUtils.getTotalPendingBorrowingFees(address DataStore,Market.Props memory,MarketUtils.MarketPrices memory,bool) internal returns (uint256) => NONDET /* difficulty 357 */;
    function Precision.toFactor(uint256,uint256,bool) internal returns (uint256) => NONDET /* difficulty 68 */;
    function SwapPricingUtils.getPriceImpactUsd(SwapPricingUtils.GetPriceImpactUsdParams memory) internal returns (int256) => NONDET /* difficulty 1081 */;
    function MarketUtils.getBorrowingFactorPerSecond(address DataStore,Market.Props memory,MarketUtils.MarketPrices memory,bool) internal returns (uint256) => NONDET /* difficulty 278 */;
    function PricingUtils.getPriceImpactUsdForSameSideRebalance(uint256,uint256,uint256,uint256) internal returns (int256) => NONDET /* difficulty 239 */;
    function GasUtils.validateExecutionFee(address DataStore,uint256,uint256) internal  => NONDET /* difficulty 82 */;
    function MarketUtils.getCollateralSum(address DataStore,address,address,bool,uint256) internal returns (uint256) => NONDET /* difficulty 7 */;
    function MarketUtils.validateMarketTokenBalance(address DataStore,Market.Props memory,address) internal  => NONDET /* difficulty 38 */;
    function SwapPricingUtils._getPriceImpactUsd(address DataStore,Market.Props memory,SwapPricingUtils.PoolParams memory) internal returns (int256) => NONDET /* difficulty 500 */;
    function Precision.applyFactor(uint256,uint256) internal returns (uint256) => NONDET /* difficulty 68 */;
    function MarketUtils.getAdjustedSwapImpactFactor(address DataStore,address,bool) internal returns (uint256) => NONDET /* difficulty 8 */;
    function MarketUtils.getOpenInterest(address DataStore,address,address,bool,uint256) internal returns (uint256) => NONDET /* difficulty 7 */;
    function Calc.roundUpMagnitudeDivision(int256,uint256) internal returns (int256) => NONDET /* difficulty 43 */;
    function MarketUtils.usdToMarketTokenAmount(uint256,uint256,uint256) internal returns (uint256) => NONDET /* difficulty 78 */;
    function PricingUtils.getPriceImpactUsdForCrossoverRebalance(uint256,uint256,uint256,uint256,uint256) internal returns (int256) => NONDET /* difficulty 239 */;
    function MarketUtils.getUiFeeFactor(address DataStore,address) internal returns (uint256) => NONDET /* difficulty 6 */;
    function PRBMathUD60x18.mul(uint256,uint256) internal returns (uint256) => NONDET /* difficulty 15 */;
    function MarketUtils.getOpenInterestInTokens(address DataStore,address,address,bool,uint256) internal returns (uint256) => NONDET /* difficulty 7 */;
    function MarketUtils.getCappedPnl(address DataStore,address,bool,int256,uint256,bytes32) internal returns (int256) => NONDET /* difficulty 74 */;
    function Precision.mulDiv(uint256,uint256,uint256,bool) internal returns (uint256) => NONDET /* difficulty 68 */;
    function MarketUtils.getPoolUsdWithoutPnl(address DataStore,Market.Props memory,MarketUtils.MarketPrices memory,bool,bool) internal returns (uint256) => NONDET /* difficulty 14 */;
    function GasUtils.adjustGasLimitForEstimate(address DataStore,uint256) internal returns (uint256) => NONDET /* difficulty 74 */;
    function MarketUtils.getPoolAmount(address,Market.Props memory,address) internal returns (uint256) => NONDET /* difficulty 6 */;
    function Precision.mulDiv(uint256,uint256,uint256) internal returns (uint256) => NONDET /* difficulty 68 */;
    function MarketUtils.getSwapImpactAmountWithCap(address DataStore,address,address,Price.Props memory,int256) internal returns (int256) => NONDET /* difficulty 54 */;
    function Precision.mulDiv(uint256,int256,uint256) internal returns (int256) => NONDET /* difficulty 70 */;
    function Precision.mulDiv(int256,uint256,uint256) internal returns (int256) => NONDET /* difficulty 70 */;
    function Math.mulDiv(uint256,uint256,uint256) internal returns (uint256) => NONDET /* difficulty 68 */;
    function MarketUtils.validateMarketTokenBalance(address DataStore,Market.Props[] memory) internal  => NONDET /* difficulty 58 */;
    function MarketUtils.getNextTotalBorrowing(address DataStore,address,bool,uint256,uint256,uint256,uint256) internal returns (uint256) => NONDET /* difficulty 140 */;
    function PRBMathUD60x18.log2(uint256) internal returns (uint256) => NONDET /* difficulty 14 */;
    function MarketUtils.validateMaxPnl(address DataStore,Market.Props memory,MarketUtils.MarketPrices memory,bytes32,bytes32) internal  => NONDET /* difficulty 294 */;
    function MarketUtils.getAdjustedSwapImpactFactors(address DataStore,address) internal returns (uint256,uint256) => NONDET /* difficulty 8 */;
    function MarketUtils.validateMarketTokenBalance(address DataStore,Market.Props memory) internal  => NONDET /* difficulty 58 */;
    function MarketUtils.getFundingAmountPerSizeDelta(uint256,uint256,uint256,bool) internal returns (uint256) => NONDET /* difficulty 81 */;
    //function MarketUtils.getPoolValueInfo(address,Market.Props memory,Price.Props memory,Price.Props memory,Price.Props memory,bytes32,bool) internal returns (MarketPoolValueInfo.Props memory) => NONDET /* difficulty 1087 */;
    function MarketUtils.validateEnabledMarket(address DataStore,address) internal  => NONDET /* difficulty 10 */;
    function Precision.weiToFloat(uint256) internal returns (uint256) => NONDET /* difficulty 8 */;
    function PRBMathUD60x18.exp2(uint256) internal returns (uint256) => NONDET /* difficulty 8 */;
    function MarketUtils.validateReserve(address DataStore,Market.Props memory,MarketUtils.MarketPrices memory,bool) internal  => NONDET /* difficulty 122 */;

    // Event functions
    function DepositEventUtils.emitDepositCreated(
        address eventEmitter,
        bytes32 key,
        Deposit.Props memory deposit) internal => NONDET;
    function DepositEventUtils.emitDepositExecuted(
        address eventEmitter,
        bytes32 key,
        address account,
        uint256 longTokenAmount,
        uint256 shortTokenAmount,
        uint256 receivedMarketTokens
    ) internal => NONDET;
    function DepositEventUtils.emitDepositCancelled(
        address eventEmitter,
        bytes32 key,
        address account,
        string memory reason,
        bytes memory reasonBytes
    ) internal => NONDET;
    function GasUtils.emitKeeperExecutionFee(
        address eventEmitter,
        address keeper,
        uint256 executionFeeAmount) internal => NONDET;
    function GasUtils.emitExecutionFeeRefund(
        address eventEmitter,
        address receiver,
        uint256 refundFeeAmount
    ) internal => NONDET;

    function FeatureUtils.validateFeature(address, bytes32) internal => NONDET;
}

definition isOnlyController(method f) returns bool =
    (
        (f.selector == sig:DataStore.setUint(bytes32,uint256).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.removeUint(bytes32).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.applyDeltaToUint(bytes32,int256,string).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.incrementInt(bytes32,int256).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.decrementInt(bytes32,int256).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.setAddress(bytes32,address).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.removeAddress(bytes32).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.setBool(bytes32,bool).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.removeBool(bytes32).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.setString(bytes32,string).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.removeString(bytes32).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.setBytes32(bytes32, bytes32).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.removeBytes32(bytes32).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.setUintArray(bytes32,uint256[]).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.removeUintArray(bytes32).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.setIntArray(bytes32,int256[]).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.removeIntArray(bytes32).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.setAddressArray(bytes32, address[]).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.removeAddressArray(bytes32).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.setBoolArray(bytes32, bool[]).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.removeBoolArray(bytes32).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.setStringArray(bytes32, string[]).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.removeStringArray(bytes32).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.setBytes32Array(bytes32, bytes32[]).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.removeBytes32Array(bytes32).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.addBytes32(bytes32, bytes32).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.removeBytes32(bytes32).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.addAddress(bytes32, address).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.removeAddress(bytes32).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.addUint(bytes32, uint256).selector && f.contract == dataStore) ||
        (f.selector == sig:DataStore.removeUint(bytes32).selector && f.contract == dataStore) ||
        (f.selector == sig:DepositHandler.createDeposit(address, DepositUtils.CreateDepositParams).selector && f.contract == depositHandler) ||
        (f.selector == sig:DepositHandler.cancelDeposit(bytes32).selector && f.contract == depositHandler) ||
        (f.selector == sig:DepositVault.transferOut(address, address, uint256).selector && f.contract == depositVault) ||
        (f.selector == sig:DepositVault.transferOut(address, address, uint256, bool).selector && f.contract == depositVault) ||
        (f.selector == sig:DepositVault.transferOutNativeToken(address, uint256).selector && f.contract == depositVault) ||
        (f.selector == sig:DepositVault.recordTransferIn(address).selector && f.contract == depositVault) ||
        (f.selector == sig:DepositVault.syncTokenBalance(address).selector && f.contract == depositVault) ||
        false
    );


rule checkOnlyController(method f, env e, calldataarg args) filtered {
    f -> isOnlyController(f)
} {
    bool hasRoleController = roleStore.hasRole(e.msg.sender, roles.CONTROLLER());
    f(e,args);
    assert hasRoleController;
}
