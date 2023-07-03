certoraRun  contracts/swap/SwapHandler.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
            contracts/event/EventEmitter.sol \
            contracts/oracle/Oracle.sol \
            contracts/bank/Bank.sol \
            contracts/market/MarketToken.sol \
            contracts/mock/WNT.sol \
\
--verify SwapHandler:certora/specs/SwapHandler.spec \
\
--link  SwapHandler:roleStore=RoleStore \
\
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--server production \
--rule_sanity \
--prover_args "-optimisticFallback true" \
--send_only \
--msg "GMX SwapHandler linking, improved dispatcher WNT,Bank,Datastore,Oracle,RoleStore" 