certoraRun.py certora/harness/StrictBankHarness.sol \
--verify StrictBankHarness:certora/specs/StrictBank.spec \
--solc solc8.19 \
--loop_iter 2 \
--optimistic_loop \
--staging \
--rule_sanity \
--prover_args "-optimisticFallback true" \
--send_only \
--msg "GMX StrictBank and Bank" 