certoraRun contracts/deposit/DepositVault.sol \
    --verify DepositVault:certora/spec/DepositVault.spec \
    --optimistic_loop \
    --solc solc8.19 \
    --staging master \
    --loop_iter 3 \
    --settings -optimisticFallback=true \
    --msg "DepositVault sanity" 