certoraRun  contracts/exchange/OrderHandler.sol \
            contracts/order/BaseOrderUtils.sol \
            contracts/data/DataStore.sol \
            contracts/oracle/OracleUtils.sol \
            contracts/position/PositionStoreUtils.sol \
            contracts/position/PositionUtils.sol \
            certora/harness/KeysHarness.sol \
            certora/harness/GetPositionKeyHarness.sol \
\
--verify OrderHandler:certora/specs/GMXProperty1.spec \
--link OrderHandler:dataStore=DataStore \
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--server staging \
--prover_version master \
--prover_args "-optimisticFallback true" \
--prover_args "-dumpCodeSizeAnalysis true" \
--send_only \
--rule sanity_execute_order \
--msg "sanity_execute_order after moving to OrderHandler, un-munging much of order handler"