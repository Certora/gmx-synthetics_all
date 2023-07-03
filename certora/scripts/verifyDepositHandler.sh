certoraRun  contracts/exchange/DepositHandler.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
            contracts/event/EventEmitter.sol \
            contracts/deposit/DepositVault.sol \
            contracts/oracle/Oracle.sol \
\
--verify DepositHandler:certora/specs/DepositHandler.spec \
\
--link  DepositHandler:roleStore=RoleStore \
        DepositHandler:dataStore=DataStore \
        DepositHandler:eventEmitter=EventEmitter \
        DepositHandler:depositVault=DepositVault \
        DepositHandler:oracle=Oracle \
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
--msg "GMX DepositHandler full shellys branch createDepositOnly, with linking" \
--rule createDepositOnly

# contracts/data/DataStore.sol \
# --prover_args "-splitParallel true -dontStopAtFirstSplitTimeout true" \
# --link  FeeHandler:roleStore=RoleStore \
#         FeeHandler:dataStore=DataStore \