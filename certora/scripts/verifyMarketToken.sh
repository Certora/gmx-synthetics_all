certoraRun  contracts/market/MarketToken.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
            contracts/mock/WNT.sol \
\
--verify MarketToken:certora/specs/MarketToken.spec \
\
--link  MarketToken:dataStore=DataStore \
        MarketToken:roleStore=RoleStore \
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin \
--solc_allow_path . \
--server production \
--rule_sanity \
--prover_args "-optimisticFallback true" \
--send_only \
--msg "GMX MarketToken linking, dispatcher WNT" 