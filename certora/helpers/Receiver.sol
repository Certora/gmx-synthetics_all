pragma solidity >=0.8.9;

contract Receiver {
    fallback() external payable { }

    bool randBoolReturn;
    function sendTo() external payable returns (bool) { return randBoolReturn; }

    bool randBool;
    bytes randBytes;
    function sendToDoubleReturn() external payable returns (bool, bytes memory) {
        return (randBool, randBytes);
    }

    function getRandBytes() external view returns (bytes memory) {
        return randBytes;
    }

    receive() external payable { }
}
