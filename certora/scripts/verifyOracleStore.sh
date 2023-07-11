certoraRun  certora/harness/OracleStoreHarness.sol \
            contracts/role/RoleStore.sol \
            contracts/event/EventEmitter.sol \
\
--verify OracleStoreHarness:certora/specs/OracleStore.spec \
\
--link  OracleStoreHarness:roleStore=RoleStore \
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
--msg "fix array calls for all rules"