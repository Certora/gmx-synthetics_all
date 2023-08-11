// using RoleMock as Role;

methods {
    // RoleStore.sol
    function revokeRole(address, bytes32) external;
    function grantRole(address, bytes32) external;
    function hasRole(address, bytes32) external returns (bool)                              envfree;
    function getRoleCount() external returns (uint256)                                      envfree;
    function getRoles(uint256, uint256) external returns (bytes32[] memory)                 envfree;
    function getRoleMemberCount(bytes32) external returns (uint256)                         envfree;
    function getRoleMembers(bytes32, uint256, uint256) external returns (address[] memory)  envfree;
    function castToBytes32(address) external returns bytes32                                envfree;

    // RoleStoreHarness.sol
    //function roleMembersAtRoleKeyContainsAccount(bytes32, address) external returns bool envfree;

    // RoleMock
    function ROLE_ADMIN() external returns bytes32 envfree;

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

    bool hasRoleRAccountABefore = accountHasRole(accountA,roleR);
    mathint countRoleRMembersBefore = getRoleMemberCount(roleR);
    require countRoleRMembersBefore < max_uint256;  // reasonable there are not so many role members

    grantRole(e,accountA,roleR);

    mathint countRoleRMembersAfter = getRoleMemberCount(roleR);

    assert hasRoleRAccountABefore => (countRoleRMembersAfter == countRoleRMembersBefore);
    assert !hasRoleRAccountABefore => (countRoleRMembersAfter == countRoleRMembersBefore + 1); 
    assert hasRole(accountA,roleR) && accountHasRole(accountA,roleR);
}


// Removing a roleR from a member should *decrease* the count of getRoleMemberCount(roleR) by one
rule countDecreaseByOneWhenRevokeRole() {
    env e;

    bytes32 roleR;
    address accountA;

    bool hasRoleRAccountABefore = accountHasRole(accountA,roleR);
    mathint countRoleRMembersBefore = getRoleMemberCount(roleR);
    
    revokeRole(e,accountA,roleR);

    mathint countRoleRMembersAfter = getRoleMemberCount(roleR);

    assert !hasRoleRAccountABefore => (countRoleRMembersAfter == countRoleRMembersBefore);
    assert hasRoleRAccountABefore => (countRoleRMembersAfter == countRoleRMembersBefore - 1);
    assert !hasRole(accountA,roleR) && !accountHasRole(accountA,roleR);
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

    bool hasAdminRole = hasRole(e.msg.sender, ROLE_ADMIN()); // This must be before f because of possibility that e.smg.sender == accountA.


    bool hasRoleRBefore = hasRole(accountA,roleR);
    bool hasRoleRBeforeV2 = accountHasRole(accountA,roleR);
    uint256 roleMemberCountBefore = getRoleMemberCount(roleR);
    uint256 roleCountBefore = getRoleCount();

    f(e,args);

    bool hasRoleRAfter = hasRole(accountA,roleR);
    bool hasRoleRAfterV2 = accountHasRole(accountA,roleR);
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



// ghost field for the values array
ghost mapping(bytes32 => mapping(mathint => bytes32)) ghostRoleMemberValues {
    init_state axiom forall bytes32 roles. forall mathint x. ghostRoleMemberValues[roles][x] == to_bytes32(0);
}
// ghost field for the indexes map
ghost mapping(bytes32 => mapping(bytes32 => uint256)) ghostRoleMemberIndexes {
    init_state axiom forall bytes32 role. forall bytes32 account. ghostRoleMemberIndexes[role][account] == 0;
}
// ghost field for the length of the values array (stored in offset 0)
ghost mapping(bytes32 => uint256) ghostRoleMemberLength {
    // assumption: it's infeasible to grow the list to these many elements.
    init_state axiom forall bytes32 role. ghostRoleMemberLength[role] == 0;
    axiom forall bytes32 role. ghostRoleMemberLength[role] < 0xffffffffffffffffffffffffffffffff;
}

// HOOKS
// Store hook to synchronize ghostLength with the length of the set._inner._values array. 
// We need to use (offset 0) here, as there is no keyword yet to access the length.
hook Sstore currentContract.roleMembers[KEY bytes32 role].(offset 0) uint256 newLength STORAGE {
    ghostRoleMemberLength[role] = newLength;
}
// Store hook to synchronize ghostValues array with set._inner._values.
hook Sstore currentContract.roleMembers[KEY bytes32 role]._inner._values[INDEX uint256 index] bytes32 newValue STORAGE {
    ghostRoleMemberValues[role][index] = newValue;
}
// Store hook to synchronize ghostIndexes array with set._inner._indexes.
hook Sstore currentContract.roleMembers[KEY bytes32 role]._inner._indexes[KEY bytes32 value] uint256 newIndex STORAGE {
    ghostRoleMemberIndexes[role][value] = newIndex;
}

// The load hooks can use require to ensure that the ghost field has the same information as the storage.
// The require is sound, since the store hooks ensure the contents are always the same.  However we cannot
// prove that with invariants, since this would require the invariant to read the storage for all elements
// and neither storage access nor function calls are allowed in quantifiers.
//
// By following this simple pattern it is ensured that the ghost state and the storage are always the same
// and that the solver can use this knowledge in the proofs.

// Load hook to synchronize ghostLength with the length of the set._inner._values array. 
// Again we use (offset 0) here, as there is no keyword yet to access the length.
hook Sload uint256 length currentContract.roleMembers[KEY bytes32 role].(offset 0) STORAGE {
    require ghostRoleMemberLength[role] == length;
}
hook Sload bytes32 value currentContract.roleMembers[KEY bytes32 role]._inner._values[INDEX uint256 index] STORAGE {
    require ghostRoleMemberValues[role][index] == value;
}
hook Sload uint256 index currentContract.roleMembers[KEY bytes32 role]._inner._indexes[KEY bytes32 value] STORAGE {
    require ghostRoleMemberIndexes[role][value] == index;
}

// INVARIANTS

//  This is the main invariant stating that the indexes and values always match:
//        values[indexes[v] - 1] = v for all values v in the set
//    and indexes[values[i]] = i+1 for all valid indexes i.

invariant setInvariant()
    (forall bytes32 role. forall uint256 index. 0 <= index && index < ghostRoleMemberLength[role] => to_mathint(ghostRoleMemberIndexes[role][ghostRoleMemberValues[role][index]]) == index + 1)
    && (forall bytes32 role. forall bytes32 value. ghostRoleMemberIndexes[role][value] == 0 || 
         (ghostRoleMemberValues[role][ghostRoleMemberIndexes[role][value] - 1] == value && ghostRoleMemberIndexes[role][value] >= 1 && ghostRoleMemberIndexes[role][value] <= ghostRoleMemberLength[role]));

// DEFINITION

// Returns, whether a value is in the set.
definition accountHasRole(address account, bytes32 role) returns bool = (ghostRoleMemberIndexes[role][castToBytes32(account)] != 0);


invariant dataIntegrity(bytes32 role, address account)
    hasRole(account,role) == accountHasRole(account,role) {
        preserved { 
            requireInvariant setInvariant();
        }
    }