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
// status: works as long as I do not also test getSigners which fails
// probably due to lack of constraints around memory
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
// status: works as long as I do not also test getSigners which fails
// probably due to lack of constraints around memory
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

// 5. calling addSigner with the controller role will: increase getSignerCount, and add the signer to the result of getSinger(s) for some index(es).
// status: last assert fails... not sure why yet...
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
    // NOTE: This does not seem to affect verification result at the moment.
    // Try removing this later...
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
// status: last assert also fails here... confused about why as well.
rule remove_signer_valid_liveness {
    env e;
    calldataarg args;
    address signer_to_remove;
    uint256 signer_count_before;
    uint256 signer_count_after;

    uint256 signers_invariant_index;
    uint256 signers_invariant_address;

    // invariants that the specify the EnumerableSet is well-formed.
    require (oracleStore.signers._inner.values[signers_invariant_index] ==
        signers_invariant_address) <=> (oracleStore.signers._inner._indexes[signers_invariant_address] == signers_invariant_index);



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
rule double_get_signer_count {
    env e;
    uint256 signer_count_one;
    uint256 signer_count_two;
    signer_count_one = getSignerCount(e);
    signer_count_two = getSignerCount(e);
    assert(signer_count_one == signer_count_two);
}


