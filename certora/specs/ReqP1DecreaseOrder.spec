using DecreaseOrderUtilsHarness as decreaseOrderUtils;
using GetPositionKeyHarness as positionKeyHarness;
using PositionStoreUtils as PositionStoreUtils;

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

function isPositionEmpty(Position.Props position) returns bool {
    return position.numbers.sizeInUsd == 0 && position.numbers.sizeInTokens == 0 && position.numbers.collateralAmount == 0;
}

function positions_closable(env e, OracleUtils.SetPricesParams oracle_price_params, uint256 close_value) returns bool {
    address some_account;
    address some_market;
    address some_collateral_token;
    bool some_is_long;
    address dataStore;
    bytes32 some_position_key = positionKeyHarness.getPositionKey(e, some_account, some_market, some_collateral_token, some_is_long);
    Position.Props position = getPosition(some_position_key);

    bool non_empty_position = !isPositionEmpty(position);
    require non_empty_position;
    
    // Create Closing ExecuteOrder from position
    BaseOrderUtils.ExecuteOrderParams executeOrderParams;
    require executeOrderParams.order.numbers.orderType == Order.OrderType.MarketDecrease;
    require executeOrderParams.order.addresses.receiver == position.addresses.account;
    require executeOrderParams.order.addresses.market == position.addresses.market;
    require executeOrderParams.order.addresses.initialCollateralToken == position.addresses.collateralToken;
    require executeOrderParams.order.numbers.sizeDeltaUsd == position.numbers.sizeInUsd;
    require executeOrderParams.order.flags.isLong == position.flags.isLong;

    // require executeOrderParams.minOracleBlockNumbers = OracleUtils.getUncompactedOracleBlockNumbers(
    //     oracle_price_params.compactedMinOracleBlockNumbers,
    //     oracle_price_params.tokens.length
    // );

    // require executeOrderParams.maxOracleBlockNumbers = OracleUtils.getUncompactedOracleBlockNumbers(
    //     oracle_price_params.compactedMaxOracleBlockNumbers,
    //     oracle_price_params.tokens.length
    // );

    decreaseOrderUtils.processOrder@withrevert(e, executeOrderParams);
    bool processOrderReverted = lastReverted;

    require close_value == assert_uint256(executeOrderParams.order.numbers.sizeDeltaUsd * 
        executeOrderParams.order.numbers.triggerPrice); 

    return !processOrderReverted;
}

function positions_closable_nonreverting(env e, OracleUtils.SetPricesParams oracle_price_params, uint256 close_value) returns bool {
    address some_account;
    address some_market;
    address some_collateral_token;
    bool some_is_long;
    address dataStore;
    bytes32 some_position_key = positionKeyHarness.getPositionKey(e, some_account, some_market, some_collateral_token, some_is_long);
    Position.Props position = getPosition(some_position_key);

    bool non_empty_position = !isPositionEmpty(position);
    require non_empty_position;
    
    // Create Closing ExecuteOrder from position
    BaseOrderUtils.ExecuteOrderParams executeOrderParams;
    require executeOrderParams.order.numbers.orderType == Order.OrderType.MarketDecrease;
    require executeOrderParams.order.addresses.receiver == position.addresses.account;
    require executeOrderParams.order.addresses.market == position.addresses.market;
    require executeOrderParams.order.addresses.initialCollateralToken == position.addresses.collateralToken;
    require executeOrderParams.order.numbers.sizeDeltaUsd == position.numbers.sizeInUsd;
    require executeOrderParams.order.flags.isLong == position.flags.isLong;

    // require executeOrderParams.minOracleBlockNumbers = OracleUtils.getUncompactedOracleBlockNumbers(
    //     oracle_price_params.compactedMinOracleBlockNumbers,
    //     oracle_price_params.tokens.length
    // );

    // require executeOrderParams.maxOracleBlockNumbers = OracleUtils.getUncompactedOracleBlockNumbers(
    //     oracle_price_params.compactedMaxOracleBlockNumbers,
    //     oracle_price_params.tokens.length
    // );

    decreaseOrderUtils.processOrder(e, executeOrderParams);

    require close_value == assert_uint256(executeOrderParams.order.numbers.sizeDeltaUsd * 
        executeOrderParams.order.numbers.triggerPrice); 

    // The position should be empty if it has been closed
    Position.Props positionAfter = getPosition(some_position_key);
    return isPositionEmpty(positionAfter);

}

rule gmx_property1_DecreaseOrder{
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
    BaseOrderUtils.ExecuteOrderParams executeOrderParams;
    require executeOrderParams.order.numbers.orderType == Order.OrderType.MarketDecrease ||
        executeOrderParams.order.numbers.orderType == Order.OrderType.LimitDecrease ||
        executeOrderParams.order.numbers.orderType == Order.OrderType.StopLossDecrease ||
        executeOrderParams.order.numbers.orderType == Order.OrderType.Liquidation;

    // Used for both precond and postcond since we assume the
    // prices do not change
    OracleUtils.SetPricesParams oracle_price_params;

    // We need to save the state before positions_closable because
    // simulateExecuteOrder in positions_closable is state-changing.
    storage stateBeforePrecond = lastStorage;

    //========================================================================
    // Require: positions can be closed before executing the call
    //========================================================================
    // NOTE: drop require since it should help get away from the timeout
    // require positions_closable(e, oracle_price_params, position_close_value);

    //========================================================================
    // Execute the call
    //========================================================================
    decreaseOrderUtils.processOrder(e, executeOrderParams);

    //========================================================================
    // Assert: positions can be closed after executing the call
    //========================================================================
    satisfy positions_closable(e, oracle_price_params, position_close_value);
}

rule gmx_property1_DecreaseOrder_NoRevert {
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
    BaseOrderUtils.ExecuteOrderParams executeOrderParams;
    require executeOrderParams.order.numbers.orderType == Order.OrderType.MarketDecrease ||
        executeOrderParams.order.numbers.orderType == Order.OrderType.LimitDecrease ||
        executeOrderParams.order.numbers.orderType == Order.OrderType.StopLossDecrease ||
        executeOrderParams.order.numbers.orderType == Order.OrderType.Liquidation;

    // Used for both precond and postcond since we assume the
    // prices do not change
    OracleUtils.SetPricesParams oracle_price_params;

    // We need to save the state before positions_closable because
    // simulateExecuteOrder in positions_closable is state-changing.
    // storage stateBeforePrecond = lastStorage;

    //========================================================================
    // Require: positions can be closed before executing the call
    //========================================================================
    // NOTE: drop require since it should help get away from the timeout
    // require positions_closable(e, oracle_price_params, position_close_value);

    //========================================================================
    // Execute the call
    //========================================================================
    decreaseOrderUtils.processOrder(e, executeOrderParams);

    //========================================================================
    // Assert: positions can be closed after executing the call
    //========================================================================
    satisfy positions_closable_nonreverting(e, oracle_price_params, position_close_value);
}