using WNT as wnt;
using DummyERC20A as DummyERC20Long;
using DummyERC20B as DummyERC20Short;
using OrderStoreUtils as OrderStoreUtils;
using MarketToken as MarketToken;
using Position as Position;
using Order as Order;
using OrderVault as OrderVault;
using MarketUtils as MarketUtils;
using DepositVault as DepositVault;
using Price as Price;
using MarketPoolValueInfo as MarketPoolValueInfo;
using Keys as Keys;
using Oracle as Oracle;
using GetPositionKeyHarness as positionKeyHarness;
using BaseOrderHandler as BaseOrderHandler;

methods {  
    //OrderHandler - createOrder
    function _.createOrderFeatureDisabledKey(address,uint256) internal => NONDET;
    function _.validateFeature(address,bytes32) internal => NONDET;
    function _.createOrder(address,address,address,address,address,BaseOrderUtils.CreateOrderParams) external => NONDET;

    //OrderHandler - updateOrder
    function _.isMarketOrder(Order.OrderType) internal => NONDET;
    function _.wnt(address) internal => myWNT() expect address;
    function _.estimateExecuteOrderGasLimit(address, Order.Props memory) internal => NONDET;
    function _.validateExecutionFee(address,uint256,uint256) internal => NONDET;

    //OrderHandler - cancelOrder
    function _.cancelOrderFeatureDisabledKey(address,uint256) internal => NONDET;
    function _.validateRequestCancellation(address,uint256,string memory) internal => NONDET;
    function _.cancelOrder(address,address,address,bytes32,address,uint256,string,bytes) external => NONDET;

    //OrderHandler - executeOrder
    function _.getExecutionGas(address,uint256) internal => NONDET;
    function _.executeOrderFeatureDisabledKey(address,uint256) internal => NONDET;
    function _.getErrorSelectorFromData(bytes memory) internal => NONDET;
    function _.isOracleError(bytes4) internal => NONDET;
    function _.revertWithCustomError(bytes memory) internal => NONDET;
    // function _.getRevertMessage(bytes memory) internal => NONDET;
    // function _handleOrderError(bytes32,uint256,bytes memory) internal => NONDET;
    // function _.getUncompactedOracleBlockNumbers(uint256[] memory,uint256) internal returns (uint256[] memory) => NONDET;

    // MarketUtils
    function MarketUtils.getReservedUsdEx(address, Market.Props memory, MarketUtils.MarketPrices memory, bool) external returns (uint256) optional envfree;
    function MarketUtils.getReserveFactorEx(address, address, bool) external returns (uint256) optional envfree;
    function MarketUtils.getMaxPnlFactorEx(address, bytes32, address, bool) external returns (uint256) optional envfree;
    function MarketUtils.getPoolAmountEx(address, Market.Props memory, address) external returns (uint256) optional envfree;
    function MarketUtils.getPoolValueInfo(address,Market.Props memory,Price.Props memory,Price.Props memory,Price.Props memory, bytes32, bool) external returns (MarketPoolValueInfo.Props memory) optional envfree;



    // ERC20
    function _.name()                                external  => DISPATCHER(true);
    function _.symbol()                              external  => DISPATCHER(true);
    function _.decimals()                            external  => DISPATCHER(true);
    function _.totalSupply()                         external  => DISPATCHER(true);
    function _.balanceOf(address)                    external  => DISPATCHER(true);
    function _.allowance(address,address)            external  => DISPATCHER(true);
    function _.approve(address,uint256)              external  => DISPATCHER(true);
    function _.transfer(address,uint256)             external  => DISPATCHER(true);
    function _.transferFrom(address,address,uint256) external  => DISPATCHER(true);

    // blanceOf:
    function DummyERC20A.balanceOf(address) external returns (uint256) envfree;
    function DummyERC20B.balanceOf(address) external returns (uint256) envfree;

    // WNT
    function _.deposit()                             external  => DISPATCHER(true);
    function _.withdraw(uint256)                     external  => DISPATCHER(true);

    //Bank
    function _.transferOut(address,address,uint256,bool) external => DISPATCHER(true);
    function _.transferOut(address,address,uint256) external => DISPATCHER(true);

    //Datastore
    function _.getUint(bytes32 key) external => NONDET;
    function _.setUint(bytes32 key, uint256 value) external => NONDET;
    function _.removeUint(bytes32 key) external => NONDET;
    function _.applyDeltaToUint(bytes32 key, int256 value, string) external => NONDET;
    function _.applyDeltaToUint(bytes32 key, uint256 value) external => NONDET;
    function _.applyBoundedDeltaToUint(bytes32 key, int256 value) external => NONDET;
    function _.incrementUint(bytes32 key, uint256 value) external => NONDET;
    function _.decrementUint(bytes32 key, uint256 value) external => NONDET;
    function _.getInt(bytes32 key) external => NONDET;
    function _.setInt(bytes32 key, int256 value) external => NONDET;
    function _.removeInt(bytes32 key) external => NONDET;
    function _.applyDeltaToInt(bytes32 key, int256 value) external => NONDET;
    function _.incrementInt(bytes32 key, int256 value) external => NONDET;
    function _.decrementInt(bytes32 key, int256 value) external => NONDET;
    function _.getAddress(bytes32 key) external => NONDET;
    function _.setAddress(bytes32 key, address value) external => NONDET;
    function _.removeAddress(bytes32 key) external => NONDET;
    function _.getBool(bytes32 key) external => NONDET;
    function _.setBool(bytes32 key, bool value) external => NONDET;
    function _.removeBool(bytes32 key) external => NONDET;
    function _.getString(bytes32 key) external => NONDET;
    function _.setString(bytes32 key, string) external => NONDET;
    function _.removeString(bytes32 key) external => NONDET;
    function _.getBytes32(bytes32 key) external => NONDET;
    function _.setBytes32(bytes32 key, bytes32 value) external => NONDET;
    function _.removeBytes32(bytes32 key) external => NONDET;
    function _.getUintArray(bytes32 key) external => NONDET;
    function _.setUintArray(bytes32 key, uint256[]) external => NONDET;
    function _.removeUintArray(bytes32 key) external => NONDET;
    function _.getIntArray(bytes32 key) external => NONDET;
    function _.setIntArray(bytes32 key, int256[]) external => NONDET;
    function _.removeIntArray(bytes32 key) external => NONDET;
    function _.getAddressArray(bytes32 key) external => NONDET;
    function _.setAddressArray(bytes32 key, address[]) external => NONDET;
    function _.removeAddressArray(bytes32 key) external => NONDET;
    function _.getBoolArray(bytes32 key) external => NONDET;
    function _.setBoolArray(bytes32 key, bool[]) external => NONDET;
    function _.removeBoolArray(bytes32 key) external => NONDET;
    function _.getStringArray(bytes32 key) external => NONDET;
    function _.setStringArray(bytes32 key, string[]) external => NONDET;
    function _.removeStringArray(bytes32 key) external => NONDET;
    function _.getBytes32Array(bytes32 key) external => NONDET;
    function _.setBytes32Array(bytes32 key, bytes32[]) external => NONDET;
    function _.removeBytes32Array(bytes32 key) external => NONDET;
    function _.containsBytes32(bytes32 setKey, bytes32 value) external => NONDET;
    function _.getBytes32Count(bytes32 setKey) external => NONDET;
    function _.getBytes32ValuesAt(bytes32 setKey, uint256 start, uint256 end) external => NONDET;
    function _.addBytes32(bytes32 setKey, bytes32 value) external => NONDET;
    function _.removeBytes32(bytes32 setKey, bytes32 value) external => NONDET;
    function _.containsAddress(bytes32 setKey, address value) external => NONDET;
    function _.getAddressCount(bytes32 setKey) external => NONDET;
    function _.getAddressValuesAt(bytes32 setKey, uint256 start, uint256 end) external => NONDET;
    function _.addAddress(bytes32 setKey, address value) external => NONDET;
    function _.removeAddress(bytes32 setKey, address value) external => NONDET;
    function _.containsUint(bytes32 setKey, uint256 value) external => NONDET;
    function _.getUintCount(bytes32 setKey) external => NONDET;
    function _.getUintValuesAt(bytes32 setKey, uint256 start, uint256 end) external => NONDET;
    function _.addUint(bytes32 setKey, uint256 value) external => NONDET;
    function _.removeUint(bytes32 setKey, uint256 value) external => NONDET;

    //Oracle
    function Oracle.getPrimaryPrice(address) external returns (Price.Props memory) envfree;
    function _.setPrices(address,address,OracleUtils.SetPricesParams) external => NONDET;
    function _.clearAllPrices() external => NONDET;
    function _.setPrimaryPrice(address,Price.Props) external => NONDET;

    //RoleStore
    function _.hasRole(address,bytes32) external => DISPATCHER(true);
    function _.revokeRole(address,bytes32) external => DISPATCHER(true);
    function _.grantRole(address,bytes32) external => DISPATCHER(true);

    //GlobalReentrancyGuard
    function _._nonReentrantBefore() internal => NONDET;
    function _._nonReentrantAfter() internal => NONDET;

    //RoleModule
    function _._validateRole(bytes32,string memory) internal => NONDET;

    //ArbSys
    function _.arbBlockNumber() external => NONDET;
    function _.arbBlockHash(uint256) external => NONDET;

    //DepositEventUtils
    function _.emitDepositCreated(address,bytes32,Deposit.Props) external => NONDET;

    //StrictBank
    function _.recordTransferIn(address) external => NONDET;

    // OrderStoreUtils.sol
    // function OrderStoreUtils.get(address dataStore, bytes32 key) external returns (Order.Props memory) optional => getOrder(key);
    // function OrderStoreUtils.set(address dataStore, bytes32 key, Order.Props memory order) external optional => setOrder(key, order);
    // function OrderStoreUtils.remove(address dataStore, bytes32 key, address account) external optional => removeOrder(key);

    // function _.getExecuteOrderParams(bytes32,OracleUtils.SetPricesParams,address,uint256,Order.SecondaryOrderType) external => NONDET;

    // PositionStoreUtils.sol
    function PositionStoreUtils.get(address dataStore, bytes32 key) external returns (Position.Props) optional => getPosition(key);
    function PositionStoreUtils.set(address dataStore, bytes32 key, Position.Props position) external optional => setPosition(key, position);

    // Keys.sol
    function Keys.MAX_PNL_FACTOR_FOR_TRADERS() external returns (bytes32) envfree;
}

// OrderStoreUtils Ghosts:
// struct Props {
//     Addresses addresses;
//     Numbers numbers;
//     Flags flags;
// }

// struct Addresses {
//     address account;
//     address receiver;
//     address callbackContract;
//     address uiFeeReceiver;
//     address market;
//     address initialCollateralToken;
//     address[] swapPath;
// }
ghost mapping(bytes32 => address) AddressesAccounts;
ghost mapping(bytes32 => address) AddressesReceivers;
ghost mapping(bytes32 => address) AddressesCallbackContract;
ghost mapping(bytes32 => address) AddressesUiFeeReceivers;
ghost mapping(bytes32 => address) AddressesMarkets;
ghost mapping(bytes32 => address) AddressesInitialCollateralTokens;
ghost mapping(bytes32 => mapping(uint256 => address)) AddressesSwapPaths;

function setAddresses(bytes32 key, Order.Addresses addresses) {
    AddressesAccounts[key] = addresses.account;
    AddressesReceivers[key] = addresses.receiver;
    AddressesCallbackContract[key] = addresses.callbackContract;
    AddressesUiFeeReceivers[key] = addresses.uiFeeReceiver;
    AddressesMarkets[key] = addresses.market;
    AddressesInitialCollateralTokens[key] = addresses.initialCollateralToken;
    AddressesSwapPaths[key][0] = addresses.swapPath[0];
    AddressesSwapPaths[key][1] = addresses.swapPath[1];
    AddressesSwapPaths[key][2] = addresses.swapPath[2];
}

function getAddresses(bytes32 key, Order.Props props) {
    // Order.Addresses addresses;
    require props.addresses.account == AddressesAccounts[key];
    require props.addresses.receiver == AddressesReceivers[key];
    require props.addresses.callbackContract == AddressesCallbackContract[key];
    require props.addresses.uiFeeReceiver == AddressesUiFeeReceivers[key];
    require props.addresses.market == AddressesMarkets[key];
    require props.addresses.initialCollateralToken == AddressesInitialCollateralTokens[key];
    require props.addresses.swapPath[0] == AddressesSwapPaths[key][0];
    require props.addresses.swapPath[1] == AddressesSwapPaths[key][1];
    require props.addresses.swapPath[2] == AddressesSwapPaths[key][2];
    
    // return addresses;
}

function removeAddresses(bytes32 key) {
    AddressesAccounts[key] = 0;
    AddressesReceivers[key] = 0;
    AddressesCallbackContract[key] = 0;
    AddressesUiFeeReceivers[key] = 0;
    AddressesMarkets[key] = 0;
    AddressesInitialCollateralTokens[key] = 0;
    AddressesSwapPaths[key][0] = 0;
    AddressesSwapPaths[key][1] = 0;
    AddressesSwapPaths[key][2] = 0;
}

// struct Numbers {
//     OrderType orderType;
//     DecreasePositionSwapType decreasePositionSwapType;
//     uint256 sizeDeltaUsd;
//     uint256 initialCollateralDeltaAmount;
//     uint256 triggerPrice;
//     uint256 acceptablePrice;
//     uint256 executionFee;
//     uint256 callbackGasLimit;
//     uint256 minOutputAmount;
//     uint256 updatedAtBlock;
// }
ghost mapping(bytes32 => uint256) NumbersOrderType;
ghost mapping(bytes32 => uint256) NumbersDecreasePositionSwapType;
ghost mapping(bytes32 => uint256) NumbersSizeDeltaUsd;
ghost mapping(bytes32 => uint256) NumbersInitialCollateralDeltaAmount;
ghost mapping(bytes32 => uint256) NumbersTriggerPrice;
ghost mapping(bytes32 => uint256) NumbersAcceptablePrice;
ghost mapping(bytes32 => uint256) NumbersExecutionFee;
ghost mapping(bytes32 => uint256) NumbersCallbackGasLimit;
ghost mapping(bytes32 => uint256) NumbersMinOutputAmount;
ghost mapping(bytes32 => uint256) NumbersUpdatedAtBlock;

function setNumbers(bytes32 key, Order.Numbers numbers) {
    NumbersOrderType[key] = assert_uint256(numbers.orderType);
    NumbersDecreasePositionSwapType[key] = assert_uint256(numbers.decreasePositionSwapType);
    NumbersSizeDeltaUsd[key] = numbers.sizeDeltaUsd;
    NumbersInitialCollateralDeltaAmount[key] = numbers.initialCollateralDeltaAmount;
    NumbersTriggerPrice[key] = numbers.triggerPrice;
    NumbersAcceptablePrice[key] = numbers.acceptablePrice;
    NumbersExecutionFee[key] = numbers.executionFee;
    NumbersCallbackGasLimit[key] = numbers.callbackGasLimit;
    NumbersMinOutputAmount[key] = numbers.minOutputAmount;
    NumbersUpdatedAtBlock[key] = numbers.updatedAtBlock;
}

function getNumbers(bytes32 key, Order.Props props) {
    // Order.Numbers numbers;
    require assert_uint256(props.numbers.orderType) == NumbersOrderType[key];
    require assert_uint256(props.numbers.decreasePositionSwapType) == NumbersDecreasePositionSwapType[key];
    require props.numbers.sizeDeltaUsd == NumbersSizeDeltaUsd[key];
    require props.numbers.initialCollateralDeltaAmount == NumbersInitialCollateralDeltaAmount[key];
    require props.numbers.triggerPrice == NumbersTriggerPrice[key];
    require props.numbers.acceptablePrice == NumbersAcceptablePrice[key];
    require props.numbers.executionFee == NumbersExecutionFee[key];
    require props.numbers.callbackGasLimit == NumbersCallbackGasLimit[key];
    require props.numbers.minOutputAmount == NumbersMinOutputAmount[key];
    require props.numbers.updatedAtBlock == NumbersUpdatedAtBlock[key];

    // return numbers;
}

function removeNumbers(bytes32 key) {
    NumbersOrderType[key] = 0;
    NumbersDecreasePositionSwapType[key] = 0;
    NumbersSizeDeltaUsd[key] = 0;
    NumbersInitialCollateralDeltaAmount[key] = 0;
    NumbersTriggerPrice[key] = 0;
    NumbersAcceptablePrice[key] = 0;
    NumbersExecutionFee[key] = 0;
    NumbersCallbackGasLimit[key] = 0;
    NumbersMinOutputAmount[key] = 0;
    NumbersUpdatedAtBlock[key] = 0;
}

// struct Flags {
//     bool isLong;
//     bool shouldUnwrapNativeToken;
//     bool isFrozen;
// }
ghost mapping(bytes32 => bool) FlagsIsLong;
ghost mapping(bytes32 => bool) FlagsShouldUnwrapNativeToken;
ghost mapping(bytes32 => bool) FlagsIsFrozen;

function setFlags(bytes32 key, Order.Flags flags) {
    FlagsIsLong[key] = flags.isLong;
    FlagsShouldUnwrapNativeToken[key] = flags.shouldUnwrapNativeToken;
    FlagsIsFrozen[key] = flags.isFrozen;
}

function getFlags(bytes32 key, Order.Props props) {
    // Order.Flags flags;
    require props.flags.isLong == FlagsIsLong[key];
    require props.flags.shouldUnwrapNativeToken == FlagsShouldUnwrapNativeToken[key];
    require props.flags.isFrozen == FlagsIsFrozen[key];

    // return flags;
}

function setOrder(bytes32 key, Order.Props order) {
    setAddresses(key, order.addresses);
    setNumbers(key, order.numbers);
    setFlags(key, order.flags);
} 

function getOrder(bytes32 key) returns Order.Props {
    Order.Props props;
    getAddresses(key, props);
    getNumbers(key, props);
    getFlags(key, props);

    return props;
} 

function removeOrder(bytes32 key) {
    removeAddresses(key);
    removeNumbers(key);
} 

// struct Props {
//     Addresses addresses;
//     Numbers numbers;
//     Flags flags;
// }

// struct Addresses {
//     address account;
//     address market;
//     address collateralToken;
// }
ghost mapping(bytes32 => address) PositionAddressesAccounts;
ghost mapping(bytes32 => address) PositionAddressesMarkets;
ghost mapping(bytes32 => address) PositionAddressesCollateralToken;

function setPositionAddresses(bytes32 key, Position.Addresses positionAddresses) {
    PositionAddressesAccounts[key] = positionAddresses.account;
    PositionAddressesMarkets[key] = positionAddresses.market;
    PositionAddressesCollateralToken[key] = positionAddresses.collateralToken;
}

function getPositionAddresses(bytes32 key, Position.Props positionProps) {
    require positionProps.addresses.account == PositionAddressesAccounts[key];
    require positionProps.addresses.market == PositionAddressesMarkets[key];
    require positionProps.addresses.collateralToken == PositionAddressesCollateralToken[key];
}

function removePositionAddresses(bytes32 key) {
    PositionAddressesAccounts[key] = 0;
    PositionAddressesMarkets[key] = 0;
    PositionAddressesCollateralToken[key] = 0;
}

// struct Numbers {
//     uint256 sizeInUsd;
//     uint256 sizeInTokens;
//     uint256 collateralAmount;
//     uint256 borrowingFactor;
//     uint256 fundingFeeAmountPerSize;
//     uint256 longTokenClaimableFundingAmountPerSize;
//     uint256 shortTokenClaimableFundingAmountPerSize;
//     uint256 increasedAtBlock;
//     uint256 decreasedAtBlock;
// }
ghost mapping(bytes32 => uint256) PositionNumbersSizeInUsd;
ghost mapping(bytes32 => uint256) PositionNumbersSizeInTokens;
ghost mapping(bytes32 => uint256) PositionNumbersCollateralAmount;
ghost mapping(bytes32 => uint256) PositionNumbersBorrowingFactor;
ghost mapping(bytes32 => uint256) PositionNumbersFundingFeeAmountPerSize;
ghost mapping(bytes32 => uint256) PositionNumbersLongTokenClaimableFundingAmountPerSize;
ghost mapping(bytes32 => uint256) PositionNumbersShortTokenClaimableFundingAmountPerSize;
ghost mapping(bytes32 => uint256) PositionNumbersIncreasedAtBlock;
ghost mapping(bytes32 => uint256) PositionNumbersDecreasedAtBlock;

ghost mathint sumOfLongs;
ghost mathint sumOfShorts;

function setPositionNumbers(bytes32 key, Position.Numbers positionNumbers) {
    sumOfShorts = PositionFlagsIsLong[key] ? sumOfShorts : sumOfShorts - PositionNumbersSizeInUsd[key] + positionNumbers.sizeInUsd;
    sumOfLongs = PositionFlagsIsLong[key] ? sumOfLongs - PositionNumbersSizeInTokens[key] + positionNumbers.sizeInTokens : sumOfLongs;
    PositionNumbersSizeInUsd[key] = positionNumbers.sizeInUsd;
    PositionNumbersSizeInTokens[key] = positionNumbers.sizeInTokens;
    PositionNumbersCollateralAmount[key] = positionNumbers.collateralAmount;
    PositionNumbersBorrowingFactor[key] = positionNumbers.borrowingFactor;
    PositionNumbersFundingFeeAmountPerSize[key] = positionNumbers.fundingFeeAmountPerSize;
    PositionNumbersLongTokenClaimableFundingAmountPerSize[key] = positionNumbers.longTokenClaimableFundingAmountPerSize;
    PositionNumbersShortTokenClaimableFundingAmountPerSize[key] = positionNumbers.shortTokenClaimableFundingAmountPerSize;
    PositionNumbersIncreasedAtBlock[key] = positionNumbers.increasedAtBlock;
    PositionNumbersDecreasedAtBlock[key] = positionNumbers.decreasedAtBlock;
}

function getPositionNumbers(bytes32 key, Position.Props positionProps) {
    require positionProps.numbers.sizeInUsd == PositionNumbersSizeInUsd[key];
    require positionProps.numbers.sizeInTokens == PositionNumbersSizeInTokens[key];
    require positionProps.numbers.collateralAmount == PositionNumbersCollateralAmount[key];
    require positionProps.numbers.borrowingFactor == PositionNumbersBorrowingFactor[key];
    require positionProps.numbers.fundingFeeAmountPerSize == PositionNumbersFundingFeeAmountPerSize[key];
    require positionProps.numbers.longTokenClaimableFundingAmountPerSize == PositionNumbersLongTokenClaimableFundingAmountPerSize[key];
    require positionProps.numbers.shortTokenClaimableFundingAmountPerSize == PositionNumbersShortTokenClaimableFundingAmountPerSize[key];
    require positionProps.numbers.increasedAtBlock == PositionNumbersIncreasedAtBlock[key];
    require positionProps.numbers.decreasedAtBlock == PositionNumbersDecreasedAtBlock[key];
}

function removePositionNumbers(bytes32 key) {
    sumOfShorts = PositionFlagsIsLong[key] ? sumOfShorts : sumOfShorts - PositionNumbersSizeInUsd[key];
    sumOfLongs = PositionFlagsIsLong[key] ? sumOfLongs - PositionNumbersSizeInTokens[key] : sumOfLongs;
    PositionNumbersSizeInUsd[key] = 0;
    PositionNumbersSizeInTokens[key] = 0;
    PositionNumbersCollateralAmount[key] = 0;
    PositionNumbersBorrowingFactor[key] = 0;
    PositionNumbersFundingFeeAmountPerSize[key] = 0;
    PositionNumbersLongTokenClaimableFundingAmountPerSize[key] = 0;
    PositionNumbersShortTokenClaimableFundingAmountPerSize[key] = 0;
    PositionNumbersIncreasedAtBlock[key] = 0;
    PositionNumbersDecreasedAtBlock[key] = 0;
}

// struct Flags {
//     bool isLong;
// }
ghost mapping(bytes32 => bool) PositionFlagsIsLong;

function setPositionFlags(bytes32 key, Position.Flags positionFlags) {
    PositionFlagsIsLong[key] = positionFlags.isLong;
}

function getPositionFlags(bytes32 key, Position.Props positionProps) {
    require positionProps.flags.isLong == PositionFlagsIsLong[key];
}

function setPosition(bytes32 key, Position.Props position) {
    setPositionFlags(key, position.flags);
    setPositionAddresses(key, position.addresses);
    setPositionNumbers(key, position.numbers);
} 

function getPosition(bytes32 key) returns Position.Props {
    Position.Props props;
    getPositionAddresses(key, props);
    getPositionNumbers(key, props);
    getPositionFlags(key, props);

    return props;
} 

function removePosition(bytes32 key) {
    removePositionAddresses(key);
    removePositionNumbers(key);
} 


ghost myWNT() returns address {
	init_state axiom myWNT() == wnt;
}

/***
GMX Property #1:
    if the price value is the same, no sequence of actions should result in a net profit, or another way to phrase it would be that markets should always be solvent if price does not change
***/
// this mirrors PositionUtils.validateNonEmptyPosition, but returns
// a bool rather than reverting if the position is empty
function isPositionEmpty(Position.Props position) returns bool {
    return position.numbers.sizeInUsd == 0 && position.numbers.sizeInTokens == 0 && position.numbers.collateralAmount == 0;
}

function closing_create_order_params_from_position(Position.Props position) returns BaseOrderUtils.CreateOrderParams {
    BaseOrderUtils.CreateOrderParams close_order_params;

    require close_order_params.orderType == Order.OrderType.MarketDecrease;

    // addresses
    require close_order_params.addresses.receiver == position.addresses.account;
    require close_order_params.addresses.market == position.addresses.market;
    require close_order_params.addresses.initialCollateralToken == position.addresses.collateralToken;

    // numbers
    // NOTE: price is underspecified here. This is currently
    // just used to show that it is possible to issue a close order.
    require close_order_params.numbers.sizeDeltaUsd == position.numbers.sizeInUsd;

    require close_order_params.isLong == position.flags.isLong;

    return close_order_params;
}

function positions_closable(env e, OracleUtils.SetPricesParams oracle_price_params, uint256 close_value) returns bool {
    address some_account;
    address some_market;
    address some_collateral_token;
    bool some_is_long;
    address dataStore;
    bytes32 some_position_key = positionKeyHarness.getPositionKey(e, some_account, some_market, some_collateral_token, some_is_long);
    Position.Props position = getPosition(some_position_key);

    // save whether or not the position is empty, but do NOT require it.
    // At the end of the rule, we require that if the position (any position),
    // is non-empty, then it must be possible to create and execute an order
    // that undoes it.
    bool non_empty_position = !isPositionEmpty(position);
    require non_empty_position;
    BaseOrderUtils.CreateOrderParams closing_order_params = closing_create_order_params_from_position(position);

    bytes32 closing_order_key = createOrder(e, some_account, closing_order_params); 
    executeOrder@withrevert(e, closing_order_key, oracle_price_params);
    bool executeOrderReverted = lastReverted;

    // Assuming the created order goes through, the close_value is the
    // value returned.
    // NOTE: There are two prices in CreateOrderParams -- triggerPrice and 
    // acceptablePrice. I am not exactly sure which one is right for this.
    // It could also be that the price used depends on whether it is long 
    // or short?
    // The argument close_value is used to track the value returned from
    // closing the position before and after an order is made.
    require close_value == assert_uint256(closing_order_params.numbers.sizeDeltaUsd * 
        closing_order_params.numbers.triggerPrice);

    // If the position is non-empty, it is possible to create and execute an
    // an order 
    // return non_empty_position => !createOrderReverted && !executeOrderReverted;
    return !executeOrderReverted;
}

// This is the original specification of GMX Requested Property 1
rule positions_can_be_closed {
    // A liveness property that all open positions can be closed, even
    // after arbitrary (potentially adversarial) user actions. More precisely,
    // for any public/external call, we prove an invariant that assuming
    // it was possible to close all open positions before the call, it is still
    // possible to close all open positions after the call.

    // A position is closed by issuing a decrease order (so that it is 
    // decreased to zero).

    env e;
    // This value is used to enforce that the value from closing a position
    // is the same before and after issuing the user command.
    uint256 position_close_value;

    // Used for both precond and postcond since we assume the
    // prices do not change
    OracleUtils.SetPricesParams oracle_price_params;

    // We need to save the state before positions_closable because
    // simulateExecuteOrder in positions_closable is state-changing.
    storage stateBeforePrecond = lastStorage;

    //========================================================================
    // Require: positions can be closed before executing the call
    //========================================================================
    require positions_closable(e, oracle_price_params, position_close_value);

    //========================================================================
    // Execute the call
    //========================================================================
    bytes32 key;
    OracleUtils.SetPricesParams oracleParams;
    executeOrder(e, key, oracleParams) at stateBeforePrecond;

    //========================================================================
    // Assert: positions can be closed after executing the call
    //========================================================================
    assert positions_closable(e, oracle_price_params, position_close_value);
}

/***
GMX Property #2:
    If the market has a long token that is the same as the index token and the reserveFactor is less than 1, 
    then the market should always be solvent regardless of the price of the index token

    note: reserveFactor is less than 1 - implies that all positions are backed by the order and deposit vault (the same way we defined solvency)
    we defined solvency as all open positions are backed by the contract's balances (both orderVault and depositVault).
***/
rule requireReserveFactorLessThanOneSolvency(method f) filtered {
    f -> f.selector != sig:simulateExecuteOrder(bytes32, OracleUtils.SimulatePricesParams).selector
}{
    env e;
    calldataarg args;

    address dataStore;
    Market.Props marketProps;
    MarketUtils.MarketPrices prices;
    bool long = true;
    bool short = false;

    require marketProps.longToken == DummyERC20Long;
    require marketProps.longToken == marketProps.indexToken;
    require marketProps.shortToken == DummyERC20Short;
    require marketProps.marketToken == MarketToken;

    require MarketUtils.getReservedUsdEx(dataStore, marketProps, prices, short) < 1;
    require MarketUtils.getReserveFactorEx(dataStore, MarketToken, long) < 1;

    mathint longReservses = DummyERC20Long.balanceOf(OrderVault) + DummyERC20Long.balanceOf(DepositVault);
    mathint shortReserves = DummyERC20Short.balanceOf(OrderVault) + DummyERC20Short.balanceOf(DepositVault);

    require require_uint256(longReservses) >= MarketUtils.getPoolAmountEx(dataStore, marketProps, DummyERC20Long);
    require require_uint256(shortReserves) >= MarketUtils.getPoolAmountEx(dataStore, marketProps, DummyERC20Short);

    require longReservses >= sumOfLongs;
    require shortReserves >= sumOfShorts;

    f(e, args);

    assert DummyERC20Long.balanceOf(OrderVault) + DummyERC20Long.balanceOf(DepositVault) >= sumOfLongs;
    assert DummyERC20Short.balanceOf(OrderVault) + DummyERC20Short.balanceOf(DepositVault) >= sumOfShorts;
}

/***
GMX Property #3:
    if the market has a long token that is not the same as the index token and the max pnl factor for traders is less than 1, 
    Then the market should always be solvent regardless of the price of the index token

    note:  max pnl factor for traders is less than 1 - implies that all positions can gain up to 100% profit of their initial position value. 
    no special requiremnt needed because we assume the protocol takes that into account when closing a position.

    we defined solvency as all open positions are backed by the contract's balances (both orderVault and depositVault).
***/
rule requireMaxPnlFactorLessThanOneSolvency(method f) filtered {
    f -> f.selector != sig:simulateExecuteOrder(bytes32, OracleUtils.SimulatePricesParams).selector
}{
    env e;
    calldataarg args;

    address dataStore;
    Market.Props marketProps;
    MarketUtils.MarketPrices prices;
    bool long = true;
    bool short = false;

    require marketProps.longToken == DummyERC20Long;
    require marketProps.longToken != marketProps.indexToken;
    require marketProps.shortToken == DummyERC20Short;
    require marketProps.marketToken == MarketToken;

    require MarketUtils.getMaxPnlFactorEx(dataStore, Keys.MAX_PNL_FACTOR_FOR_TRADERS(), MarketToken, long) < 1;
    require MarketUtils.getMaxPnlFactorEx(dataStore, Keys.MAX_PNL_FACTOR_FOR_TRADERS(), MarketToken, short) < 1;

    mathint longReservses = DummyERC20Long.balanceOf(OrderVault) + DummyERC20Long.balanceOf(DepositVault);
    mathint shortReserves = DummyERC20Short.balanceOf(OrderVault) + DummyERC20Short.balanceOf(DepositVault);

    // require solvency
    require longReservses >= sumOfLongs;
    require shortReserves >= sumOfShorts; // assumes short token is usdc (if not, need to mul by actual price).

    f(e, args);

    // assert solvency
    assert DummyERC20Long.balanceOf(OrderVault) + DummyERC20Long.balanceOf(DepositVault) >= sumOfLongs;
    assert DummyERC20Short.balanceOf(OrderVault) + DummyERC20Short.balanceOf(DepositVault) >= sumOfShorts;
}

/***
GMX Property #5:
    If price does not change, no sequence of actions should lead to a decrease in the market pool value, 
    all funding fees and protocol fees can be claimed and all market tokens can be redeemed.
    
    TODO: add assertion that all fees can be claimed.
***/
rule priceDontChangeNoDecreeseInPoolValue(method f) filtered {
    f -> f.selector != sig:simulateExecuteOrder(bytes32, OracleUtils.SimulatePricesParams).selector
}{
    env e;
    calldataarg args;

    address dataStore;
    address indexToken;
    Market.Props marketProps;
    MarketUtils.MarketPrices prices;
    bool maximize;

    require marketProps.longToken == DummyERC20Long;
    require marketProps.shortToken == DummyERC20Short;
    require marketProps.marketToken == MarketToken;
    require marketProps.indexToken == indexToken;

    // Fixed prices.
    Price.Props indexTokenPrice = Oracle.getPrimaryPrice(indexToken);
    Price.Props longTokenPrice = Oracle.getPrimaryPrice(DummyERC20Long);
    Price.Props shortTokenPrice = Oracle.getPrimaryPrice(DummyERC20Short);

    MarketPoolValueInfo.Props poolValuePropsBefore = MarketUtils.getPoolValueInfo(dataStore, marketProps, indexTokenPrice, longTokenPrice, shortTokenPrice, Keys.MAX_PNL_FACTOR_FOR_TRADERS(), maximize);
    int256 poolValueBefore = poolValuePropsBefore.poolValue;

    f(e, args);

    MarketPoolValueInfo.Props poolValuePropsAfter = MarketUtils.getPoolValueInfo(dataStore, marketProps, indexTokenPrice, longTokenPrice, shortTokenPrice, Keys.MAX_PNL_FACTOR_FOR_TRADERS(), maximize);
    int256 poolValueAfter = poolValuePropsAfter.poolValue;

    assert poolValueBefore >= poolValueAfter;
}


rule GMXMarketAlwaysSolventReserveFactor() { // the second property requested by GMX
    env e;
    address account;
    address market;
    // require market.longToken == market.indexToken;
    address uiFeeReceiver;
    address initialCollateralToken;

    uint256 sizeDeltaUsd;
    uint256 initialCollateralDeltaAmount;
    uint256 triggerPrice;
    uint256 acceptablePrice;
    uint256 executionFee;
    uint256 callbackGasLimit;
    uint256 minOutputAmount;

    BaseOrderUtils.CreateOrderParams params;    // for createOrder()
    OracleUtils.SetPricesParams oracleParams;   // for executeOrder()

    bytes32 key; // for the first createOrder()
    bytes32 key2; // for the second createOrder()

    require params.orderType == Order.OrderType.MarketDecrease;
    require params.decreasePositionSwapType == Order.DecreasePositionSwapType.NoSwap;

    require params.addresses.receiver == account;
    require params.addresses.callbackContract == 0;
    require params.addresses.uiFeeReceiver == uiFeeReceiver;
    require params.addresses.market == market;  // we have to verify in separate rule
                                                // no interference between markets
    require params.addresses.initialCollateralToken == initialCollateralToken;
    //require params.addresses.swapPath == [0]; // doesn't work

    require params.numbers.sizeDeltaUsd == sizeDeltaUsd;
    require params.numbers.initialCollateralDeltaAmount == initialCollateralDeltaAmount;
    require params.numbers.triggerPrice == triggerPrice;
    require params.numbers.acceptablePrice == acceptablePrice;
    require params.numbers.executionFee == executionFee;
    require params.numbers.callbackGasLimit == callbackGasLimit;
    require params.numbers.minOutputAmount == minOutputAmount;


    // require indexToken
    // require longToken
    // require reserveFactor < 1

    // Save this state
    storage initState = lastStorage;

    // create order (decrease order type) and get its key
    // execute the order with the key above - if it passed it means solvent
    key = createOrder(e, account, params);
    executeOrder(e, key, oracleParams);
    //assert false;

    

    // Go back to state above and create order (decrease order type) and get its key
    key2 = createOrder(e, account, params) at initState;

    // change oracle prices

    // execute the order with the key above - if it passed it means solvent    
    executeOrder@withrevert(e, key2, oracleParams);
    assert !lastReverted;

}

rule createOrderOnly() {
    env e;
    calldataarg args;
    createOrder(e, args);
    assert false;
}

rule updateOrderOnly() {
    env e; calldataarg args;
    //updateOrder(e, args);

    bytes32 key;
    uint256 sizeDeltaUsd;
    uint256 acceptablePrice;
    uint256 triggerPrice;
    uint256 minOutputAmount;
    Order.Props order;

    require order.addresses.account != 0;
    require order.addresses.receiver != 0;
    require order.addresses.callbackContract != 0;
    require order.addresses.uiFeeReceiver != 0;
    require order.addresses.market != 0;
    require order.addresses.initialCollateralToken != 0;
    //require order.addresses.swapPath == address [0]; //not working

    require order.numbers.orderType == Order.OrderType.MarketSwap; //MarketSwap; //not working
    //require order.numbers.decreasePositionSwapType == NoSwap; //not working
    require order.numbers.decreasePositionSwapType == Order.DecreasePositionSwapType.NoSwap;
    require order.numbers.sizeDeltaUsd != 0;
    require order.numbers.initialCollateralDeltaAmount != 0;
    require order.numbers.triggerPrice != 0;
    require order.numbers.acceptablePrice != 0;
    require order.numbers.executionFee != 0;
    require order.numbers.callbackGasLimit != 0;
    require order.numbers.minOutputAmount != 0;
    require order.numbers.updatedAtBlock != 0;

    require order.flags.isLong == false;
    require order.flags.shouldUnwrapNativeToken == false;
    require order.flags.isFrozen == false;

    updateOrder(e, key, sizeDeltaUsd, acceptablePrice, triggerPrice, minOutputAmount, order);
    assert false;
}

//-----------------------------------------------------------------------------
// Trading Integrity Rules
//-----------------------------------------------------------------------------
rule marketIncreaseOrderCorrect() {
    // save position value before calling executeOrder with IncreaseOrder
    // executeOrder
    // check that new position value is higher than old one

    env e;
    bytes32 orderKey;
    OracleUtils.SetPricesParams oracleParams;
    address keeper = e.msg.sender;
    uint256 startingGas;

    // This rule compares the position before and after an IncreaseOrder
    // call. Most of this code is used to get the position key to check this,
    // and the details of determining the key come from the implementation 
    // of IncreaseOrderUtils.processOrder (eventually called by executeOrder
    // when the type is MarketIncrease.


    // This instantiation of parameters follows the implementation of _executeOrder
    BaseOrderUtils.ExecuteOrderParams executeOrderParams = BaseOrderHandler.getExecuteOrderParams(
        e,
        orderKey,
        oracleParams,
        keeper, 
        startingGas,
        Order.SecondaryOrderType.None
    );

    require executeOrderParams.order.numbers.orderType == Order.OrderType.MarketIncrease;

    // In IncreaseOrderUtils.processOrder collateralToken is defined by 
    // SwapUtils.swap as the returned token value which is the same as the 
    // tokenIn from the input params which is defined as the following in
    // IncreaseOrderUtils.processOrder
    address collateralToken = executeOrderParams.order.addresses.initialCollateralToken;

    // this should be executeOrderParams.order.account(), similar for market, isLong
    address orderAccount = executeOrderParams.order.addresses.account;
    address orderMarket = executeOrderParams.order.addresses.market;
    bool orderIsLong = executeOrderParams.order.flags.isLong;

    bytes32 positionKey = positionKeyHarness.getPositionKey(e, orderAccount,
        orderMarket, collateralToken, orderIsLong);


    // PositionStoreUtils.get
    // first arg should be executeOrderParams.contracts.dataStore
    Position.Props positionBefore = getPosition(positionKey);

    executeOrder(e, orderKey, oracleParams);
    
    Position.Props positionAfter = getPosition(positionKey);

    // The position has really increased
    assert positionAfter.numbers.sizeInUsd >= positionBefore.numbers.sizeInUsd;
    assert positionAfter.numbers.sizeInTokens >= positionBefore.numbers.sizeInTokens;
}

//-----------------------------------------------------------------------------
// Sanity Rules
//-----------------------------------------------------------------------------
rule cancelOrderOnly() {
    env e;
    calldataarg args;
    cancelOrder(e, args);
    assert false;
}

rule simulateExecuteOrderOnly() {
    env e;
    calldataarg args;
    simulateExecuteOrder(e, args);
    assert false;
}

rule executeOrderOnly() {
    env e;
    calldataarg args;
    executeOrder(e, args);
    assert false;
}

rule _executeOrderOnly() {
    env e;
    calldataarg args;
    _executeOrder(e, args);
    assert false;
}


// Rule ideas:
// createOrder:
// 1. createOrder() should revert only if:
//    a. the order type is not allowed (FeatureUtils.validateFeature)
//    b. the account == 0
//    c. the params.orderType == Order.OrderType.Liquidation
//    d. initialCollateralDeltaAmount < params.numbers.executionFee
//    e. wntAmount < params.numbers.executionFee
//    f. market.marketToken != 0
//    g. isMarketDisabled == true
//    h. isSwapOnlyMarket (market.indexToken == address(0))
//    i. validateSwapPath: swapPath.length > maxSwapPathLength
//    j. any of the markets on the swapPath: market.marketToken == address(0)
//    k. the receiver == 0
//    l. callbackGasLimit > maxCallbackGasLimit
//    m. executionFee < minExecutionFee
//    n. order.sizeDeltaUsd() == 0 && order.initialCollateralDeltaAmount() == 0

// 2. The nonce bytes32 key = NonceUtils.getNextKey(dataStore);
//    is always increased by one after any type of order is created:
//    ADL, Deposit, Liquidation, Any order type, Withdrawal
//    this might be ***problematic*** as the returned key is hash of the nonce
//    bytes32 key = keccak256(abi.encode(address(dataStore), nonce));

// 3. On successful order creation/update its property (props.numbers.updatedAtBlock) is correctly updated:
//    props.setUpdatedAtBlock(Chain.currentBlockNumber());




// mental notes:
// - the referral code is set when calling the createOrder() and can be set to anything - who controls it?
// - storing of orders in the datastore is with OrderStoreUtils.sol and it uses hash of a key hash