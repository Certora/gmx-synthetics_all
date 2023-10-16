certoraRun  certora/harness/MarketUtilsHarness.sol \
            certora/harness/PrecisionHarness.sol \
            contracts/market/MarketUtils.sol \
            contracts/data/DataStore.sol \
            contracts/event/EventEmitter.sol \
            contracts/bank/StrictBank.sol \
            contracts/market/Market.sol \
            contracts/market/MarketPoolValueInfo.sol \
            contracts/market/MarketToken.sol \
            contracts/market/MarketEventUtils.sol \
            contracts/market/MarketStoreUtils.sol \
            contracts/position/Position.sol \
            contracts/order/Order.sol \
            contracts/oracle/Oracle.sol \
            contracts/price/Price.sol \
            contracts/utils/Calc.sol \
            contracts/utils/Precision.sol \
--verify MarketUtilsHarness:certora/specs/MarketUtils.spec \
--solc solc8.19 \
--loop_iter 1 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--server production \
--prover_version master \
--prover_args "-optimisticFallback true" \
--prover_args '-copyLoopUnroll 1' \
--rule  market_pricing_correct \
--msg "run market_pricing_correct using ghost summary, fix spec bug to properly do muldiv"