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
--rule_sanity \
--prover_args "-optimisticFallback true" \
--prover_args "-splitParallel true -dontStopAtFirstSplitTimeout true" \
--send_only \
--msg "empty sanity on withdrawHandlerLight, no datastore"