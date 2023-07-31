certoraRun  contracts/router/ExchangeRouter.sol \
            contracts/order/BaseOrderUtils.sol \
            contracts/data/DataStore.sol \
            contracts/exchange/WithdrawalHandler.sol \
            contracts/position/PositionStoreUtils.sol \
            contracts/position/PositionUtils.sol \
            certora/harness/KeysHarness.sol \
            certora/harness/GetPositionKeyHarness.sol \
\
--verify ExchangeRouter:certora/specs/ExchangeRouterSolvency.spec \
--link ExchangeRouter:withdrawalHandler=WithdrawalHandler \
       ExchangeRouter:dataStore=DataStore \
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--server staging \
--prover_version master \
--prover_args "-optimisticFallback true" \
--prover_args "-splitParallel true" \
--prover_args "-splitParallelTimelimit 1000" \
--send_only \
--rule positions_can_be_closed \
--method "simulateExecuteOrder(bytes32,(address[],(uint256,uint256)[]))" \
--msg "positions_can_be_closed, parametric, simulateExecuteOrder, using naftali fix (prover_version master)"