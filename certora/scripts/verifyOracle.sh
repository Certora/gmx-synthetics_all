certoraRun  contracts/oracle/Oracle.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
            contracts/event/EventEmitter.sol \
            contracts/oracle/OracleStore.sol \
            contracts/mock/MockPriceFeed.sol \
\
--verify Oracle:certora/specs/Oracle.spec \
\
--link  Oracle:roleStore=RoleStore \
        Oracle:oracleStore=OracleStore \
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--staging \
--rule_sanity \
--prover_args "-optimisticFallback true" \
--send_only \
--msg "GMX Oracle linking, munged to remove emits, DISPATCHERs, with MockPriceFeed" 