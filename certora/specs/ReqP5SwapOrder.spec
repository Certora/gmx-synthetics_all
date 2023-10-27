using SwapOrderUtilsHarness as swapOrderUtils;
using GetPositionKeyHarness as positionKeyHarness;
using PositionStoreUtils as PositionStoreUtils;

// For GMX Req Property 5
using DummyERC20A as DummyERC20Long;
using DummyERC20B as DummyERC20Short;
using MarketToken as MarketToken;
using Oracle as Oracle;
using MarketUtilsHarness as marketUtils;
using Keys as Keys;

methods {
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


    // PositionUtils
    // function PositionUtils.getPositionKey(address account, address market, address collateralToken, bool isLong) internal returns (bytes32) => NONDET;
    // PositionUtils.UpdatePositionParams TODO

    // PositionStoreUtils.sol
    function PositionStoreUtils.get(address dataStore, bytes32 key) external returns (Position.Props) optional => getPosition(key);
    function PositionStoreUtils.set(address dataStore, bytes32 key, Position.Props position) external optional => setPosition(key, position);

    // DecreasePositionUtils
    // function DecreasePositionUtils.decreasePosition(
    //     PositionUtils.UpdatePositionParams params
    // ) external returns (DecreasePositionUtils.DecreasePositionResult) => NONDET;

    // SwapUtils
    // function SwapUtils.swap(SwapUtils.SwapParams params) external returns (address, uint256) => NONDET;

    //--------------------------------------------------------------------------
    // For Requested Property 5
    //--------------------------------------------------------------------------
    // Oracle
    function Oracle.getPrimaryPrice(address) external returns (Price.Props memory) envfree;
    function _.setPrices(address,address,OracleUtils.SetPricesParams) external => NONDET;
    function _.clearAllPrices() external => NONDET;
    function _.setPrimaryPrice(address,Price.Props) external => NONDET;

    // Keys.sol
    function Keys.MAX_PNL_FACTOR_FOR_TRADERS() external returns (bytes32) envfree;

    // MarketUtils
    function _.getPoolValueInfo(address, Market.Props, Price.Props, Price.Props, Price.Props, bytes32, bool) external optional => DISPATCHER(true);
}

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

rule priceDontChangeNoDecreeseInPoolValue {
    env e;
    calldataarg args;

    address dataStore;
    address indexToken;
    Market.Props marketProps;
    MarketUtils.MarketPrices prices;
    bool maximize;
    
    BaseOrderUtils.ExecuteOrderParams executeOrderParams;

    require marketProps.longToken == DummyERC20Long;
    require marketProps.shortToken == DummyERC20Short;
    require marketProps.marketToken == MarketToken;
    require marketProps.indexToken == indexToken;

    // Fixed prices.
    Price.Props indexTokenPrice = Oracle.getPrimaryPrice(indexToken);
    Price.Props longTokenPrice = Oracle.getPrimaryPrice(DummyERC20Long);
    Price.Props shortTokenPrice = Oracle.getPrimaryPrice(DummyERC20Short);

    MarketPoolValueInfo.Props poolValuePropsBefore = marketUtils.getPoolValueInfo(e, dataStore, marketProps, indexTokenPrice, longTokenPrice, shortTokenPrice, Keys.MAX_PNL_FACTOR_FOR_TRADERS(), maximize);
    int256 poolValueBefore = poolValuePropsBefore.poolValue;

    swapOrderUtils.processOrder(e, executeOrderParams);

    MarketPoolValueInfo.Props poolValuePropsAfter = marketUtils.getPoolValueInfo(e, dataStore, marketProps, indexTokenPrice, longTokenPrice, shortTokenPrice, Keys.MAX_PNL_FACTOR_FOR_TRADERS(), maximize);
    int256 poolValueAfter = poolValuePropsAfter.poolValue;

    assert poolValueBefore >= poolValueAfter;
}

rule priceDontChangeNoDecreeseInPoolValue_satisfy_not {
    env e;
    calldataarg args;

    address dataStore;
    address indexToken;
    Market.Props marketProps;
    MarketUtils.MarketPrices prices;
    bool maximize;
    
    BaseOrderUtils.ExecuteOrderParams executeOrderParams;

    require marketProps.longToken == DummyERC20Long;
    require marketProps.shortToken == DummyERC20Short;
    require marketProps.marketToken == MarketToken;
    require marketProps.indexToken == indexToken;

    // Fixed prices.
    Price.Props indexTokenPrice = Oracle.getPrimaryPrice(indexToken);
    Price.Props longTokenPrice = Oracle.getPrimaryPrice(DummyERC20Long);
    Price.Props shortTokenPrice = Oracle.getPrimaryPrice(DummyERC20Short);

    MarketPoolValueInfo.Props poolValuePropsBefore = marketUtils.getPoolValueInfo(e, dataStore, marketProps, indexTokenPrice, longTokenPrice, shortTokenPrice, Keys.MAX_PNL_FACTOR_FOR_TRADERS(), maximize);
    int256 poolValueBefore = poolValuePropsBefore.poolValue;

    swapOrderUtils.processOrder(e, executeOrderParams);

    MarketPoolValueInfo.Props poolValuePropsAfter = marketUtils.getPoolValueInfo(e, dataStore, marketProps, indexTokenPrice, longTokenPrice, shortTokenPrice, Keys.MAX_PNL_FACTOR_FOR_TRADERS(), maximize);
    int256 poolValueAfter = poolValuePropsAfter.poolValue;

    satisfy !(poolValueBefore >= poolValueAfter);
}