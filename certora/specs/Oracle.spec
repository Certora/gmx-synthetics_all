methods {
    /// DataStore (to be dispatched only if the DataStore contract isn't linked to the harness Oracle)
    // function _.getUint(bytes32) external => DISPATCHER(true);
    // function _.getAddress(bytes32) external => DISPATCHER(true);
    // function _.getBytes32(bytes32) external => DISPATCHER(true);
    /// PriceFeed
    function _.latestRoundData() external => DISPATCHER(true);
    /// Array (temporary summarization)
    function _.getMedian(uint256[] memory) internal => NONDET;
    /// Chain
    function _.arbBlockNumber() external => ghostBlockNumber() expect uint256 ALL;
    function _.arbBlockHash(uint256 blockNumber) external => ghostBlockHash(blockNumber) expect bytes32 ALL;
    /// Oracle summaries
    function Oracle._getSalt() internal returns bytes32 => mySalt();
    /// @notice : the following summaries aren't applied (issue)
    //function OracleHarness._getPriceFeedPrice(address,address) internal returns (bool, uint256) => NONDET;
    //function OracleHarness._setPrices(address,address,address[] memory, OracleUtils.SetPricesParams memory) internal => NONDET;

    /// Getters:
    function OracleHarness.primaryPrices(address) external returns (uint256,uint256);
    function OracleHarness.secondaryPrices(address) external returns (uint256,uint256);
    function OracleHarness.customPrices(address) external returns (uint256,uint256);
    function OracleHarness.getSignerByInfo(uint256, uint256) external returns (address);
}

definition isSetPrices(method f) returns bool = f.selector == 0xdf026811;

ghost mySalt() returns bytes32;

ghost ghostBlockNumber() returns uint256 {
    axiom ghostBlockNumber() !=0;
}

ghost ghostBlockHash(uint256) returns bytes32 {
    axiom forall uint256 num1. forall uint256 num2. 
        num1 != num2 => ghostBlockHash(num1) != ghostBlockHash(num2);
}

function ghostMedian(uint256[] array) returns uint256 {
    uint256 med;
    uint256 len = array.length;
    require med >= array[0] && med <= array[require_uint256(len-1)];
    return med;
}

rule complexityCheck(method f)
filtered{f-> !isSetPrices(f)} {
    env e; 
    calldataarg args;
    f(e, args);

    assert false, "this assertion should fail";
}

rule setPricesComplexity() {
    env e; 
    calldataarg args;
    _setPrices(e, args);

    assert false, "this assertion should fail";
}

// rule validateSignerConsistency() {
//     env e1; env e2;
//     require e1.msg.value == e2.msg.value;
    
//     bytes32 salt1;
//     bytes32 salt2;
//     address signer1;
//     address signer2;
//     bytes signature;

//     validateSignerHarness(e1, salt1, signature, signer1);
//     validateSignerHarness@withrevert(e2, salt2, signature, signer2);

//     assert (salt1 == salt2 && signer1 == signer2) => !lastReverted,
//         "Revert characteristics of validateSigner are not consistent";

//     assert ((salt1 != salt2 && signer1 == signer2) ||
//         (salt1 == salt2 && signer1 != signer2)) => lastReverted,
//         "Calling validateSigner twice cannot succeed with changing a single argument";

//     assert (!lastReverted && salt1 == salt2) => (signer1 == signer2),
//         "Same salt must imply same signer";
// }