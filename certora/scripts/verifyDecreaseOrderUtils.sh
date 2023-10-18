certoraRun  certora/harness/DecreaseOrderUtilsHarness.sol \
            certora/harness/ArrayHarness.sol \
            certora/harness/GetPositionKeyHarness.sol \
            contracts/order/DecreaseOrderUtils.sol \
            contracts/order/BaseOrderUtils.sol \
            contracts/swap/SwapUtils.sol \
            contracts/position/DecreasePositionUtils.sol \
            contracts/order/OrderStoreUtils.sol \
            contracts/error/ErrorUtils.sol \
--verify DecreaseOrderUtilsHarness:certora/specs/DecreaseOrderUtils.spec \
\
--solc solc8.19 \
--loop_iter 1 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--server staging \
\
--prover_args "-optimisticFallback true" \
--prover_args '-copyLoopUnroll 1' \
--prover_args "-solvers [z3]" \
--send_only \
--msg "DecreaseOrder block numbers, on prod with new tool version"
# --prover_args '-summarizeExtLibraryCallsAsNonDetPreLinking true' \