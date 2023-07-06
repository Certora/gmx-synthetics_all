certoraRun  contracts/oracle/OracleStore.sol \
            contracts/role/RoleStore.sol \
            certora/harness/OracleStoreHarness.sol \
            contracts/event/EventEmitter.sol \
\
--verify OracleStore:certora/specs/OracleStore.spec \
\
--link  OracleStoreHarness:roleStore=RoleStore \
        OracleStore:roleStore=RoleStore \
        OracleStoreHarness:eventEmitter=EventEmitter \
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--server production \
--rule_sanity \
--prover_args "-optimisticFallback true" \
--send_only \
--msg "rerun all rules after changing linking"