certoraRun  contracts/config/Config.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
            contracts/event/EventEmitter.sol \
\
--verify Config:certora/specs/Config.spec \
\
--link  Config:dataStore=DataStore \
        Config:roleStore=RoleStore \
        Config:eventEmitter=EventEmitter \
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
--staging \
--rule_sanity \
--prover_args "-optimisticFallback true" \
--send_only \
--msg "GMX Config linking munged to remove emits" 