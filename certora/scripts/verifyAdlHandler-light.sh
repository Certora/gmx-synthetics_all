certoraRun  contracts/exchange/AdlHandler.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
\
--verify AdlHandler:certora/specs/AdlHandler.spec \
\
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--server production \
--rule_sanity \
--prover_args "-optimisticFallback true" \
\
--send_only \
--msg "GMX AdlHandler light, globalNonReentrant onlyAdlKeeper withOraclePrices NONDET, updateAdlState internal summary, dispatch dataStore, no linking"

# --prover_args "-splitParallel true -dontStopAtFirstSplitTimeout true" \
# --link  AdlHandler:roleStore=RoleStore \
#         AdlHandler:dataStore=DataStore \