certoraRun  certora/harness/SwapOrderUtilsHarness.sol \
            certora/harness/ArrayHarness.sol \
            certora/harness/GetPositionKeyHarness.sol \
            contracts/order/DecreaseOrderUtils.sol \
            contracts/order/BaseOrderUtils.sol \
            contracts/swap/SwapUtils.sol \
            contracts/position/DecreasePositionUtils.sol \
            contracts/order/OrderStoreUtils.sol \
            contracts/error/ErrorUtils.sol \
            contracts/market/MarketToken.sol \
            certora/mocks/DummyERC20A.sol \
            certora/mocks/DummyERC20B.sol \
            contracts/oracle/Oracle.sol \
            contracts/market/MarketUtils.sol \
            certora/harness/MarketUtilsHarness.sol \
            contracts/data/Keys.sol \
--verify SwapOrderUtilsHarness:certora/specs/ReqP5SwapOrder.spec \
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
--rule priceDontChangeNoDecreeseInPoolValue \
--msg "SwapOrder P5"