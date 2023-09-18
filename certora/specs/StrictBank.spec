// syncTokenBalance should not change the tokenBalances[token'] where token' != token
// _afterTransferOut should not change the tokenBalances[token'] where token' != token
// _recordTransferIn does not change any tokenBalances

// From Chandra:
// Bank
// 1. transferOut must increase the tokens for receiver by amount
// 2. something about native tokens but not sure I know why they are special
// 3. roles should be checked too

// From Chandra:
// StrictBank
// 5. TODO: roles should be checked too
// if something goes up, something else should go depositAndSendWrappedNativeToken
// valid changes.
// 

methods {
    function syncTokenBalance(address token) external returns (uint256);
    function tokenBalances(address token) external returns (uint256) envfree;
    function _afterTransferOutHarness(address token) external;
    function _recordTransferInHarness(address token) external returns (uint256) envfree;
}

// syncTokenBalance should not change the tokenBalances[token'] where token' != token
rule syncTokenBalance_doesnt_change_other_balances(address token, address otherToken) {
    env e;
    require(token != otherToken);

    uint256 before = tokenBalances(otherToken);
    syncTokenBalance(e, token);
    uint256 after = tokenBalances(otherToken);

    assert(before == after);

}

// _afterTransferOut should not change the tokenBalances[token'] where token' != token
// _afterTransferOut is internal, so there is a harness for it
rule afterTransferOut_doesnt_change_other_balances(address token, address otherToken) {
    env e;
    require(token != otherToken);

    uint256 before = tokenBalances(otherToken);
    _afterTransferOutHarness(e, token);
    uint256 after = tokenBalances(otherToken);

    assert(before == after);

}

// _recordTransferIn does not change any tokenBalances
// TODO: _recordTransferIn obviously changes tokenBalances[token], so I guess it should also be for token' != token?
// _recordTransferIn is internal, so there is a harness for it
rule recordTransferIn_doesnt_change_any_balance(address token, address otherToken) {
    env e;
    require(token != otherToken);

    uint256 before = tokenBalances(otherToken);
    _recordTransferInHarness(e, token);
    uint256 after = tokenBalances(otherToken);

    assert(before == after);

}