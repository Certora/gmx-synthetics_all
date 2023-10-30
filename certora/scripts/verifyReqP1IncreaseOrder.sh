certoraRun certora/harness/IncreaseOrderUtilsHarness.sol \
            certora/harness/DecreaseOrderUtilsHarness.sol \
            certora/harness/ArrayHarness.sol \
            certora/harness/GetPositionKeyHarness.sol \
            contracts/order/DecreaseOrderUtils.sol \
            contracts/order/IncreaseOrderUtils.sol \
            contracts/order/BaseOrderUtils.sol \
            contracts/swap/SwapUtils.sol \
            contracts/position/IncreasePositionUtils.sol \
            contracts/order/OrderStoreUtils.sol \
            contracts/callback/CallbackUtils.sol \
--verify IncreaseOrderUtilsHarness:certora/specs/ReqP1IncreaseOrder.spec \
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
--rule gmx_property1_IncreaseOrder \
--msg "IncreaseOrder reqp1, assert no revert."
# --prover_args "-depth 20, -mediumTimeout 60, -s\"[z3:def,z3:arith1,z3:lia1]\" " \
# --prover_args "-splitParallel true -smt_parallelLIASolvers \"[z3:def,z3:arith1,z3:lia1]\" -smt_parallelNIASolvers [z3:def]" \