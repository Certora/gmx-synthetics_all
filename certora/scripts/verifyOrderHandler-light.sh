certoraRun  contracts/exchange/OrderHandler.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
            contracts/oracle/Oracle.sol \
            contracts/mock/WNT.sol \
\
--verify OrderHandler:certora/specs/OrderHandler.spec \
\
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
\
--rule_sanity \
--prover_args "-optimisticFallback true" \
--prover_args '-summarizeExtLibraryCallsAsNonDetPreLinking true' \
--server production \
--prover_version gmx/1 \
\
--send_only \
--msg "GMX OrderHandler light, updateOrderOnly explicit, shellys branch, myWNT, RoleStore Oracle included, _executeOrder is summarized as NONDET" \
--rule updateOrderOnly

# contracts/data/DataStore.sol \
# --prover_args "-splitParallel true -dontStopAtFirstSplitTimeout true" \
# --link  FeeHandler:roleStore=RoleStore \
#         FeeHandler:dataStore=DataStore \