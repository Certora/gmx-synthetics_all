certoraRun  contracts/fee/FeeHandler.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
            contracts/market/MarketToken.sol \
            contracts/mock/WNT.sol \
\
--verify FeeHandler:certora/specs/FeeHandler.spec \
\
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--staging \
--rule_sanity \
--prover_args "-optimisticFallback true" \
\
--send_only \
--msg "GMX FeeHandler light, dispatch dataStore MarketToken WNT, no linking"

# --prover_args "-splitParallel true -dontStopAtFirstSplitTimeout true" \
# --link  FeeHandler:roleStore=RoleStore \
#         FeeHandler:dataStore=DataStore \