certoraRun certora/harness/DepositUtilsHarness.sol contracts/event/EventEmitter.sol contracts/data/DataStore.sol contracts/data/Keys.sol \
    contracts/market/MarketStoreUtils.sol contracts/deposit/DepositStoreUtils.sol certora/helpers/DummyERC20B.sol certora/helpers/DummyERC20A.sol \
    --verify DepositUtilsHarness:certora/spec/DepositUtils.spec \
    --optimistic_loop \
    --solc solc8.19 \
    --server staging \
    --prover_version master \
    --loop_iter 1 \
    --prover_args "-optimisticFallback true -globalTimeout 3600 -dumpCodeSizeAnalysis true" \
    --msg "DepositUtils dumpCodeSizeAnalysis" 