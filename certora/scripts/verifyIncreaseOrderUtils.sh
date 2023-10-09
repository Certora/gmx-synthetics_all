certoraRun  certora/harness/IncreaseOrderUtilsHarness.sol \
            certora/harness/ArrayHarness.sol \
            contracts/order/IncreaseOrderUtils.sol \
            contracts/order/BaseOrderUtils.sol \
            contracts/swap/SwapUtils.sol \
            contracts/position/IncreasePositionUtils.sol \
            contracts/order/OrderStoreUtils.sol \
            contracts/callback/CallbackUtils.sol \
--verify IncreaseOrderUtilsHarness:certora/specs/IncreaseOrderUtils.spec \
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
--rule  increase_blocks_case1variant2 \
--msg "increaseOrder block pricing invariant. specify using instance of arrays instead of function call. Also write as satisfy"
# --prover_args '-summarizeExtLibraryCallsAsNonDetPreLinking true' \