certoraRun.py  certora/harness/SwapOrderUtilsHarness.sol \
            certora/harness/ArrayHarness.sol \
            contracts/order/SwapOrderUtils.sol \
            contracts/order/BaseOrderUtils.sol \
            contracts/swap/SwapUtils.sol \
            contracts/order/OrderStoreUtils.sol \
--verify SwapOrderUtilsHarness:certora/specs/SwapOrderUtils.spec \
\
--solc solc8.19 \
--loop_iter 1 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--server production \
--prover_version master \
\
--prover_args "-optimisticFallback true" \
--prover_args '-copyLoopUnroll 1' \
--prover_args "-solvers [z3]" \
--msg "swapOrder block numbers, run on master, bit of munging of structs, bring in some summarization from the OrderHandler contract, munge SwapUtils.swap, summarize array functions as UF"
# --prover_args '-summarizeExtLibraryCallsAsNonDetPreLinking true' \