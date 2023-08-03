certoraRun contracts/exchange/DepositHandler.sol \
    --verify DepositHandler:certora/spec/DepositHandler.spec \
    --optimistic_loop \
    --solc solc8.19 \
    --staging master \
    --loop_iter 3 \
    --settings -optimisticFallback=true \
    --msg "DepositHandler sanity" 