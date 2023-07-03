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
// -- similar as last spec but using getSigners()
// -- similar as last spec but using getSignerCount()
// -- calling removeSigner with an address that has not been added
// to the list of signers previously will have no affect on: getSigner(s), getSignerCount
// -- calling getSigner with an invalid index "fails gracefully"
// -- calling addSigner with the controller role will: increase the size of getSigners, and add the signer to the result of getSinger(s) for some index(es).
// -- calling 