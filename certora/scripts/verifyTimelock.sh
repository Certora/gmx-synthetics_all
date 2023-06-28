certoraRun  contracts/config/Timelock.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
            contracts/event/EventEmitter.sol \
            contracts/oracle/OracleStore.sol \
\
--verify Timelock:certora/specs/Timelock.spec \
\
--link  Timelock:roleStore=RoleStore \
        Timelock:dataStore=DataStore \
        Timelock:eventEmitter=EventEmitter \
        Timelock:oracleStore=OracleStore \
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--server staging --prover_version alex/nonskey-minus-skey \
--rule_sanity \
--prover_args "-optimisticFallback true" \
--send_only \
--msg "GMX Timelock linking munged to remove emits with DISPATCHERs" 