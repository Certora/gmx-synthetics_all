certoraRun  contracts/data/DataStore.sol \
            contracts/role/RoleStore.sol \
\
--verify DataStore:certora/specs/DataStore.spec \
\
--link  DataStore:roleStore=RoleStore \
\
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin \
--solc_allow_path . \
--server production \
--rule_sanity \
--prover_args "-optimisticFallback true" \
--send_only \
--msg "GMX DataStore linking" 