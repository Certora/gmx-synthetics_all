using RoleMock as Role;

methods {
    // RoleStore.sol
    function revokeRole(address, bytes32) external;
    function grantRole(address, bytes32) external;
    function hasRole(address, bytes32) external returns (bool)                              envfree;
    function hasRoleV2(address, bytes32) external returns (bool)                            envfree;
    function getRoleCount() external returns (uint256)                                      envfree;
    function getRoles(uint256, uint256) external returns (bytes32[] memory)                 envfree;
    function getRoleMemberCount(bytes32) external returns (uint256)                         envfree;
    function getRoleMembers(bytes32, uint256, uint256) external returns (address[] memory)  envfree;

    // RoleStoreHarness.sol
    //function roleMembersAtRoleKeyContainsAccount(bytes32, address) external returns bool envfree;

    // RoleMock
    function RoleMock.ROLE_ADMIN() external returns bytes32 envfree;

}


// rule sanity(method f) {
//     env e;
//     calldataarg args;
//     f(e, args);
//     assert false;
// }


// Adding a new role member with roleR should *increase* the count of getRoleMemberCount(roleR) by one
rule countIncreaseByOneWhenGrantRole() {
    env e;
    
    bytes32 roleR;
    address accountA;

    bool hasRoleRAccountABefore = hasRoleV2(accountA,roleR);
    mathint countRoleRMembersBefore = getRoleMemberCount(roleR);
    require countRoleRMembersBefore < max_uint256;  // reasonable there are not so many role members

    grantRole(e,accountA,roleR);

    mathint countRoleRMembersAfter = getRoleMemberCount(roleR);

    assert hasRoleRAccountABefore => (countRoleRMembersAfter == countRoleRMembersBefore);
    assert !hasRoleRAccountABefore => (countRoleRMembersAfter == countRoleRMembersBefore + 1); 
    assert hasRole(accountA,roleR) && hasRoleV2(accountA,roleR);
}


// Removing a roleR from a member should *decrease* the count of getRoleMemberCount(roleR) by one
rule countDecreaseByOneWhenRevokeRole() {
    env e;

    bytes32 roleR;
    address accountA;

    bool hasRoleRAccountABefore = hasRoleV2(accountA,roleR);
    mathint countRoleRMembersBefore = getRoleMemberCount(roleR);
    
    revokeRole(e,accountA,roleR);

    mathint countRoleRMembersAfter = getRoleMemberCount(roleR);

    assert !hasRoleRAccountABefore => (countRoleRMembersAfter == countRoleRMembersBefore);
    assert hasRoleRAccountABefore => (countRoleRMembersAfter == countRoleRMembersBefore - 1);
    assert !hasRole(accountA,roleR) && !hasRoleV2(accountA,roleR);
}

// GetRoleMemberCount(roleX) should not be affected by adding or removing roleR (roleR != roleX)
rule memberCountNonInterference(method f) {
    env e;
    calldataarg args;

    bytes32 roleR;
    bytes32 roleX;
    require roleR != roleX;

    uint256 countRoleRMembersBefore = getRoleMemberCount(roleR);
    uint256 countRoleXMembersBefore = getRoleMemberCount(roleX);

    f(e,args);

    uint256 countRoleRMembersAfter = getRoleMemberCount(roleR);
    uint256 countRoleXMembersAfter = getRoleMemberCount(roleX);

    
    assert (countRoleRMembersAfter != countRoleRMembersBefore) =>
            countRoleXMembersAfter == countRoleXMembersBefore;
}


// Only admin can grant or revoke roles
rule onlyAdminCanGrantOrRevokeRoles(method f){
    env e;
    calldataarg args;
    
    address accountA;
    bytes32 roleR;

    bool hasAdminRole = hasRole(e.msg.sender,Role.ROLE_ADMIN()); // This must be before f because of possibility that e.smg.sender == accountA.


    bool hasRoleRBefore = hasRole(accountA,roleR);
    bool hasRoleRBeforeV2 = hasRoleV2(accountA,roleR);
    uint256 roleMemberCountBefore = getRoleMemberCount(roleR);
    uint256 roleCountBefore = getRoleCount();

    f(e,args);

    bool hasRoleRAfter = hasRole(accountA,roleR);
    bool hasRoleRAfterV2 = hasRoleV2(accountA,roleR);
    uint256 roleMemberCountAfter = getRoleMemberCount(roleR);
    uint256 roleCountAfter = getRoleCount();

    assert (hasRoleRBefore != hasRoleRAfter) => hasAdminRole;
    assert (roleMemberCountBefore != roleMemberCountAfter) => hasAdminRole;
    assert (roleCountBefore != roleCountAfter) => hasAdminRole;
    assert (hasRoleRBeforeV2 != hasRoleRAfterV2) => hasAdminRole;
}


// Granting or revoking roleR from accountA should not affect any accountB.
rule nonInterferenceOfRolesAndAccounts(method f) {
    env e;
    calldataarg args;

    bytes32 roleR; address accountA;
    bytes32 roleX; address accountB;

    bool hasRoleRAccountABefore = hasRole(accountA,roleR);
    bool hasRoleXAccountBBefore = hasRole(accountB,roleX);

    f(e,args);

    bool hasRoleRAccountAAfter = hasRole(accountA,roleR);
    bool hasRoleXAccountBAfter = hasRole(accountB,roleX);

    require (roleR != roleX) || (accountA != accountB);

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

invariant dataConsistency(address accountA, bytes32 roleR)
    hasRole(accountA,roleR) == hasRoleV2(accountA,roleR)
    {
        preserved {
            require getRoleMemberCount(roleR) < max_uint256;
        }
    }


rule dataConsistencyTest() {
    env e;
    address accountA; bytes32 roleR;
    address accountB; bytes32 roleQ;
    
    require accountA > 0xfff;
    require !hasRoleV2(accountA, roleR);

    revokeRole(e, accountB, roleQ);

    assert !hasRoleV2(accountA, roleR);
}
    


    // filtered {
    //     f -> f.selector != revokeRole(address, bytes32).selector
    // }


// rule dataConsistencyAsRule(method f) {
//     env e;
//     calldataarg args;

//     bytes32 roleR;
//     address accountA;

//     require hasRole(accountA,roleR) == hasRoleV2(accountA,roleR);
//     mathint roleMemberCountBefore = getRoleMemberCount(roleR);
//     require roleMemberCountBefore < max_uint256;

//     f(e,args);

//     assert hasRole(accountA,roleR) == hasRoleV2(accountA,roleR);
// }