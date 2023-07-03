methods {
    //RoleStore
    function _.hasRole(address,bytes32) external => DISPATCHER(true);
}

rule sanity_satisfy(method f) {
    env e;
    calldataarg args;
    f(e, args);
    satisfy true;
}

// Natural language specifications
// -- for every function, if the caller does not have the controller role
// the result of calling getSigner will not change before/after the function
// (i.e. only those with the controller role can change signers)
//     -- similar as last spec but using getSigners()
//     -- similar as last spec but using getSignerCount()
// -- calling removeSigner with an address that has not been added
// to the list of signers previously will have no affect on: getSigner(s), getSignerCount
// -- calling getSigner with an invalid index "fails gracefully"
// -- calling addSigner with the controller role will: increase getSignerCount, and add the signer to the result of getSinger(s) for some index(es).
// -- calling removeSigner as a controller and on an address that has been 
// added to the list of signers previously will: decrease getSigners, ensure
// the address will not appear in the result of getSigner(s) for any index
// -- calling getSignerCount() twice in a row with no other interleaving calls
// results in the same value. Similar for getSigner(s)
// -- the results from getSigner and getSigners are consistent.


rule double_get_signer_count {
    env e;
    uint256 signer_count_one;
    uint256 signer_count_two;
    signer_count_one = getSignerCount(e);
    signer_count_two = getSignerCount(e);
    assert(signer_count_one == signer_count_two);
}

rule non_controller_add_signer {
    env e;
    calldataarg args;
    address new_signer_address;
    uint256 signer_count_before;
    uint256 signer_count_after;
    require(!roleStore.hasRole(e.msg.sender, "CONTROLLER"));
    signer_count_before = getSignerCount(e);
    addSigner(e, new_signer_address);
    signer_count_after = getSignerCount(e);
    assert(signer_count_before == signer_count_after);
}

/*
rule remove_signer_not_in_list {
    env e;
    address signer_remove_arg;
    address some_get_signer_result_before;
    uint256 some_index_before;
    // there is no index for which the signer is in the list
    
    removeSigner(e, signer_remove_arg);
}
*/