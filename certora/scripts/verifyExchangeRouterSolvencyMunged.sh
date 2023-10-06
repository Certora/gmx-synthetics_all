certoraRun  contracts/router/ExchangeRouter.sol \
            contracts/data/DataStore.sol \
            contracts/order/BaseOrderUtils.sol \
            contracts/exchange/OrderHandler.sol \
            contracts/oracle/OracleUtils.sol \
            contracts/position/PositionStoreUtils.sol \
            contracts/position/PositionUtils.sol \
            certora/harness/KeysHarness.sol \
            certora/harness/GetPositionKeyHarness.sol \
\
--verify ExchangeRouter:certora/specs/ExchangeRouterSolvency.spec \
--link ExchangeRouter:dataStore=DataStore \
       ExchangeRouter:orderHandler=OrderHandler \
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
--globalTimeout "900" \
--rule positions_can_be_closed \
--method "simulateExecuteOrder(bytes32,(address[],(uint256,uint256)[]))" \
--msg "try very low globalTimeout; use dispatcher for PositionStoreUtils.get, munging: deleting unreached code in ExchangeRouter, OrderHandler, PositionStoreUtils"