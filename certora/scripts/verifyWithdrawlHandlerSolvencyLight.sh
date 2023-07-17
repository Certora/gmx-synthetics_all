certoraRun  contracts/exchange/WithdrawalHandler.sol \
            contracts/role/RoleStore.sol \
\
--verify WithdrawalHandler:certora/specs/Solvency.spec \
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--server production \
--prover_args "-optimisticFallback true" \
--prover_args "-splitParallel true -dontStopAtFirstSplitTimeout true" \
--send_only \
--msg "withdrawHandlerLight, only summarize cancelWithdrawal as constant, and also summarize modifiers"