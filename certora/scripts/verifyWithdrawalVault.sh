certoraRun contracts/withdrawal/WithdrawalVault.sol \
           contracts/role/RoleStore.sol \
           contracts/data/DataStore.sol \
           contracts/mock/WNT.sol \
--verify WithdrawalVault:certora/specs/WithdrawalVault.spec \
--link  WithdrawalVault:dataStore=DataStore \
        WithdrawalVault:dataStore=RoleStore \
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--staging \
--rule_sanity \
--prover_args "-optimisticFallback true" \
--send_only \
--msg "GMX WithdrawalVault" 