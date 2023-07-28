library GetPositionKeyHarness {

    // This mirrors getPositionKey in PositionUtils.sol, but is not internal.
    function getPositionKey(address account, address market, address collateralToken, bool isLong) public pure returns (bytes32) {
        bytes32 key = keccak256(abi.encode(account, market, collateralToken, isLong));
        return key;
    }
}