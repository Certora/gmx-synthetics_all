certoraRun  contracts/router/ExchangeRouter.sol \
            contracts/order/BaseOrderUtils.sol \
            contracts/data/DataStore.sol \
            contracts/exchange/WithdrawalHandler.sol \
\
--verify ExchangeRouter:certora/specs/ExchangeRouterSolvency.spec \
--link ExchangeRouter:withdrawalHandler=WithdrawalHandler \
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--server production \
--prover_args "-optimisticFallback true" \
--prover_args "-splitParallel true -dontStopAtFirstSplitTimeout true" \
--send_only \
--rule solvency_invariant_cancelWithdrawal \
--msg "solvency_invariant_cancelWithdrawal, summarizeWithdrawalHandler.cancelWithdrawal"