certoraRun certora/harness/TokenUtilsHarness.sol contracts/data/DataStore.sol contracts/data/Keys.sol \
    certora/helpers/Receiver.sol certora/helpers/DummyERC20B.sol certora/helpers/DummyWeth.sol \
    --verify TokenUtilsHarness:certora/spec/TokenUtils.spec \
    --optimistic_loop \
    --solc solc8.19 \
    --cloud \
    --loop_iter 3 \
    --settings -optimisticFallback=true \
    --msg "TokenUtils all rules" 