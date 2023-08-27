certoraRun  contracts/exchange/OrderHandler.sol \
            contracts/role/RoleStore.sol \
            contracts/data/DataStore.sol \
            contracts/event/EventEmitter.sol \
            contracts/order/OrderVault.sol \
            contracts/order/OrderStoreUtils.sol \
            contracts/order/Order.sol \
            contracts/position/Position.sol \
            contracts/oracle/Oracle.sol \
            contracts/mock/ReferralStorage.sol \
            contracts/mock/WNT.sol \
            certora/mocks/DummyERC20A.sol \
            certora/mocks/DummyERC20B.sol \
            contracts/oracle/OracleUtils.sol \
            contracts/position/PositionStoreUtils.sol \
            contracts/market/Market.sol \
            contracts/market/MarketUtils.sol \
            contracts/market/MarketToken.sol \
            contracts/order/OrderVault.sol \
            contracts/deposit/DepositVault.sol \
--verify OrderHandler:certora/specs/OrderHandler.spec \
\
--link  OrderHandler:roleStore=RoleStore \
        OrderHandler:dataStore=DataStore \
        OrderHandler:eventEmitter=EventEmitter \
        OrderHandler:orderVault=OrderVault \
        OrderHandler:oracle=Oracle \
        OrderHandler:referralStorage=ReferralStorage \
\
--solc solc8.19 \
--loop_iter 1 \
--optimistic_loop \
--packages @openzeppelin=node_modules/@openzeppelin prb-math=node_modules/prb-math \
--solc_allow_path . \
\
--rule_sanity \
--prover_args "-optimisticFallback true" \
--prover_args '-summarizeExtLibraryCallsAsNonDetPreLinking true' \
--prover_args '-copyLoopUnroll 1' \
--server production \
\
--send_only \
--msg "GMX OrderHandler GMXMarketAlwaysSolvent - datastore is nondet - ghosts are commented out - copyLoopUnroll 1" 

