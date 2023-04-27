
methods {
    /// DataStore
    // function _.getUint(bytes32) external => DISPATCHER(true);
    //function _.getAddress(bytes32) external => DISPATCHER(true);
    //function _.getBytes32(bytes32) external => DISPATCHER(true);
    /// PriceFeed
    function _.latestRoundData() external => DISPATCHER(true);
    /// Array
    function _.getMedian(uint256[] memory) internal library => ALWAYS(2);
    function _.getUncompactedValue(uint256[] memory, uint256, uint256, uint256, string memory) internal library => NONDET;
    /// Chain
    function _.arbBlockNumber() external => ghostBlockNumber() expect uint256 ALL;
    function _.arbBlockHash(uint256 blockNumber) external => ghostBlockHash(blockNumber) expect bytes32 ALL;
    /// 
    // function Oracle._setPrices(address, address, address[] memory, OracleUtils.SetPricesParams memory) internal => NONDET;
}

ghost ghostBlockNumber() returns uint256 {
    axiom ghostBlockNumber() !=0;
}

ghost ghostBlockHash(uint256) returns bytes32 {
    axiom forall uint256 num1. forall uint256 num2. 
        num1 != num2 => ghostBlockHash(num1) != ghostBlockHash(num2);
}

rule complexity_check(method f) {
    env e; 
    calldataarg args;
    f(e, args);

    assert false, "this assertion should fail";
}

rule setPricesComplexity() {
    env e; 
    calldataarg args;
    setPrices(e, args);

    assert false, "this assertion should fail";
}