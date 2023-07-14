certoraRun  contracts/exchange/WithdrawalHandler.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
            contracts/event/EventEmitter.sol \
            contracts/order/OrderVault.sol \
            contracts/oracle/Oracle.sol \
            contracts/swap/SwapHandler.sol \
            contracts/mock/ReferralStorage.sol \
            contracts/mock/WNT.sol \
\
--verify WithdrawalHandler:certora/specs/Solvency.spec \
\
--link  WithdrawalHandler:roleStore=RoleStore \
        WithdrawalHandler:dataStore=DataStore \
        WithdrawalHandler:eventEmitter=EventEmitter \
        WithdrawalHandler:oracle=Oracle \
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--server production \
--rule_sanity \
--prover_args "-optimisticFallback true" \
--prover_args "-splitParallel true -dontStopAtFirstSplitTimeout true" \
--send_only \
--msg "Run empty solvency spec on WithdrawalHandler, all linking"