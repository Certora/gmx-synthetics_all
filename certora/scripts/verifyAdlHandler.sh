certoraRun  contracts/exchange/AdlHandler.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
            contracts/event/EventEmitter.sol \
            contracts/order/OrderVault.sol \
            contracts/oracle/Oracle.sol \
            contracts/swap/SwapHandler.sol \
            contracts/mock/ReferralStorage.sol \
            contracts/mock/WNT.sol \
\
--verify AdlHandler:certora/specs/AdlHandler.spec \
\
--link  AdlHandler:roleStore=RoleStore \
        AdlHandler:dataStore=DataStore \
        AdlHandler:eventEmitter=EventEmitter \
        AdlHandler:orderVault=OrderVault \
        AdlHandler:swapHandler=SwapHandler \
        AdlHandler:oracle=Oracle \
        AdlHandler:referralStorage=ReferralStorage \
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--staging \
--rule_sanity \
--prover_args "-optimisticFallback true" \
--prover_args "-splitParallel true -dontStopAtFirstSplitTimeout true" \
--send_only \
--msg "GMX AdlHandler linking, -splitParallel true, all is commented out, including modifiers"