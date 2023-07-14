certoraRun  contracts/fee/FeeHandler.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
            certora/mocks/KeysMock.sol \
            contracts/market/MarketToken.sol \
            contracts/mock/WNT.sol \
\
--verify FeeHandler:certora/specs/FeeHandler.spec \
--link  FeeHandler:dataStore=DataStore \
\
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--server production \
--rule_sanity \
--rule claimFeesWorkload \
--prover_args "-optimisticFallback true" \
\
--send_only \
--msg "GMX FeeHandler claimFeesTest with market require 1, dispatch dataStore MarketToken WNT, no linking"

# --prover_args "-splitParallel true -dontStopAtFirstSplitTimeout true" \
# --link  FeeHandler:roleStore=RoleStore \
#         FeeHandler:dataStore=DataStore \