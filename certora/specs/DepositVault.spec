import "OnlyController.spec";

using DataStore as datastore;
using KeysHarness as keys;
//using RoleHarness as roles;
//using DepositVault as depositVault;

// depositvault balance equals pending deposits in datastore.
// containsBytes32(key) --> deposits exists
//  in that case: DepositUtils.get() will give deposit.
//  DepositVault should contain longToken shortToken and fee tokens for all these.
methods {
    function DataStore.getBytes32Count(bytes32 setKey) external returns (uint256) envfree;
    function DataStore.containsBytes32(bytes32 setKey, bytes32 value) external returns (bool) envfree;
    function DataStore.addBytes32(bytes32 setKey, bytes32 value) external;
    function DataStore.removeBytes32(bytes32 setKey, bytes32 value) external;
    function DataStore.getAddress(bytes32 key) external returns (address) envfree;
    function KeysHarness.DEPOSIT_LIST() external returns (bytes32) envfree;
    function KeysHarness.WNT() external returns (bytes32) envfree;
    function RoleHarness.CONTROLLER() external returns (bytes32) envfree;
    function DepositStoreUtils.get(address ds, bytes32 key) internal returns (Deposit.Props memory) => depositStoreGet(ds, key);
    function DepositStoreUtils.set(address ds, bytes32 key, Deposit.Props memory props) internal with (env e) => depositStoreSet(e, ds, key, props);
    function DepositStoreUtils.remove(address ds, bytes32 key, address account) internal with (env e) => depositStoreRemove(e, ds, key, account);
    function DepositStoreUtils.getAccountDepositCount(address ds, address account) internal returns (uint256) => depositStoreAccountCount[account];
    function DepositStoreUtils.getDepositCount(address ds) internal returns (uint256) => depositStoreCount;

    function MarketStoreUtils.get(address ds, address key) internal returns (Market.Props memory) => marketStoreGet(ds, key);
    function MarketStoreUtils.set(address ds, address key, bytes32 salt, Market.Props memory props) internal => NONDET;
    function MarketStoreUtils.remove(address ds, address key) internal => NONDET;

    function TokenUtils.nonRevertingTransferWithGasLimit(
        address token,
        address to,
        uint256 amount,
        uint256 gasLimit
    ) internal returns (bool, bytes memory) => nonRevertingTransfer(token, to, amount);

    function TokenUtils.withdrawAndSendNativeToken(
        address ds,
        address _wnt,
        address receiver,
        uint256 amount
    ) internal => withdrawAndSendNativeToken(receiver, amount);
    function TokenUtils.depositAndSendWrappedNativeToken(
        address ds,
        address receiver,
        uint256 amount
    ) internal => depositAndSendNativeToken(receiver, amount);
    function _.transferOutNativeToken(address keeper,uint256 amount) external => DISPATCHER(true);

    function RoleModule._validateRole(bytes32 role, string memory roleName) internal with (env e) => validateRole(e.msg.sender, role);

    function _.balanceOf(address account) external => tokenBalanceOf(calledContract, account) expect uint256;
    function _.afterDepositExecution(bytes32 key, Deposit.Props deposit, EventUtils.EventLogData eventData) external => NONDET;
    function _.afterDepositCancellation(bytes32 key, Deposit.Props deposit, EventUtils.EventLogData eventData) external => NONDET;
    function _.pluginTransfer(address token, address from, address to, uint256 amount) external => transferFrom(token, from, to, amount) expect void;
    //function SwapUtils.swap(SwapUtils.SwapParams params) external returns (address, uint256) => NONDET;
    function SwapUtils._swap(SwapUtils.SwapParams memory params, SwapUtils._SwapParams memory _params) internal returns (address, uint256) => NONDET;
    // Oracle Contract
    function _.setPrices(address ds, address eventEmitter, OracleUtils.SetPricesParams params) external => NONDET;
    function _.clearAllPrices() external => NONDET;

    // Datastore:
    function _.applyDeltaToUint(bytes32, int256, string) external => NONDET;
    function _.applyBoundedDeltaToUint(bytes32, int256) external => NONDET;
    function _.incrementUint(bytes32, uint256) external => NONDET;
    function DataStore.getUintValuesAt(bytes32 setKey, uint256 start, uint256 end) external returns (uint256[] memory) => NONDET DELETE;

    // MarketToken
    function _.mint(address receiver, uint256 amount) external => NONDET;


    // // Auto-summarized as NONDET the following internal pure/view functions found to be difficult (threshold: 5)
    // function MarketUtils.getPnl(address DataStore,Market.Props memory,Price.Props memory,bool,bool) internal returns (int256) => NONDET /* difficulty 54 */;
    // function MarketUtils.getReservedUsd(address DataStore,Market.Props memory,MarketUtils.MarketPrices memory,bool) internal returns (uint256) => NONDET /* difficulty 36 */;
    // function MarketUtils.getOpenInterest(address DataStore,Market.Props memory,bool) internal returns (uint256) => NONDET /* difficulty 14 */;
    // function MarketUtils.validatePoolAmount(address DataStore,Market.Props memory,address) internal  => NONDET /* difficulty 9 */;
    // function MarketUtils.getVirtualInventoryForSwaps(address DataStore,address) internal returns (bool,uint256,uint256) => NONDET /* difficulty 11 */;
    // //function ExchangeUtils.validateRequestCancellation(address DataStore,uint256,string memory) internal  => NONDET /* difficulty 8 */;
    // function MarketUtils.validateMarketTokenBalance(address DataStore,address) internal  => NONDET /* difficulty 68 */;
    // function MarketUtils.getPnlToPoolFactor(address DataStore,Market.Props memory,MarketUtils.MarketPrices memory,bool,bool) internal returns (int256) => NONDET /* difficulty 139 */;
    // function PricingUtils.applyImpactFactor(uint256,uint256,uint256) internal returns (uint256) => NONDET /* difficulty 119 */;
    // function PRBMath.mulDivFixedPoint(uint256,uint256) internal returns (uint256) => NONDET /* difficulty 15 */;
    // function MarketUtils.getOpenInterestInTokens(address DataStore,Market.Props memory,bool) internal returns (uint256) => NONDET /* difficulty 14 */;
    // function Precision.applyExponentFactor(uint256,uint256) internal returns (uint256) => NONDET /* difficulty 51 */;
    // function Math.mulDiv(uint256,uint256,uint256,Math.Rounding) internal returns (uint256) => NONDET /* difficulty 76 */;
    // function MarketUtils.isPnlFactorExceeded(address DataStore,Market.Props memory,MarketUtils.MarketPrices memory,bool,bytes32) internal returns (bool,int256,uint256) => NONDET /* difficulty 147 */;
    // function Precision.toFactor(uint256,uint256) internal returns (uint256) => NONDET /* difficulty 68 */;
    // function Precision.toFactor(int256,uint256) internal returns (int256) => NONDET /* difficulty 70 */;
    // function GasUtils.estimateExecuteDepositGasLimit(address DataStore,Deposit.Props memory) internal returns (uint256) => NONDET /* difficulty 21 */;
    // function MarketUtils.validateSwapPath(address DataStore,address[] memory) internal  => NONDET /* difficulty 13 */;
    // function GasUtils.adjustGasUsage(address DataStore,uint256) internal returns (uint256) => NONDET /* difficulty 74 */;
    // function MarketUtils.getNextCumulativeBorrowingFactor(address DataStore,Market.Props memory,MarketUtils.MarketPrices memory,bool) internal returns (uint256,uint256) => NONDET /* difficulty 294 */;
    // function PRBMathUD60x18.pow(uint256,uint256) internal returns (uint256) => NONDET /* difficulty 37 */;
    // function MarketUtils.getExpectedMinTokenBalance(address DataStore,Market.Props memory,address) internal returns (uint256) => NONDET /* difficulty 18 */;
    // function MarketUtils.getTotalPendingBorrowingFees(address DataStore,Market.Props memory,MarketUtils.MarketPrices memory,bool) internal returns (uint256) => NONDET /* difficulty 357 */;
    // function Precision.toFactor(uint256,uint256,bool) internal returns (uint256) => NONDET /* difficulty 68 */;
    // function SwapPricingUtils.getPriceImpactUsd(SwapPricingUtils.GetPriceImpactUsdParams memory) internal returns (int256) => NONDET /* difficulty 1081 */;
    // function MarketUtils.getBorrowingFactorPerSecond(address DataStore,Market.Props memory,MarketUtils.MarketPrices memory,bool) internal returns (uint256) => NONDET /* difficulty 278 */;
    // function PricingUtils.getPriceImpactUsdForSameSideRebalance(uint256,uint256,uint256,uint256) internal returns (int256) => NONDET /* difficulty 239 */;
    // function GasUtils.validateExecutionFee(address DataStore,uint256,uint256) internal  => NONDET /* difficulty 82 */;
    // function MarketUtils.getCollateralSum(address DataStore,address,address,bool,uint256) internal returns (uint256) => NONDET /* difficulty 7 */;
    // function MarketUtils.validateMarketTokenBalance(address DataStore,Market.Props memory,address) internal  => NONDET /* difficulty 38 */;
    // function SwapPricingUtils._getPriceImpactUsd(address DataStore,Market.Props memory,SwapPricingUtils.PoolParams memory) internal returns (int256) => NONDET /* difficulty 500 */;
    // function Precision.applyFactor(uint256,uint256) internal returns (uint256) => NONDET /* difficulty 68 */;
    // function MarketUtils.getAdjustedSwapImpactFactor(address DataStore,address,bool) internal returns (uint256) => NONDET /* difficulty 8 */;
    // function MarketUtils.getOpenInterest(address DataStore,address,address,bool,uint256) internal returns (uint256) => NONDET /* difficulty 7 */;
    // function Calc.roundUpMagnitudeDivision(int256,uint256) internal returns (int256) => NONDET /* difficulty 43 */;
    // function MarketUtils.usdToMarketTokenAmount(uint256,uint256,uint256) internal returns (uint256) => NONDET /* difficulty 78 */;
    // function PricingUtils.getPriceImpactUsdForCrossoverRebalance(uint256,uint256,uint256,uint256,uint256) internal returns (int256) => NONDET /* difficulty 239 */;
    // function MarketUtils.getUiFeeFactor(address DataStore,address) internal returns (uint256) => NONDET /* difficulty 6 */;
    // function PRBMathUD60x18.mul(uint256,uint256) internal returns (uint256) => NONDET /* difficulty 15 */;
    // function MarketUtils.getOpenInterestInTokens(address DataStore,address,address,bool,uint256) internal returns (uint256) => NONDET /* difficulty 7 */;
    // function MarketUtils.getCappedPnl(address DataStore,address,bool,int256,uint256,bytes32) internal returns (int256) => NONDET /* difficulty 74 */;
    // function Precision.mulDiv(uint256,uint256,uint256,bool) internal returns (uint256) => NONDET /* difficulty 68 */;
    // function MarketUtils.getPoolUsdWithoutPnl(address DataStore,Market.Props memory,MarketUtils.MarketPrices memory,bool,bool) internal returns (uint256) => NONDET /* difficulty 14 */;
    // function GasUtils.adjustGasLimitForEstimate(address DataStore,uint256) internal returns (uint256) => NONDET /* difficulty 74 */;
    // function MarketUtils.getPoolAmount(address,Market.Props memory,address) internal returns (uint256) => NONDET /* difficulty 6 */;
    // function Precision.mulDiv(uint256,uint256,uint256) internal returns (uint256) => NONDET /* difficulty 68 */;
    // function MarketUtils.getSwapImpactAmountWithCap(address DataStore,address,address,Price.Props memory,int256) internal returns (int256) => NONDET /* difficulty 54 */;
    // function Precision.mulDiv(uint256,int256,uint256) internal returns (int256) => NONDET /* difficulty 70 */;
    // function Precision.mulDiv(int256,uint256,uint256) internal returns (int256) => NONDET /* difficulty 70 */;
    // function Math.mulDiv(uint256,uint256,uint256) internal returns (uint256) => NONDET /* difficulty 68 */;
    // function MarketUtils.validateMarketTokenBalance(address DataStore,Market.Props[] memory) internal  => NONDET /* difficulty 58 */;
    // function MarketUtils.getNextTotalBorrowing(address DataStore,address,bool,uint256,uint256,uint256,uint256) internal returns (uint256) => NONDET /* difficulty 140 */;
    // function PRBMathUD60x18.log2(uint256) internal returns (uint256) => NONDET /* difficulty 14 */;
    // function MarketUtils.validateMaxPnl(address DataStore,Market.Props memory,MarketUtils.MarketPrices memory,bytes32,bytes32) internal  => NONDET /* difficulty 294 */;
    // function MarketUtils.getAdjustedSwapImpactFactors(address DataStore,address) internal returns (uint256,uint256) => NONDET /* difficulty 8 */;
    // function MarketUtils.validateMarketTokenBalance(address DataStore,Market.Props memory) internal  => NONDET /* difficulty 58 */;
    // function MarketUtils.getFundingAmountPerSizeDelta(uint256,uint256,uint256,bool) internal returns (uint256) => NONDET /* difficulty 81 */;
    // //function MarketUtils.getPoolValueInfo(address,Market.Props memory,Price.Props memory,Price.Props memory,Price.Props memory,bytes32,bool) internal returns (MarketPoolValueInfo.Props memory) => NONDET /* difficulty 1087 */;
    // function MarketUtils.validateEnabledMarket(address DataStore,address) internal  => NONDET /* difficulty 10 */;
    // function Precision.weiToFloat(uint256) internal returns (uint256) => NONDET /* difficulty 8 */;
    // function PRBMathUD60x18.exp2(uint256) internal returns (uint256) => NONDET /* difficulty 8 */;
    // function MarketUtils.validateReserve(address DataStore,Market.Props memory,MarketUtils.MarketPrices memory,bool) internal  => NONDET /* difficulty 122 */;

    // // Event functions
    // function DepositEventUtils.emitDepositCreated(
    //     address eventEmitter,
    //     bytes32 key,
    //     Deposit.Props memory deposit) internal => NONDET;
    // function DepositEventUtils.emitDepositExecuted(
    //     address eventEmitter,
    //     bytes32 key,
    //     address account,
    //     uint256 longTokenAmount,
    //     uint256 shortTokenAmount,
    //     uint256 receivedMarketTokens
    // ) internal => NONDET;
    // function DepositEventUtils.emitDepositCancelled(
    //     address eventEmitter,
    //     bytes32 key,
    //     address account,
    //     string memory reason,
    //     bytes memory reasonBytes
    // ) internal => NONDET;

    // function GasUtils.emitKeeperExecutionFee(
    //     address eventEmitter,
    //     address keeper,
    //     uint256 executionFeeAmount) internal => NONDET;
    // function GasUtils.emitExecutionFeeRefund(
    //     address eventEmitter,
    //     address receiver,
    //     uint256 refundFeeAmount
    // ) internal => NONDET;

    // function FeatureUtils.validateFeature(address, bytes32) internal => NONDET;

/*
    function EventEmitter.emitEventLog1(string memory eventName, bytes32 topic1,
        EventUtils.EventLogData memory eventData
    ) external => NONDET;
*/
}

// ghost field for the values array
ghost mapping(bytes32 => mapping(mathint => bytes32)) ghostValues {
    init_state axiom forall bytes32 setid. forall mathint x. ghostValues[setid][x] == to_bytes32(0);
}
// ghost field for the indexes map
ghost mapping(bytes32 => mapping(bytes32 => uint256)) ghostIndexes {
    init_state axiom  forall bytes32 setid. forall bytes32 x. ghostIndexes[setid][x] == 0;
}
// ghost field for the length of the values array (stored in offset 0)
ghost mapping(bytes32 => mathint) ghostLength {
    init_state axiom forall bytes32 setid. ghostLength[setid] == 0;
    // assumption: it's infeasible to grow the list to these many elements.
    axiom  forall bytes32 setid. ghostLength[setid] < 0xffffffffffffffffffffffffffffffff;
}

ghost mapping(address => mapping(bytes32 => bool)) hasRole;

// HOOKS
// Store hook to synchronize ghostLength with the length of the set._inner._values array.
// We need to use (offset 0) here, as there is no keyword yet to access the length.
hook Sstore datastore.bytes32Sets[KEY bytes32 dataset].(offset 0) uint256 newLength {
    ghostLength[dataset] = newLength;
}
// Store hook to synchronize ghostValues array with set._inner._values.
hook Sstore datastore.bytes32Sets[KEY bytes32 dataset]._inner._values[INDEX uint256 index] bytes32 newValue {
    ghostValues[dataset][index] = newValue;
}
// Store hook to synchronize ghostIndexes array with set._inner._indexes.
hook Sstore datastore.bytes32Sets[KEY bytes32 dataset]._inner._indexes[KEY bytes32 value] uint256 newIndex {
    ghostIndexes[dataset][value] = newIndex;
}

// The load hooks can use require to ensure that the ghost field has the same information as the storage.
// The require is sound, since the store hooks ensure the contents are always the same.  However we cannot
// prove that with invariants, since this would require the invariant to read the storage for all elements
// and neither storage access nor function calls are allowed in quantifiers.
//
// By following this simple pattern it is ensured that the ghost state and the storage are always the same
// and that the solver can use this knowledge in the proofs.

// Load hook to synchronize ghostLength with the length of the set._inner._values array.
// Again we use (offset 0) here, as there is no keyword yet to access the length.
hook Sload uint256 length datastore.bytes32Sets[KEY bytes32 dataset].(offset 0) {
    require ghostLength[dataset] == to_mathint(length);
}
hook Sload bytes32 value datastore.bytes32Sets[KEY bytes32 dataset]._inner._values[INDEX uint256 index] {
    require ghostValues[dataset][index] == value;
}
hook Sload uint256 index datastore.bytes32Sets[KEY bytes32 dataset]._inner._indexes[KEY bytes32 value] {
    require ghostIndexes[dataset][value] == index;
}

function validateRole(address caller, bytes32 role) {
    require hasRole[caller][role];
}

function depositAndSendNativeToken(address receiver, uint256 amount) {
    if (receiver == depositVault) {
        actualTokenBalances[nativeToken] = actualTokenBalances[nativeToken] + amount;
    }
}
function withdrawAndSendNativeToken(address receiver, uint256 amount) {
    actualTokenBalances[nativeToken] = actualTokenBalances[nativeToken] - amount;
}
function transferFrom(address token, address from, address receiver, uint256 amount) {
    if (from == depositVault) {
        actualTokenBalances[token] = actualTokenBalances[token] - amount;
        require actualTokenBalances[token] >= 0;
    }
    if (receiver == depositVault) {
        actualTokenBalances[token] = actualTokenBalances[token] + amount;
    }
}
function nonRevertingTransfer(address token, address receiver, uint256 amount) returns (bool, bytes) {
    bool success;
    if (success) {
        actualTokenBalances[token] = actualTokenBalances[token] - amount;
        require actualTokenBalances[token] >= 0;
    }
    return (success, _);
}

// INVARIANTS

//  This is the main invariant stating that the indexes and values always match:
//        values[indexes[v] - 1] = v for all values v in the set
//    and indexes[values[i]] = i+1 for all valid indexes i.

invariant setInvariant(bytes32 dataset)
    (forall mathint index. 0 <= index && index < ghostLength[dataset] => to_mathint(ghostIndexes[dataset][ghostValues[dataset][index]]) == index + 1)
    && (forall bytes32 value. ghostIndexes[dataset][value] == 0 ||
         (ghostValues[dataset][ghostIndexes[dataset][value] - 1] == value && ghostIndexes[dataset][value] >= 1 && to_mathint(ghostIndexes[dataset][value]) <= ghostLength[dataset]));


ghost address nativeToken;
ghost uint256 depositStoreCount;
ghost mapping(address => uint256) depositStoreAccountCount;
ghost mapping(address => mathint) expectedTokenBalances {
    init_state axiom forall address token. expectedTokenBalances[token] == 0;
}
ghost mapping(address => mathint) actualTokenBalances {
    init_state axiom forall address token. actualTokenBalances[token] == 0;
}
ghost mapping(bytes32 => address) depositsAccount;
ghost mapping(bytes32 => address) depositsInitialLongToken;
ghost mapping(bytes32 => address) depositsInitialShortToken;
ghost mapping(bytes32 => uint256) depositsInitialLongTokenAmount;
ghost mapping(bytes32 => uint256) depositsInitialShortTokenAmount;
ghost mapping(bytes32 => uint256) depositsExecutionFee;

function tokenBalanceOf(address token, address account) returns uint256 {
    uint256 balance;
    if (account == depositVault) {
        require to_mathint(balance) == actualTokenBalances[token];
    }
    return balance;
}

function marketStoreGet(address ds, address key) returns Market.Props {
    assert ds == datastore;
    Market.Props props;
    return props;
}

function depositStoreGet(address ds, bytes32 key) returns Deposit.Props {
    assert ds == datastore;
    Deposit.Props props;
    require datastore.containsBytes32(keys.DEPOSIT_LIST(), key);
    require props.addresses.account == depositsAccount[key];
    require props.addresses.initialLongToken == depositsInitialLongToken[key];
    require props.addresses.initialShortToken == depositsInitialShortToken[key];
    require props.numbers.initialLongTokenAmount == depositsInitialLongTokenAmount[key];
    require props.numbers.initialShortTokenAmount == depositsInitialShortTokenAmount[key];
    require props.numbers.executionFee == depositsExecutionFee[key];
    return props;
}
function depositStoreSet(env e, address ds, bytes32 key, Deposit.Props props) {
    assert ds == datastore;
    // TODO: this should be an assert, but we require nonce reasoning for that.
    require !datastore.containsBytes32(keys.DEPOSIT_LIST(), key);
    //assert !datastore.containsBytes32(keys.DEPOSIT_LIST(), key);
    datastore.addBytes32(e, keys.DEPOSIT_LIST(), key);
    depositStoreCount = require_uint256(depositStoreCount + 1);
    depositStoreAccountCount[props.addresses.account] = require_uint256(depositStoreAccountCount[props.addresses.account] + 1);
    depositsAccount[key] = props.addresses.account;
    depositsInitialLongToken[key] = props.addresses.initialLongToken;
    depositsInitialShortToken[key] = props.addresses.initialShortToken;
    depositsInitialLongTokenAmount[key] = props.numbers.initialLongTokenAmount;
    depositsInitialShortTokenAmount[key] = props.numbers.initialShortTokenAmount;
    depositsExecutionFee[key] = props.numbers.executionFee;
    expectedTokenBalances[props.addresses.initialLongToken] = expectedTokenBalances[props.addresses.initialLongToken] + props.numbers.initialLongTokenAmount;
    expectedTokenBalances[props.addresses.initialShortToken] = expectedTokenBalances[props.addresses.initialShortToken] + props.numbers.initialShortTokenAmount;
    expectedTokenBalances[nativeToken] = expectedTokenBalances[nativeToken] + props.numbers.executionFee;
}

function depositStoreRemove(env e, address ds, bytes32 key, address account) {
    assert ds == datastore;
    assert depositsAccount[key] == account;
    address initialLongToken = depositsInitialLongToken[key];
    address initialShortToken = depositsInitialShortToken[key];
    uint256 initialLongTokenAmount = depositsInitialLongTokenAmount[key];
    uint256 initialShortTokenAmount = depositsInitialShortTokenAmount[key];
    uint256 executionFee = depositsExecutionFee[key];

    datastore.removeBytes32(e, keys.DEPOSIT_LIST(), key);
    depositStoreCount = require_uint256(depositStoreCount - 1);
    depositStoreAccountCount[account] = require_uint256(depositStoreAccountCount[account] - 1);
    depositsAccount[key] = 0;
    depositsInitialLongToken[key] = 0;
    depositsInitialShortToken[key] = 0;
    depositsInitialLongTokenAmount[key] = 0;
    depositsInitialShortTokenAmount[key] = 0;
    depositsExecutionFee[key] = 0;
    expectedTokenBalances[initialLongToken] = expectedTokenBalances[initialLongToken] - initialLongTokenAmount;
    expectedTokenBalances[initialShortToken] = expectedTokenBalances[initialShortToken] - initialShortTokenAmount;
    expectedTokenBalances[nativeToken] = expectedTokenBalances[nativeToken] - executionFee;
}

invariant actualGeExpected(address token)
    actualTokenBalances[token] >= expectedTokenBalances[token]
    filtered {
        m -> !isOnlyController(m)
    }
    {
        preserved with (env e) {
            requireInvariant setInvariant(keys.DEPOSIT_LIST());
            requireInvariant vaultHasEnoughBalance(token);
            require nativeToken == datastore.getAddress(keys.WNT());
            require e.msg.sender != depositVault;
            require !hasRole[e.msg.sender][roles.CONTROLLER()];
        }
    }

invariant vaultHasEnoughBalance(address token)
    to_mathint(depositVault.tokenBalances[token]) >= expectedTokenBalances[token]
    filtered {
        m -> !isOnlyController(m)
    }
    {
        preserved with (env e) {
            requireInvariant setInvariant(keys.DEPOSIT_LIST());
            requireInvariant actualGeExpected(token);
            require nativeToken == datastore.getAddress(keys.WNT());
            require !hasRole[e.msg.sender][roles.CONTROLLER()];
        }
    }

rule createDepositOkay() {
    env e;
    DepositUtils.CreateDepositParams params;
    require nativeToken == datastore.getAddress(keys.WNT());
    require to_mathint(datastore.getBytes32Count(keys.DEPOSIT_LIST())) < 2^256-1;
    bytes32 key = createDeposit(e,params);
    assert datastore.containsBytes32(keys.DEPOSIT_LIST(), key);
    assert depositsAccount[key] == e.msg.sender;
}
