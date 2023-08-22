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
--smt_timeout 2400 \
--prover_args "-optimisticFallback true" \
--prover_args "-dumpCodeSizeAnalysis true" \
--prover_args "-copyLoopUnroll 1" \
--send_only \
--rule positions_can_be_closed \
--msg "positions_can_be_closed. copyLoopUnroll 1. replace keys with constants. comment createOrder. Summarize orderhandler. munge boolArray, try-catch. SMT_TIMEOUT 2400. Summarize libs and datastore."