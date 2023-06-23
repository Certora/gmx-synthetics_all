certoraRun  contracts/oracle/OracleStore.sol \
            contracts/role/RoleStore.sol \
            contracts/event/EventEmitter.sol \
\
--verify OracleStore:certora/specs/OracleStore.spec \
\
--link  OracleStore:roleStore=RoleStore \
        OracleStore:eventEmitter=EventEmitter \
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--staging \
--rule_sanity \
--prover_args "-optimisticFallback true" \
--send_only \
--msg "GMX OracleStore linking munged to remove emits" 