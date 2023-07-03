certoraRun  contracts/market/MarketFactory.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
            contracts/event/EventEmitter.sol \
\
--verify MarketFactory:certora/specs/MarketFactory.spec \
\
--link  MarketFactory:dataStore=DataStore \
        MarketFactory:roleStore=RoleStore \
        MarketFactory:eventEmitter=EventEmitter \
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--server production \
--rule_sanity \
--prover_args "-optimisticFallback true" \
--send_only \
--msg "GMX MarketFactory linking munged to remove emits" 