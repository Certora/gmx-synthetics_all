certoraRun.py  certora/harness/IncreaseOrderUtilsHarness.sol \
            certora/harness/ArrayHarness.sol \
            contracts/order/IncreaseOrderUtils.sol \
            contracts/order/BaseOrderUtils.sol \
            contracts/swap/SwapUtils.sol \
            contracts/position/IncreasePositionUtils.sol \
            contracts/order/OrderStoreUtils.sol \
            contracts/callback/CallbackUtils.sol \
            contracts/utils/Array.sol \
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
--msg "increaseOrder block numbers, summarize datastore NONDET, summarize immaterial fn as NONDET"
# --msg "increase_executed, summarizing with uninterpreted CVL function"
# --prover_args '-summarizeExtLibraryCallsAsNonDetPreLinking true' \