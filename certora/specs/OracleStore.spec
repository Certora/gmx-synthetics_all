using RoleStoreHarness as roleStore;

methods {
    //RoleStore
    //function RoleStore.hasRole(address,bytes32) external => DISPATCHER(true);
    // definition CONTROLLER() returns bytes32 = 70546d1c92f8c2132ae23a23f5177aa8526356051c7510df99f50e012d221529;
}

rule sanity(method f) {
    env e;
    calldataarg args;
    f(e, args);
    assert false;
}

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
