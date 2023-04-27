methods {
    /// DataStore (to be dispatched only if the DataStore contract isn't linked to the harness Oracle)
    // function _.getUint(bytes32) external => DISPATCHER(true);
    // function _.getAddress(bytes32) external => DISPATCHER(true);
    // function _.getBytes32(bytes32) external => DISPATCHER(true);
    /// PriceFeed
    function _.latestRoundData() external => DISPATCHER(true);
    /// Array (temporary summarization)
    //function _.getMedian(uint256[] memory) internal library => NONDET;
    function _.getUncompactedValue(uint256[] memory, uint256, uint256, uint256, string memory) internal library => NONDET;
    /// Chain
    function _.arbBlockNumber() external => ghostBlockNumber() expect uint256 ALL;
    function _.arbBlockHash(uint256 blockNumber) external => ghostBlockHash(blockNumber) expect bytes32 ALL;
    /// Oracle summaries
    function OracleHarness._getSalt() internal returns bytes32 => mySalt();
    /// @notice : the following summary isn't applied (issue)
    //function OracleHarness._setPrices(address,address,address[] memory, OracleUtils.SetPricesParams memory) internal => NONDET;
}

ghost mySalt() returns bytes32;

ghost ghostBlockNumber() returns uint256 {
    axiom ghostBlockNumber() !=0;
}

ghost ghostBlockHash(uint256) returns bytes32 {
    axiom forall uint256 num1. forall uint256 num2. 
        num1 != num2 => ghostBlockHash(num1) != ghostBlockHash(num2);
}

rule complexityCheck(method f)
filtered{f-> f.selector != 0xdf026811} {
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

rule validateSignerConsistency() {
    env e1; env e2;
    require e1.msg.value == e2.msg.value;
    
    bytes32 salt1;
    bytes32 salt2;
    address signer1;
    address signer2;
    bytes signature;

    validateSignerHarness(e1, salt1, signature, signer1);
    validateSignerHarness@withrevert(e2, salt2, signature, signer2);

    assert (salt1 == salt2 && signer1 == signer2) => !lastReverted,
        "Revert characteristics of validateSigner are not consistent";

    assert ((salt1 != salt2 && signer1 == signer2) ||
        (salt1 == salt2 && signer1 != signer2)) => lastReverted,
        "Calling validateSigner twice cannot succeed with changing a single argument";

    assert (!lastReverted && salt1 == salt2) => (signer1 == signer2),
        "Same salt must imply same signer";
}