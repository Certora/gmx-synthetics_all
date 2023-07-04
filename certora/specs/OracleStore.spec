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
// the result of calling getSigner will not change before/after the function
// (i.e. only those with the controller role can change signers)
//     -- similar as last spec but using getSigners()
//     -- similar as last spec but using getSignerCount()
// 2. for removeSigner, if the caller does not have the controller role
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
// the result of calling getSigner will not change before/after the function
// (i.e. only those with the controller role can change signers)
//     -- similar as last spec but using getSigners()
//     -- similar as last spec but using getSignerCount()
// status:
// currently failing sanity... is it because we need the specific
// roleStore that is a member of OracleStore ?
rule non_controller_add_signer {
    env e;
    calldataarg args;
    address new_signer_address;
    uint256 signer_count_before;
    uint256 signer_count_after;

    bytes32 myController = roleStore.getCONTROLLER(e);

    require(!roleStore.hasRole(e, e.msg.sender, myController));

    signer_count_before = getSignerCount(e);
    addSigner(e, new_signer_address);
    signer_count_after = getSignerCount(e);
    assert(signer_count_before == signer_count_after);
}

// 3. calling removeSigner with an address that has not been added
// to the list of signers previously will have no affect on: getSigner(s), 
// getSignerCount
//
// status:
// Currently throwing an internal error about types.
// It is apparently bad to call a solidity function inside a
// quantifier though, so this property may not be expressible.
rule remove_signer_not_in_list {
    env e;
    address signer_remove_arg;
    // address some_signer_arg; // may or may not be same as arg to call
    // uint256 some_index_before;
    uint256 signer_count_before;
    // uint256 some_index_after;
    uint256 signer_count_after;

    // Here I am just trying to ensure that the instance of OracleStore
    // under verification is the same as the one in the harness, so
    // that we can use signersContains to get the state of the store
    // under verification. This does not seem to work though...
    require(e.msg.sender == oracleStore); 
    
    // there is no index for which the signer is in the list
    require(!oracleStore.signersContains(e, signer_remove_arg));

    signer_count_before = getSignerCount(e);
    removeSigner(e, signer_remove_arg);
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


