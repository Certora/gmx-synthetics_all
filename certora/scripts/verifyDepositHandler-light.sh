certoraRun  contracts/exchange/DepositHandler.sol \
\
--verify DepositHandler:certora/specs/DepositHandler.spec \
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
--msg "GMX DepositHandler light, createDepositOnly, modifiers are NONDET" \
--rule createDepositOnly

# contracts/data/DataStore.sol \
# --prover_args "-splitParallel true -dontStopAtFirstSplitTimeout true" \
# --link  FeeHandler:roleStore=RoleStore \
#         FeeHandler:dataStore=DataStore \