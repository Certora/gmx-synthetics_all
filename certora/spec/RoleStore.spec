using RoleMock as Role;


rule sanity(method f) {
    env e;
    calldataarg args;
    f(e, args);
    assert false;
}



definition UINT64_MAX() returns uint64 = 0xFFFFFFFFFFFFFFFF;
definition UINT256_MAX() returns uint256 = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff;


// Adding a new role member with roleR should *increase* the count of getRoleMemberCount(roleR) by one
rule countIncreaseByOneWhenGrantRole() {
    env e;
    calldataarg args;
    
    bytes32 roleR;
    address accountA;

    revokeRole(e,accountA,roleR); // ensure accountA does not have roleR

    bool hasRoleRAccountABefore = hasRole(e,accountA,roleR);
    uint256 countRoleRMembersBefore = getRoleMemberCount(e,roleR);
    require countRoleRMembersBefore < UINT256_MAX();  // reasonable there are not so many role members

    grantRole(e,accountA,roleR);

    bool hasRoleRAccountAAfter = hasRole(e,accountA,roleR);
    uint256 countRoleRMembersAfter = getRoleMemberCount(e,roleR);

    assert to_mathint(countRoleRMembersAfter) == countRoleRMembersBefore + 1; // new
}


// Removing a roleR from a member should *decrease* the count of getRoleMemberCount(roleR) by one
rule countDecreaseByOneWhenRenounceRole() {
    env e;
    
    bytes32 roleR;
    address accountA;

    grantRole(e,accountA,roleR); // ensure accountA has roleR

    bool hasRoleRAccountABefore = hasRole(e,accountA,roleR);
    uint256 countRoleRMembersBefore = getRoleMemberCount(e,roleR);
    require countRoleRMembersBefore > 0;  // there is at least one account with roleR
    
    revokeRole(e,accountA,roleR);

    bool hasRoleRAccountAAfter = hasRole(e,accountA,roleR);
    uint256 countRoleRMembersAfter = getRoleMemberCount(e,roleR);

    assert to_mathint(countRoleRMembersAfter) == countRoleRMembersBefore - 1;
}

// GetRoleMemberCount(roleX) should not be affected by adding or removing roleR (roleR != roleX)
rule memberCountNonInterference(method f) {
    env e;
    calldataarg args;

    bytes32 roleR;
    bytes32 roleX;
    require roleR != roleX;

    uint256 countRoleRMembersBefore = getRoleMemberCount(e,roleR);
    uint256 countRoleXMembersBefore = getRoleMemberCount(e,roleX);

    f(e,args);

    uint256 countRoleRMembersAfter = getRoleMemberCount(e,roleR);
    uint256 countRoleXMembersAfter = getRoleMemberCount(e,roleX);

    
    assert (countRoleRMembersAfter != countRoleRMembersBefore) =>
            countRoleXMembersAfter == countRoleXMembersBefore;
}


// Only admin can grant or revoke roles
rule onlyAdminCanGrantOrRevokeRoles(method f){
    env e;
    calldataarg args;
    
    address accountA;
    bytes32 roleR;

    bool hasAdminRole = hasRole(e,e.msg.sender,Role.ROLE_ADMIN(e)); // This must be before f because of possibility that e.smg.sender == accountA.

    bool hasRoleRBefore = hasRole(e,accountA,roleR);

    f(e,args);

    bool hasRoleRAfter = hasRole(e,accountA,roleR);

    assert (hasRoleRBefore != hasRoleRAfter) => hasAdminRole;
}

// Should be covered by the above rule if the data is consistent.
rule onlyAdminCanGrantOrRevokeRolesCheckViaMemberCount(method f){
    env e;
    calldataarg args;
    
    bytes32 roleR;

    bool hasAdminRole = hasRole(e,e.msg.sender,Role.ROLE_ADMIN(e));

    uint256 roleMemberCountBefore = getRoleMemberCount(e,roleR);

    f(e,args);

    uint256 roleMemberCountAfter = getRoleMemberCount(e,roleR);

    assert (roleMemberCountBefore != roleMemberCountAfter) => hasAdminRole;
}

// Should be covered by the above if the data is consistent.
rule onlyAdminCanGrantRolesCheckViaRoleCount(method f){
    env e;
    calldataarg args;
    
    bytes32 roleR;

    bool hasAdminRole = hasRole(e,e.msg.sender,Role.ROLE_ADMIN(e));

    uint256 roleCountBefore = getRoleCount(e);

    f(e,args);

    uint256 roleCountAfter = getRoleCount(e);

    assert (roleCountBefore != roleCountAfter) => hasAdminRole;
}

// Granting or revoking roleR from accountA should not affect any accountB.
rule nonInterferenceOfRolesAndAccounts(method f) {
    env e;
    calldataarg args;

    bytes32 roleR; address accountA;
    bytes32 roleX; address accountB;

    bool hasRoleRAccountABefore = hasRole(e,accountA,roleR);
    bool hasRoleXAccountBBefore = hasRole(e,accountB,roleX);

    f(e,args);

    bool hasRoleRAccountAAfter = hasRole(e,accountA,roleR);
    bool hasRoleXAccountBAfter = hasRole(e,accountB,roleX);

    require (roleR != roleX) && (accountA != accountB);

    assert (hasRoleRAccountABefore != hasRoleRAccountAAfter) =>                // if AccountA roles changed
                (hasRoleXAccountBBefore == hasRoleXAccountBAfter);             // accountB roles did not
}


// I don't see a check that role has to be from the list predefined in Role.sol.

/*
rule onlyPredefinedRolesAreAllowed() {
    env e;
    bytes32 roleR;
    address accountA;

    grantRole(e,accountA,roleR);

    uint256 roleCount = getRoleCount(e);

    assert roleCount < 500;
}
*/


// Data consistency.

/*
    roles ... enumerable set of role keys
    roleMembers ... mapping of role keys to enumerable set of accounts
    roleCache[account][roleKey] ... boolean set to true iff account has a particular role (implemented as mapping of accounts to mappings)
*/

//invariant dataConsistency(bytes32 roleR, address accountA)
//    (roleMembers[roleR].contains(accountA)) => (roleCache[roleR][accountA] == true);


/*
rule dataConsistencyAsRule(method f) {
    env e;
    calldataarg args;

    bytes32 roleR;
    address accountA;


    require roleMembers[roleR].contains(accountA) == (roleCache[roleR][accountA] == true);

    f(e,calldataarg);

    assert roleMembers[roleR].contains(accountA) == (roleCache[roleR][accountA] == true);
}
*/