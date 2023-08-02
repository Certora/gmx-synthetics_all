certoraRun  contracts/fee/FeeHandler.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
            contracts/market/MarketToken.sol \
            contracts/mock/WNT.sol \
            certora/harness/KeysHarness.sol \
            certora/mocks/DummyERC20A.sol \
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
--rule claimFeesIntegrity \
--prover_args "-optimisticFallback true" \
\
--send_only \
--msg "GMX FeeHandler claimFeesIntegrity verify, use DummyERC20"

# --prover_args "-splitParallel true -dontStopAtFirstSplitTimeout true" \
# --link  FeeHandler:roleStore=RoleStore \
#         FeeHandler:dataStore=DataStore \