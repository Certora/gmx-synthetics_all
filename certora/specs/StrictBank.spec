rule sanity(method f) {
    env e;
    calldataarg args;
    f(e, args);
    assert false;
}



// 1. syncTokenBalance should not change the tokenBalances[token'] where token' != token
// 2. _recordTransferIn should not change then tokenBalances[token'] where token' != token
rule f_changes_no_other_balance(method f, address token) filtered {
    f -> f.selector == syncTokenBalance(address).selector ||
    f.selector == recordTransferIn(address).selector ||
    f.selector == afterTransferOutWrapper(address).selector }
{ 
    env e;
    address other;
    uint256 other_before_balance = tokenBalances(e, other);
    f(e, token);
    uint256 other_after_balance = tokenBalances(e, other); 
    assert (other != token => other_after_balance == other_before_balance);
} 



// 3. _recordTransferIn also sets tokenBalances[token] to balanceOf(this)
rule _recordTransferIn_changes_no_other_balance(address token) {
    env e;
    address other;
    uint256 other_before_balance = tokenBalances(e, other);
    recordTransferIn(e, token);
    uint256 other_after_balance = tokenBalances(e, other); 
    // TODO: need to figure out how to write this:  _recordTransferIn also sets tokenBalances[token] to balanceOf(this) 
}  


// Bank
// 1. transferOut must increase the tokens for receiver by amount
// 2. something about native tokens but not sure I know why they are special
// 3. roles should be checked too


// StrictBank
// 5. TODO: roles should be checked too
// if something goes up, something else should go depositAndSendWrappedNativeToken
// valid changes.
// 