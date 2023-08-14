certoraRun  contracts/exchange/OrderHandler.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
            contracts/event/EventEmitter.sol \
            contracts/order/OrderVault.sol \
            contracts/oracle/Oracle.sol \
            contracts/swap/SwapHandler.sol \
            contracts/mock/ReferralStorage.sol \
            contracts/mock/WNT.sol \
            certora/mocks/DummyERC20A.sol \
            certora/mocks/DummyERC20B.sol \
\
--verify OrderHandler:certora/specs/OrderHandler.spec \
\
--link  OrderHandler:roleStore=RoleStore \
        OrderHandler:dataStore=DataStore \
        OrderHandler:eventEmitter=EventEmitter \
        OrderHandler:orderVault=OrderVault \
        OrderHandler:swapHandler=SwapHandler \
        OrderHandler:oracle=Oracle \
        OrderHandler:referralStorage=ReferralStorage \
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
--msg "GMX OrderHandler full, shellys branch, myWNT, all, with linking" #\
# --rule createDepositOnly

# contracts/data/DataStore.sol \
# --prover_args "-splitParallel true -dontStopAtFirstSplitTimeout true" \
# --link  FeeHandler:roleStore=RoleStore \
#         FeeHandler:dataStore=DataStore \