rule sanity(method f) {
    env e;
    calldataarg args;
    f(e, args);
    assert false;
}


// StrictBank
// 5. TODO: roles should be checked too

// These are all state changing properties
// if something goes up, something else should go depositAndSendWrappedNativeToken
// valid changes.
// 

// 1. syncTokenBalance should not change the tokenBalances[token'] where token' != token
rule syncTokenBalance_changes_no_other_balance(address token) {
    env e;
    address other;
    uint256 other_before_balance = tokenBalances(e, other);
    syncTokenBalance(e, token);
    uint256 other_after_balance = tokenBalances(e, other); 
    assert (other != token => other_after_balance == other_before_balance);
} 


// 2. _recordTransferIn does not change then tokenBalances[token'] where token' != token
// 3. _recordTransferIn also sets tokenBalances[token] to balanceOf(this)
rule _recordTransferIn_changes_no_other_balance(address token) {
    env e;
    address other;
    uint256 other_before_balance = tokenBalances(e, other);
    recordTransferIn(e, token);
    uint256 other_after_balance = tokenBalances(e, other); 
    assert (other != token => other_after_balance == other_before_balance);
    // TODO: need to figure out how to write this:  _recordTransferIn also sets tokenBalances[token] to balanceOf(this) 
}  


// 4. _afterTransferOut should not change the tokenBalances[token'] where token' != token
rule _afterTransferOut_changes_no_other_balance(address token) {
    env e;
    address other;
    uint256 other_before_balance = tokenBalances(e, other);
    afterTransferOut(e, token);
    uint256 other_after_balance = tokenBalances(e, other); 
    assert (other != token => other_after_balance == other_before_balance);
} 

// Bank
// 1. transferOut must increase the tokens for receiver by amount
// 2. something about native tokens but not sure I know why they are special
// 3. roles should be checked too
