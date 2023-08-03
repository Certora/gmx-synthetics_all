certoraRun contracts/bank/StrictBank.sol contracts/data/DataStore.sol \
    --verify StrictBank:certora/spec/StrictBank.spec \
    --optimistic_loop \
    --solc solc8.19 \
    --staging master \
    --loop_iter 3 \
    --settings -optimisticFallback=true \
    --msg "StrictBank sanity" 