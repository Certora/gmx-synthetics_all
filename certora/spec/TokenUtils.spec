using DummyERC20B as erc20Token;
using DataStore as dataStore;
using DummyWeth as wnt;

methods {
    function wntFn(address) external returns (address) envfree;
    function transferFn(address, address, address, uint256) external envfree;
    function depositAndSendWrappedNativeTokenFn(address, address, uint256) external envfree;
    function withdrawAndSendNativeTokenFn(address, address, address, uint256) external envfree;
    function nonRevertingTransferWithGasLimitFn(address, address, uint256, uint256) external returns (bool, bytes memory) envfree;

    // DataStore.sol
    function _.getAddress(bytes32) external => DISPATCHER(true);
    function _.getUint(bytes32) external => DISPATCHER(true);
    function DataStore.getAddress(bytes32) external returns (address) envfree;

    // IWNT.sol
    function _.withdraw(uint256) external => DISPATCHER(true);
    function _.deposit() external => DISPATCHER(true);
    function DummyWeth.balanceOf(address) external returns (uint256) envfree;

    // Receiver.sol
    function _.sendTo() external => DISPATCHER(true);
    function _.sendToDoubleReturn() external => DISPATCHER(true);
    function _.getRandBytes() external => DISPATCHER(true);

    // Keys.sol
    function getHoldingAddress(address) external returns (address) envfree;

    // ERC20:
    function _.transfer(address,uint256) external => DISPATCHER(true);
    function DummyERC20B.totalSupply() external returns (uint256) envfree;
    function DummyERC20B.balanceOf(address) external returns (uint256) envfree;
}

// contracts balance should decrease by amount
rule integrityOfTransfer(address receiver, uint256 amount) {
    address holdingAddress = getHoldingAddress(dataStore);
    require receiver != currentContract;
    // require DataStore.getAddress(Keys.HOLDING_ADDRESS()) == dataStore;

    mathint receiverBalanceBefore = erc20Token.balanceOf(receiver);
    mathint currentContractBalanceBefore = erc20Token.balanceOf(currentContract);
    mathint holdingAddressBalanceBefore = erc20Token.balanceOf(holdingAddress);

    transferFn(dataStore, erc20Token, receiver, amount);

    mathint receiverBalanceAfter = erc20Token.balanceOf(receiver);
    mathint currentContractBalanceAfter = erc20Token.balanceOf(currentContract);
    mathint holdingAddressBalanceAfter = erc20Token.balanceOf(holdingAddress);

    assert (holdingAddressBalanceAfter == holdingAddressBalanceBefore + amount) || (receiverBalanceAfter == receiverBalanceBefore + amount);
    assert currentContractBalanceAfter == currentContractBalanceBefore - amount;
}

rule integrityOfDepositAndSendWrappedNativeToken(address receiver, uint256 amount) {
    address holdingAddress = getHoldingAddress(dataStore);
    require receiver != currentContract;

    mathint receiverBalanceBefore = wnt.balanceOf(receiver);
    mathint currentContractBalanceBefore = wnt.balanceOf(currentContract);
    mathint holdingAddressBalanceBefore = wnt.balanceOf(holdingAddress);

    depositAndSendWrappedNativeTokenFn(dataStore, receiver, amount);

    mathint receiverBalanceAfter = wnt.balanceOf(receiver);
    mathint currentContractBalanceAfter = wnt.balanceOf(currentContract);
    mathint holdingAddressBalanceAfter = wnt.balanceOf(holdingAddress);

    assert (holdingAddressBalanceAfter == holdingAddressBalanceBefore + amount) || (receiverBalanceAfter == receiverBalanceBefore + amount);
    // assert currentContractBalanceAfter == currentContractBalanceBefore - amount;
}

rule integrityOfNonRevertingTransfer(address to, uint256 amount) {
    require to != currentContract;
    address holdingAddress;

    mathint toBalanceBefore = erc20Token.balanceOf(to);
    mathint currentContractBalanceBefore = erc20Token.balanceOf(currentContract);

    uint256 gasLimit = 0; // commented out at source code (low-level call havocing).
    bool success;
    bytes res;

    success, res = nonRevertingTransferWithGasLimitFn(erc20Token, to, amount, gasLimit);

    mathint toBalanceAfter = erc20Token.balanceOf(to);
    mathint currentContractBalanceAfter = erc20Token.balanceOf(currentContract);

    assert success => toBalanceAfter == toBalanceBefore + amount;
    assert success => currentContractBalanceAfter == currentContractBalanceBefore - amount;
}

rule nonRevertingTransferDontChangeOther(address to, address other, uint256 amount) {
    require to != currentContract;
    require to != other;
    require other != currentContract;

    mathint otherBalanceBefore = erc20Token.balanceOf(other);

    uint256 gasLimit = 0; // commented out at source code (low-level call havocing).
    bool success;
    bytes res;

    success, res = nonRevertingTransferWithGasLimitFn(erc20Token, to, amount, gasLimit);

    mathint otherBalanceAfter = erc20Token.balanceOf(other);

    assert otherBalanceBefore == otherBalanceAfter;
}

// rule sanity(method f)
// {
// 	env e;
// 	calldataarg arg;
// 	f(e, arg);
// 	assert false;
// }
