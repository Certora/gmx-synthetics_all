using WNT as wnt;
using DummyERC20A as DummyERC20Long;
using DummyERC20B as DummyERC20Short;
using OrderStoreUtils as OrderStoreUtils;
// using Position as Position;
using Order as Order;

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

    //OrderHandler - simulateExecuteOrder
    function _._executeOrder(bytes32,OracleUtils.SetPricesParams,address) external => NONDET;
    // Oracle.setPrimaryPrice => NONDET (see below)

    //OrderHandler - executeOrder
    function _.getExecutionGas(address,uint256) internal => NONDET;
    function _handleOrderError(bytes32,uint256,bytes memory) internal => NONDET;
    //function _.getUncompactedOracleBlockNumbers(uint256[] memory,uint256) internal => NONDET;
    function _.executeOrderFeatureDisabledKey(address,uint256) internal => NONDET;
    function _.getErrorSelectorFromData(bytes memory) internal => NONDET;
    function _.isOracleError(bytes4) internal => NONDET;
    function _.revertWithCustomError(bytes memory) internal => NONDET;
    //function _.getRevertMessage(bytes memory) internal => NONDET;


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

    // WNT
    function _.deposit()                             external  => DISPATCHER(true);
    function _.withdraw(uint256)                     external  => DISPATCHER(true);

    //Bank
    function _.transferOut(address,address,uint256,bool) external => DISPATCHER(true);
    function _.transferOut(address,address,uint256) external => DISPATCHER(true);

    //Datastore

    function _.getUint(bytes32 key) external => DISPATCHER(true);
    function _.setUint(bytes32 key, uint256 value) external => DISPATCHER(true);
    function _.removeUint(bytes32 key) external => DISPATCHER(true);
    function _.applyDeltaToUint(bytes32 key, int256 value, string) external => DISPATCHER(true);
    function _.applyDeltaToUint(bytes32 key, uint256 value) external => DISPATCHER(true);
    function _.applyBoundedDeltaToUint(bytes32 key, int256 value) external => DISPATCHER(true);
    function _.incrementUint(bytes32 key, uint256 value) external => DISPATCHER(true);
    function _.decrementUint(bytes32 key, uint256 value) external => DISPATCHER(true);
    function _.getInt(bytes32 key) external => DISPATCHER(true);
    function _.setInt(bytes32 key, int256 value) external => DISPATCHER(true);
    function _.removeInt(bytes32 key) external => DISPATCHER(true);
    function _.applyDeltaToInt(bytes32 key, int256 value) external => DISPATCHER(true);
    function _.incrementInt(bytes32 key, int256 value) external => DISPATCHER(true);
    function _.decrementInt(bytes32 key, int256 value) external => DISPATCHER(true);
    function _.getAddress(bytes32 key) external => DISPATCHER(true);
    function _.setAddress(bytes32 key, address value) external => DISPATCHER(true);
    function _.removeAddress(bytes32 key) external => DISPATCHER(true);
    function _.getBool(bytes32 key) external => DISPATCHER(true);
    function _.setBool(bytes32 key, bool value) external => DISPATCHER(true);
    function _.removeBool(bytes32 key) external => DISPATCHER(true);
    function _.getString(bytes32 key) external => DISPATCHER(true);
    function _.setString(bytes32 key, string) external => DISPATCHER(true);
    function _.removeString(bytes32 key) external => DISPATCHER(true);
    function _.getBytes32(bytes32 key) external => DISPATCHER(true);
    function _.setBytes32(bytes32 key, bytes32 value) external => DISPATCHER(true);
    function _.removeBytes32(bytes32 key) external => DISPATCHER(true);
    function _.getUintArray(bytes32 key) external => DISPATCHER(true);
    function _.setUintArray(bytes32 key, uint256[]) external => DISPATCHER(true);
    function _.removeUintArray(bytes32 key) external => DISPATCHER(true);
    function _.getIntArray(bytes32 key) external => DISPATCHER(true);
    function _.setIntArray(bytes32 key, int256[]) external => DISPATCHER(true);
    function _.removeIntArray(bytes32 key) external => DISPATCHER(true);
    function _.getAddressArray(bytes32 key) external => DISPATCHER(true);
    function _.setAddressArray(bytes32 key, address[]) external => DISPATCHER(true);
    function _.removeAddressArray(bytes32 key) external => DISPATCHER(true);
    function _.getBoolArray(bytes32 key) external => DISPATCHER(true);
    function _.setBoolArray(bytes32 key, bool[]) external => DISPATCHER(true);
    function _.removeBoolArray(bytes32 key) external => DISPATCHER(true);
    function _.getStringArray(bytes32 key) external => DISPATCHER(true);
    function _.setStringArray(bytes32 key, string[]) external => DISPATCHER(true);
    function _.removeStringArray(bytes32 key) external => DISPATCHER(true);
    function _.getBytes32Array(bytes32 key) external => DISPATCHER(true);
    function _.setBytes32Array(bytes32 key, bytes32[]) external => DISPATCHER(true);
    function _.removeBytes32Array(bytes32 key) external => DISPATCHER(true);
    function _.containsBytes32(bytes32 setKey, bytes32 value) external => DISPATCHER(true);
    function _.getBytes32Count(bytes32 setKey) external => DISPATCHER(true);
    function _.getBytes32ValuesAt(bytes32 setKey, uint256 start, uint256 end) external => DISPATCHER(true);
    function _.addBytes32(bytes32 setKey, bytes32 value) external => DISPATCHER(true);
    function _.removeBytes32(bytes32 setKey, bytes32 value) external => DISPATCHER(true);
    function _.containsAddress(bytes32 setKey, address value) external => DISPATCHER(true);
    function _.getAddressCount(bytes32 setKey) external => DISPATCHER(true);
    function _.getAddressValuesAt(bytes32 setKey, uint256 start, uint256 end) external => DISPATCHER(true);
    function _.addAddress(bytes32 setKey, address value) external => DISPATCHER(true);
    function _.removeAddress(bytes32 setKey, address value) external => DISPATCHER(true);
    function _.containsUint(bytes32 setKey, uint256 value) external => DISPATCHER(true);
    function _.getUintCount(bytes32 setKey) external => DISPATCHER(true);
    function _.getUintValuesAt(bytes32 setKey, uint256 start, uint256 end) external => DISPATCHER(true);
    function _.addUint(bytes32 setKey, uint256 value) external => DISPATCHER(true);
    function _.removeUint(bytes32 setKey, uint256 value) external => DISPATCHER(true);



    // function _.getUint(bytes32 key) external => NONDET;
    // function _.setUint(bytes32 key, uint256 value) external => NONDET;
    // function _.removeUint(bytes32 key) external => NONDET;
    // function _.applyDeltaToUint(bytes32 key, int256 value, string) external => NONDET;
    // function _.applyDeltaToUint(bytes32 key, uint256 value) external => NONDET;
    // function _.applyBoundedDeltaToUint(bytes32 key, int256 value) external => NONDET;
    // function _.incrementUint(bytes32 key, uint256 value) external => NONDET;
    // function _.decrementUint(bytes32 key, uint256 value) external => NONDET;
    // function _.getInt(bytes32 key) external => NONDET;
    // function _.setInt(bytes32 key, int256 value) external => NONDET;
    // function _.removeInt(bytes32 key) external => NONDET;
    // function _.applyDeltaToInt(bytes32 key, int256 value) external => NONDET;
    // function _.incrementInt(bytes32 key, int256 value) external => NONDET;
    // function _.decrementInt(bytes32 key, int256 value) external => NONDET;
    // function _.getAddress(bytes32 key) external => NONDET;
    // function _.setAddress(bytes32 key, address value) external => NONDET;
    // function _.removeAddress(bytes32 key) external => NONDET;
    // function _.getBool(bytes32 key) external => NONDET;
    // function _.setBool(bytes32 key, bool value) external => NONDET;
    // function _.removeBool(bytes32 key) external => NONDET;
    // function _.getString(bytes32 key) external => NONDET;
    // function _.setString(bytes32 key, string) external => NONDET;
    // function _.removeString(bytes32 key) external => NONDET;
    // function _.getBytes32(bytes32 key) external => NONDET;
    // function _.setBytes32(bytes32 key, bytes32 value) external => NONDET;
    // function _.removeBytes32(bytes32 key) external => NONDET;
    // function _.getUintArray(bytes32 key) external => NONDET;
    // function _.setUintArray(bytes32 key, uint256[]) external => NONDET;
    // function _.removeUintArray(bytes32 key) external => NONDET;
    // function _.getIntArray(bytes32 key) external => NONDET;
    // function _.setIntArray(bytes32 key, int256[]) external => NONDET;
    // function _.removeIntArray(bytes32 key) external => NONDET;
    // function _.getAddressArray(bytes32 key) external => NONDET;
    // function _.setAddressArray(bytes32 key, address[]) external => NONDET;
    // function _.removeAddressArray(bytes32 key) external => NONDET;
    // function _.getBoolArray(bytes32 key) external => NONDET;
    // function _.setBoolArray(bytes32 key, bool[]) external => NONDET;
    // function _.removeBoolArray(bytes32 key) external => NONDET;
    // function _.getStringArray(bytes32 key) external => NONDET;
    // function _.setStringArray(bytes32 key, string[]) external => NONDET;
    // function _.removeStringArray(bytes32 key) external => NONDET;
    // function _.getBytes32Array(bytes32 key) external => NONDET;
    // function _.setBytes32Array(bytes32 key, bytes32[]) external => NONDET;
    // function _.removeBytes32Array(bytes32 key) external => NONDET;
    // function _.containsBytes32(bytes32 setKey, bytes32 value) external => NONDET;
    // function _.getBytes32Count(bytes32 setKey) external => NONDET;
    // function _.getBytes32ValuesAt(bytes32 setKey, uint256 start, uint256 end) external => NONDET;
    // function _.addBytes32(bytes32 setKey, bytes32 value) external => NONDET;
    // function _.removeBytes32(bytes32 setKey, bytes32 value) external => NONDET;
    // function _.containsAddress(bytes32 setKey, address value) external => NONDET;
    // function _.getAddressCount(bytes32 setKey) external => NONDET;
    // function _.getAddressValuesAt(bytes32 setKey, uint256 start, uint256 end) external => NONDET;
    // function _.addAddress(bytes32 setKey, address value) external => NONDET;
    // function _.removeAddress(bytes32 setKey, address value) external => NONDET;
    // function _.containsUint(bytes32 setKey, uint256 value) external => NONDET;
    // function _.getUintCount(bytes32 setKey) external => NONDET;
    // function _.getUintValuesAt(bytes32 setKey, uint256 start, uint256 end) external => NONDET;
    // function _.addUint(bytes32 setKey, uint256 value) external => NONDET;
    // function _.removeUint(bytes32 setKey, uint256 value) external => NONDET;



    //Oracle
    function _.getPrimaryPrice(address) external => NONDET;
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

    //MarketStoreUtils
    // function _.get(address, address) external => NONDET;

    //StrictBank
    function _.recordTransferIn(address) external => NONDET;

    //DepositStoreUtils
    // function _.set(address,bytes32,Deposit.Props) external => NONDET;

    // OrderStoreUtils.sol
    function OrderStoreUtils.get(address dataStore, bytes32 key) external returns (Order.Props memory) optional => getOrder(key);
    function OrderStoreUtils.set(address dataStore, bytes32 key, Order.Props memory order) external optional => setOrder(key, order);
    function OrderStoreUtils.remove(address dataStore, bytes32 key, address account) external optional => removeOrder(key);

    // PositionStoreUtils.sol
    // function PositionStoreUtils.get(address, bytes32 key) external returns (Position.Props memory) => getPosition(key);
    // function PositionStoreUtils.set(address, bytes32 key, Position.Props position) external => setPosition(key, position);

    // PositionUtils.sol
    // PositionUtils.getPositionKey

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

function setPositionNumbers(bytes32 key, Position.Numbers positionNumbers) {
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

function getPositionNumbers(bytes32 key, Position.Props positionProps) {
    require positionProps.flags.isLong == PositionFlagsIsLong[key];
}

function setPosition(bytes32 key, Position.Props position) {
    setPositionAddresses(key, position.addresses);
    setPositionNumbers(key, position.numbers);
    setPositionFlags(key, position.flags);
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

/*rule sanity(method f) {
    env e;
    calldataarg args;
    f(e, args);
    assert false;
}*/

/*rule claimFeesTest() {
    env e;
    calldataarg args;

    address[] markets;
    address[] tokens;

    require markets.length == 1;

    claimFees(e, markets, tokens);
    assert false;
}*/

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