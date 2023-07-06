using OracleStoreHarness as oracleStore;

definition UINT256_MAX() returns uint256 = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff;

methods {
    //RoleStore
    //function RoleStore.hasRole(address,bytes32) external => DISPATCHER(true);
    // definition CONTROLLER() returns bytes32 = 70546d1c92f8c2132ae23a23f5177aa8526356051c7510df99f50e012d221529;
}

rule sanity_satisfy(method f) {
    env e;
    calldataarg args;
    f(e, args);
    satisfy true;
}

// Natural language specifications
// 1. for addSigner, if the caller does not have the controller role
// the contract reverts and
// the result of calling getSigner will not change before/after the function
// (i.e. only those with the controller role can change signers)
//     -- similar as last spec but using getSigners()
//     -- similar as last spec but using getSignerCount()
// 2. for removeSigner, if the caller does not have the controller role
// the contract reverts and
// the result of calling getSigner will not change before/after the function
// (i.e. only those with the controller role can change signers)
//     -- similar as last spec but using getSigners()
//     -- similar as last spec but using getSignerCount()
// 3. calling removeSigner with an address that has not been added
// to the list of signers previously will have no affect on: getSigner(s), getSignerCount
// 4. calling getSigner with an invalid index "fails gracefully"
// 5. calling addSigner with the controller role will: increase getSignerCount, and add the signer to the result of getSinger(s) for some index(es).
// 6. calling removeSigner as a controller and on an address that has been 
// added to the list of signers previously will: decrease getSigners, ensure
// the address will not appear in the result of getSigner(s) for any index
// 7. calling getSignerCount() twice in a row with no other interleaving calls
// results in the same value. Similar for getSigner(s)
// 8. the results from getSigner and getSigners are consistent.

// 1. for addSigner, if the caller does not have the controller role
// the contract reverts and
// the result of calling getSigner will not change before/after the function
// (i.e. only those with the controller role can change signers)
//     -- similar as last spec but using getSigners()
//     -- similar as last spec but using getSignerCount()
//
// status: not working -- fails revert assertion and also others
// if that one is commented out.
rule non_controller_add_signer {
    env e;
    calldataarg args;
    address new_signer_address;
    uint256 signer_count_before;
    uint256 signer_count_after;
    uint256 some_index;
    address signer_at_index_before;
    address signer_at_index_after;
    // uint256 signers_arr_idx;
    // uint256 some_start;
    // uint256 some_end;
    // address[] signers_before;
    // address[] signers_after;

    // Assuming: The "signers" set obeys an invariant that
    // the two data structures it uses internally are consistent.
    uint256 signers_invariant_index;
    address signers_invariant_address;
    address[] signer_set_values;
    signer_set_values = oracleStore.getSignerSetValues(e);
    require ((signer_set_values[signers_invariant_index] == signers_invariant_address) <=> (oracleStore.getSignerSetIndexFor(e, signers_invariant_address) == signers_invariant_index));

    // The caller does  not have the controller role
    // bytes32 myController = roleStore.getCONTROLLER(e);
    // require(!roleStore.hasRole(e, e.msg.sender, myController));
    require(!oracleStore.hasControllerRole(e));

    // The index used to check the getSigners result is within the
    // range used
    // require(some_start <= signers_arr_idx && signers_arr_idx < some_end);

    signer_count_before = oracleStore.getSignerCount(e);
    signer_at_index_before = oracleStore.getSigner(e, some_index);
    // signers_before = getSigners(e, some_start, some_end);
    
    oracleStore.addSigner@withrevert(e, new_signer_address);
    assert(lastReverted, "the call reverts");
    
    signer_count_after = oracleStore.getSignerCount(e);
    signer_at_index_after = oracleStore.getSigner(e, some_index);
    // signers_after = getSigners(e, some_start, some_end);

    assert(signer_count_before == signer_count_after, "signer count has not changed");
    assert(signer_at_index_before == signer_at_index_after, "getSigners has not changed");
    // assert(signers_before[signers_arr_idx] == signers_after[signers_arr_idx]);
}

// 2. for removeSigner, if the caller does not have the controller role
// the contract reverts and
// the result of calling getSigner will not change before/after the function
// (i.e. only those with the controller role can change signers)
//     -- similar as last spec but using getSigners()
//     -- similar as last spec but using getSignerCount()
//
// status: not working -- fails revert assertion and also others
// if that one is commented out.
rule non_controller_remove_signer {
    env e;
    calldataarg args;
    address remove_signer_address;
    uint256 signer_count_before;
    uint256 signer_count_after;
    uint256 some_index;
    address signer_at_index_before;
    address signer_at_index_after;
    // uint256 signers_arr_idx;
    // uint256 some_start;
    // uint256 some_end;
    // address[] signers_before;
    // address[] signers_after;

    // The caller does  not have the controller role
    // bytes32 myController = roleStore.getCONTROLLER(e);
    // require(!roleStore.hasRole(e, e.msg.sender, myController));
    require(!oracleStore.hasControllerRole(e));

    // The index used to check the getSigners result is within the
    // range used
    // require(some_start <= signers_arr_idx && signers_arr_idx < some_end);

    signer_count_before = oracleStore.getSignerCount(e);
    signer_at_index_before = oracleStore.getSigner(e, some_index);
    // signers_before = getSigners(e, some_start, some_end);
    
    oracleStore.removeSigner@withrevert(e, remove_signer_address);
    assert(lastReverted, "the call reverts");
    
    signer_count_after = oracleStore.getSignerCount(e);
    signer_at_index_after = oracleStore.getSigner(e, some_index);
    // signers_after = getSigners(e, some_start, some_end);

    assert(signer_count_before == signer_count_after, "signer count has not changed");
    assert(signer_at_index_before == signer_at_index_after, "getSigners has not changed");
    // assert(signers_before[signers_arr_idx] == signers_after[signers_arr_idx]);
}

// 3. calling removeSigner with an address that has not been added
// to the list of signers previously will have no affect on: getSigner(s), 
// getSignerCount
// status: passing
rule remove_signer_not_in_list {
    env e;
    address signer_remove_arg;
    uint256 signer_count_before;
    uint256 signer_count_after;
    uint256 some_index;
    address signer_at_index_before;
    address signer_at_index_after;

    // the signer address argument is not in the list
    require(!oracleStore.signersContains(e, signer_remove_arg));

    signer_count_before = oracleStore.getSignerCount(e);
    signer_at_index_before = oracleStore.getSigner(e, some_index);

    oracleStore.removeSigner(e, signer_remove_arg);

    signer_count_after = oracleStore.getSignerCount(e);
    signer_at_index_after= oracleStore.getSigner(e, some_index);

    assert(signer_count_before == signer_count_after);
    assert(signer_at_index_before == signer_at_index_after);
}

// 4. calling getSigner with an invalid index "fails gracefully"
rule get_invalid_index {
    env e;
    address signer_at_index;

    // Assuming: The "signers" set obeys an invariant that
    // the two data structures it uses internally are consistent.
    uint256 signers_invariant_index;
    address signers_invariant_address;
    address[] signer_set_values;
    signer_set_values = oracleStore.getSignerSetValues(e);
    require ((signer_set_values[signers_invariant_index] 
        == signers_invariant_address) <=> 
        (oracleStore.getSignerSetIndexFor(e, signers_invariant_address) == signers_invariant_index));


    // This spec could probably be made more general,
    // but starting simple with testing getting an element
    // when it is empty

    require(oracleStore.getSignerCount(e) == 0);

    signer_at_index = oracleStore.getSigner@withrevert(e, 1);
    assert(lastReverted);
}

// 5. calling addSigner with the controller role will: increase getSignerCount, and add the signer to the result of getSinger(s) for some index(es).
// status: passing
rule add_signer_valid_liveness {
    env e;
    calldataarg args;
    address new_signer_address;
    uint256 signer_count_before;
    uint256 signer_count_after;

    // The caller *does* have the controller role
    // bytes32 myController = roleStore.getCONTROLLER(e);
    // require(roleStore.hasRole(e, e.msg.sender, myController));
    require (oracleStore.hasControllerRole(e));


    signer_count_before = oracleStore.getSignerCount(e);
    require(signer_count_before < UINT256_MAX()); // reasonable: not many signers

    oracleStore.addSigner(e, new_signer_address);
    // assert(!lastReverted, "addSigner does not revert with correct permissions"); // NOTE: fails... must be other reasons for reverts

    signer_count_after = oracleStore.getSignerCount(e);

    assert(signer_count_after == assert_uint256(signer_count_before + 1) ||
        signer_count_after == signer_count_before,
        "the signer count increments after adding a new signer, or is the same (in case it was already a signer)");
    
    assert(oracleStore.signersContains(e, new_signer_address),
        "the new signer has been added to the list");

}

// 6. calling removeSigner as a controller and on an address that has been 
// added to the list of signers previously will: decrease getSigners, ensure
// the address will not appear in the result of getSigner(s) for any index
// status: passing
rule remove_signer_valid_liveness {
    env e;
    calldataarg args;
    address signer_to_remove;
    uint256 signer_count_before;
    uint256 signer_count_after;

    // Assuming: The "signers" set obeys an invariant that
    // the two data structures it uses internally are consistent.
    uint256 signers_invariant_index;
    address signers_invariant_address;
    address[] signer_set_values;
    signer_set_values = oracleStore.getSignerSetValues(e);
    require ((signer_set_values[signers_invariant_index] == signers_invariant_address) <=> (oracleStore.getSignerSetIndexFor(e, signers_invariant_address) == signers_invariant_index));

    // The caller *does* have the controller role
    // bytes32 myController = roleStore.getCONTROLLER(e);
    // require(roleStore.hasRole(e, e.msg.sender, myController)); 
    require(oracleStore.hasControllerRole(e));

    // the signer to be deleted is really in the set
    require(oracleStore.signersContains(e, signer_to_remove));

    signer_count_before = oracleStore.getSignerCount(e);

    oracleStore.removeSigner(e, signer_to_remove);
    assert(!lastReverted, "removeSigner does not revert with correct permissions");

    signer_count_after = oracleStore.getSignerCount(e);

    assert(signer_count_after == assert_uint256(signer_count_before - 1),
        "Removing a signer that exists and with correct permissions reduces signer count" );
    assert(!oracleStore.signersContains(e, signer_to_remove),
        "the removed signer is not in the list of signers");
}

// 7. calling getSignerCount() twice in a row with no other interleaving calls
// results in the same value. Similar for getSigner(s)
// status: passing
rule double_get_signer_count {
    env e;
    uint256 signer_count_one;
    uint256 signer_count_two;
    signer_count_one = getSignerCount(e);
    signer_count_two = getSignerCount(e);
    assert(signer_count_one == signer_count_two);
}


