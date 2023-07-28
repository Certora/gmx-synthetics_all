#!/bin/sh
# gambit mutate \
/opt/homebrew/lib/python3.11/site-packages/certora_bins/gambit mutate \
--filename "contracts/oracle/OracleStore.sol" \
--solc_remappings "@openzeppelin=node_modules/@openzeppelin" "prb-math=node_modules/prb-math"