using DataStore as DS;
using KeysHarness as KH;
using MarketToken as MToken;
using WNT as WNT;
using DummyERC20A as DummyERC20;

methods {
    //AdlHandler
    //function _.updateAdlState(address,bool,OracleUtils.SetPricesParams calldata) internal => NONDET;
    //function executeAdl(address,address,address,bool,uint256,OracleUtils.SetPricesParams) external => NONDET;
    //function _.getUncompactedOracleBlockNumbers(uint256[] memory,uint256) internal => NONDET;
    //function _.updateAdlState(address,address,address,address,bool,uint256[] memory) internal => NONDET;
    
    //FeeHandler


    // DummyERC20
    function DummyERC20A.balanceOf(address) external returns (uint256) envfree;

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
    // function _.setBool(bytes32,bool) external => DISPATCHER(true);
    // function _.getBool(bytes32 key) external => DISPATCHER(true);
    // function _.getUint(bytes32) external => DISPATCHER(true);
    // function _.setUint(bytes32,uint256) external => DISPATCHER(true);
    // function _.addBytes32(bytes32,bytes32) external => DISPATCHER(true);
    // function _.setAddress(bytes32,address) external => DISPATCHER(true);
    // function _.setAddressArray(bytes32, address[]) external => DISPATCHER(true);
    // function _.incrementUint(bytes32,uint256) external => DISPATCHER(true);
    // function _.getAddress(bytes32) external => DISPATCHER(true);
    // function _.containsBytes32(bytes32,bytes32) external => DISPATCHER(true);

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


    //Oracle
    function _.getPrimaryPrice(address) external => NONDET;
    function _.setPrices(address,address,OracleUtils.SetPricesParams) external  => NONDET;
    function _.clearAllPrices() external  => NONDET;

    //RoleStore
    function _.hasRole(address,bytes32) external => DISPATCHER(true);
    function _.revokeRole(address,bytes32) external => DISPATCHER(true);
    function _.grantRole(address,bytes32) external => DISPATCHER(true);

    //ArbSys
    function _.arbBlockNumber() external => NONDET;
    function _.arbBlockHash(uint256) external => NONDET;

}

/*rule sanity(method f) {
    env e;
    calldataarg args;
    f(e, args);
    assert false;
}*/

rule claimFeesTest() {
    env e;
    calldataarg args;

    address[] markets;
    address[] tokens;

    require markets.length == 1;

    claimFees(e, markets, tokens);
    assert false;
}

//TODO: add solvency invariant that checks, that MarketToken and Markets contracts always have enough to pay fees.

rule claimFeesIntegrity() {
    env e;
    calldataarg args;

    address[] markets;
    address[] tokens;
    uint256 i;

    require markets.length == 1;
    require tokens[0] == DummyERC20;
    require tokens.length == markets.length;
    require markets[0] == MToken;

    bytes32 key = KH.claimableFeeAmountKey(e, markets[0], tokens[0]);
    address fee_receiver = DS.getAddress(e, KH.FEE_RECEIVER(e));
    address holding_address = DS.getAddress(e, KH.HOLDING_ADDRESS(e));
    mathint feeAmountBefore = DS.getUint(e, key);
    mathint balanceDummyBefore = DummyERC20.balanceOf(fee_receiver);
    mathint balanceDummyHoldingBefore = DummyERC20.balanceOf(holding_address);

    // require, that the balance is less tham maximum
    require feeAmountBefore + balanceDummyBefore + balanceDummyHoldingBefore < max_uint256;
    // get MarketToken address and require it different to the holding address
    require MToken != holding_address;

    claimFees(e, markets, tokens);

    mathint feeAmountAfter = DS.getUint(e, key);
    mathint balanceDummyAfter = DummyERC20.balanceOf(fee_receiver);
    mathint balanceDummyHoldingAfter = DummyERC20.balanceOf(holding_address);

    assert feeAmountAfter == 0;
    assert balanceDummyAfter == balanceDummyBefore + feeAmountBefore ||
           balanceDummyHoldingAfter == balanceDummyHoldingBefore + feeAmountBefore;
}
