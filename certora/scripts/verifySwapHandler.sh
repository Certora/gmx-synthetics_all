certoraRun  contracts/swap/SwapHandler.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
            contracts/event/EventEmitter.sol \
            contracts/oracle/Oracle.sol \
            contracts/bank/Bank.sol \
            contracts/market/MarketToken.sol \
            contracts/mock/WNT.sol \
            contracts/market/Market.sol \
            certora/harness/KeysHarness.sol \
            certora/mocks/DummyERC20A.sol \
\
--verify SwapHandler:certora/specs/SwapHandler.spec \
\
--link  SwapHandler:roleStore=RoleStore \
\
--solc solc8.19 \
--loop_iter 1 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--server production \
--rule_sanity \
--rule swapPayedByBankMultipleMarkets \
--prover_args "-optimisticFallback true -dumpCodeSizeAnalysis true -depth 30 -dontStopAtFirstSplitTimeout true" \
--send_only \
--msg "swapPayedByBankMultipleMarkets enable multiple markets, with NONDET: getPriceImpactUsd comment bankBalance assert"
