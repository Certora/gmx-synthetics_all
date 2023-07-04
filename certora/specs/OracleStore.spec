using RoleStoreHarness as roleStore;
using OracleStoreHarness as oracleStore;

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
    bytes32 myController = roleStore.getCONTROLLER(e);
    require(!roleStore.hasRole(e, e.msg.sender, myController));

    // The index used to check the getSigners result is within the
    // range used
    // require(some_start <= signers_arr_idx && signers_arr_idx < some_end);

    signer_count_before = getSignerCount(e);
    signer_at_index_before = getSigner(e, some_index);
    // signers_before = getSigners(e, some_start, some_end);
    
    addSigner@withrevert(e, new_signer_address);
    assert(lastReverted, "the call reverts");
    
    signer_count_after = getSignerCount(e);
    signer_at_index_after = getSigner(e, some_index);
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
    bytes32 myController = roleStore.getCONTROLLER(e);
    require(!roleStore.hasRole(e, e.msg.sender, myController));

    // The index used to check the getSigners result is within the
    // range used
    // require(some_start <= signers_arr_idx && signers_arr_idx < some_end);

    signer_count_before = getSignerCount(e);
    signer_at_index_before = getSigner(e, some_index);
    // signers_before = getSigners(e, some_start, some_end);
    
    removeSigner@withrevert(e, remove_signer_address);
    assert(lastReverted, "the call reverts");
    
    signer_count_after = getSignerCount(e);
    signer_at_index_after = getSigner(e, some_index);
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
    // address some_signer_arg; // may or may not be same as arg to call
    // uint256 some_index_before;
    uint256 signer_count_before;
    // uint256 some_index_after;
    uint256 signer_count_after;

    // there is no index for which the signer is in the list
    require(!oracleStore.signersContains(e, signer_remove_arg));

    signer_count_before = getSignerCount(e);
    oracleStore.removeSigner(e, signer_remove_arg);
    signer_count_after = getSignerCount(e);

    assert(signer_count_before == signer_count_after);
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


