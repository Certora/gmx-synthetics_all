certoraRun  contracts/deposit/DepositVault.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
            contracts/mock/WNT.sol \
\
--verify DepositVault:certora/specs/DepositVault.spec \
\
--link  DepositVault:dataStore=DataStore \
        DepositVault:roleStore=RoleStore \
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin \
--solc_allow_path . \
--server production \
--rule_sanity \
--prover_args "-optimisticFallback true" \
--send_only \
--msg "GMX DepositVault linking, dispatcher WNT" 