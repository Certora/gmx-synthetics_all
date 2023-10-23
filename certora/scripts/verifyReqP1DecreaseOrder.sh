certoraRun.py  certora/harness/DecreaseOrderUtilsHarness.sol \
            certora/harness/ArrayHarness.sol \
            certora/harness/GetPositionKeyHarness.sol \
            contracts/order/DecreaseOrderUtils.sol \
            contracts/order/BaseOrderUtils.sol \
            contracts/swap/SwapUtils.sol \
            contracts/position/DecreasePositionUtils.sol \
            contracts/order/OrderStoreUtils.sol \
            contracts/error/ErrorUtils.sol \
--verify DecreaseOrderUtilsHarness:certora/specs/ReqP1DecreaseOrder.spec \
\
--solc solc8.19 \
--loop_iter 1 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--server production \
--prover_version yoav/VRSimplifier \
\
--prover_args "-optimisticFallback true" \
--prover_args '-copyLoopUnroll 1' \
--prover_args "-solvers [z3]" \
--prover_args '-summarizeExtLibraryCallsAsNonDetPreLinking true' \
--rule gmx_property1_DecreaseOrder_NoRevert \
--msg "DecreaseOrder version of ReqP1 using an effect-based rather than revert based spec, fixing bug in spec, deleting some summaries in case those somehow cause problems, add the big nondet flag"