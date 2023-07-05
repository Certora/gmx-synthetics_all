certoraRun  contracts/oracle/OracleStore.sol \
            certora/harness/RoleStoreHarness.sol \
            certora/harness/OracleStoreHarness.sol \
            contracts/event/EventEmitter.sol \
\
--verify OracleStore:certora/specs/OracleStore.spec \
\
--link  OracleStore:roleStore=RoleStoreHarness \
        OracleStore:eventEmitter=EventEmitter \
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--server production \
--rule_sanity \
--prover_args "-optimisticFallback true" \
--send_only \
--msg "remove_signer_valid" \
--rule remove_signer_valid_liveness