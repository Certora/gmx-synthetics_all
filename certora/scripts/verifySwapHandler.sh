certoraRun  contracts/swap/SwapHandler.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
            contracts/event/EventEmitter.sol \
            contracts/oracle/Oracle.sol \
            contracts/bank/Bank.sol \
            contracts/market/MarketToken.sol \
            contracts/mock/WNT.sol \
            contracts/market/MarketUtils.sol \
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
--rule_sanity \
--prover_args "-optimisticFallback true" \
--server production \
--prover_version master \
--rule marketSwapIntegritySatisfy \
--send_only \
--msg "marketSwapItegritySatisfy -- convert to satisfy rule and make the fee calculation opaque" 