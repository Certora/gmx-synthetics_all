certoraRun.py ./contracts/role/RoleStore.sol certora/mocks/RoleMock.sol \
--verify RoleStore:certora/specs/RoleStore.spec \
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin \
--solc_allow_path . \
--rule_sanity \
--prover_args "-optimisticFallback true"
