pragma solidity ^0.8.0;

contract KeysHarness {
    function orderList() public view returns (bytes32) {
        return keccak256(abi.encode("ORDER_LIST"));
    }
}