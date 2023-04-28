pragma solidity >=0.8.9;

contract Receiver {
    fallback() external payable { }

    bool randBoolReturn;
    function sendTo() external payable returns (bool) { return randBoolReturn; }

    receive() external payable { }
}