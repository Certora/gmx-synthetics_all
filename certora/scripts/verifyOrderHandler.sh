certoraRun  contracts/exchange/OrderHandler.sol \
            contracts/exchange/BaseOrderHandler.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
            contracts/event/EventEmitter.sol \
            contracts/order/BaseOrderUtils.sol \
            contracts/order/OrderVault.sol \
            contracts/order/OrderStoreUtils.sol \
            contracts/order/Order.sol \
            contracts/position/Position.sol \
            contracts/oracle/Oracle.sol \
            contracts/mock/ReferralStorage.sol \
            contracts/mock/WNT.sol \
            certora/mocks/DummyERC20A.sol \
            certora/mocks/DummyERC20B.sol \
            contracts/oracle/OracleUtils.sol \
            contracts/position/PositionStoreUtils.sol \
            contracts/market/Market.sol \
            contracts/market/MarketUtils.sol \
            contracts/market/MarketToken.sol \
            contracts/deposit/DepositVault.sol \
            contracts/market/MarketPoolValueInfo.sol \
            contracts/price/Price.sol \
            contracts/data/Keys.sol \
            certora/harness/GetPositionKeyHarness.sol \
            certora/harness/DecreaseOrderUtilsHarness.sol \
            certora/harness/IncreaseOrderUtilsHarness.sol \
            certora/harness/SwapOrderUtilsHarness.sol \
            certora/harness/MarketUtilsHarness.sol \
--verify OrderHandler:certora/specs/OrderHandler.spec \
\
--link  OrderHandler:roleStore=RoleStore \
        OrderHandler:dataStore=DataStore \
        OrderHandler:eventEmitter=EventEmitter \
        OrderHandler:orderVault=OrderVault \
        OrderHandler:oracle=Oracle \
        OrderHandler:referralStorage=ReferralStorage \
\
--solc solc8.19 \
--loop_iter 1 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
\
--server production \
--parametric_contracts OrderHandler \
--prover_version master \
--prover_args "-optimisticFallback true" \
--prover_args '-copyLoopUnroll 1' \
--prover_args "-s [z3]" \
--prover_args "-adaptiveSolverConfig false" \
--prover_args "-enableFlowSensitivePartitioning true" \
--prover_args "-enableCopyLoopRewrites true" \
--prover_args "-enableAggressivePartitionPruning true" \
--rule positions_can_be_closed \
--msg "Rerun GMX Req Property 1 (latest full variant), with new options 2024"
# --prover_args '-summarizeExtLibraryCallsAsNonDetPreLinking true' \
#--prover_args "-adaptiveSolverConfig false -smt_nonLinearArithmetic true" \

