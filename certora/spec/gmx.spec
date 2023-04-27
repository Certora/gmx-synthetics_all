/*

This is a demonstration of a CVL (Certora verification language) spec
written for the gmx-synthetics codebase by the Certora team.

The goal is to demonstrate to the GMX team what CVL looks like and what
kind of properties can be formulated and verified using it with the Certora 
prover.

*/


/*

This is an example of a "unit test" rule - a property that tests an execution of a 
particular function.

In this case we verify the following property:
executeDeposit() function is always called with updated prices.

When running this rule, conceptually the prover will "try" all the possible states, keys 
and oracle params. 
Unless we explicitly specify it in the rule, the prover only considers the happy path - 
where the function call din't revert.

We assert that if executeDeposit() succeeded, the oracle was updated within the valid
range of blocks.

If the prover would find a violation of this rule, it would show the sequence of events
that led to executeDeposit() being called with the wrong prices.

*/
rule useOfUpdatedPriceAccordingToBlock(method f){
    bytes32 key;
    OracleUtils.SetPricesParams oracleParams; 

    uint256 blockNumber =  getDepositUpdatedAtBlock(key);
    executeDeposit(key, oracleParams );

    assert validateBlockNumberWithinRange(oracleParams.minOracleBlockNumbers, 
        oracleParams.maxOracleBlockNumbers, blockNumber);
}



/*

This is an example of a state transition rule.

We verify the following property:
Any change to a balance of any token in the system can be only executed by a keeper.
(note that this take into account only contract methods, not external transfers and such)

This is a parametric rule: it tests every smart contract method, with any possible set of
arguments.

We assert that if the user's token balance has changed, then the sender of the transaction
has an ORDER_KEEPER or LIQUIDATION_KEEPER role.

If the prover were to find a violation, it would show a scenario where the user's balance
changes as a result of a transaction sent by an address which doesn't have a keeper role.


*/
rule validateOfBalanceChange(address token, address user) {
    method f;
    calldataarg args;

    uint256 before = token.balanceOf(user);
    f(e,args);

    assert token.balanceOf(user) != before => 
        hasRole(e.msg.sender,  ORDER_KEEPER) || hasRole(e.msg.sender, LIQUIDATION_KEEPER); 
}


/*

This is an example of an invariant. Invariant is a property that should always hold in 
every scenario / sequence of smart contract calls.

Invariants are proved by Certora prover, first by verifying the expression on the
constructor, then by induction where the inductive step is calling any smart contract
function.

This invariant states that markets are always solvent 
(no scenario where due to a function call, traders PnL is greater than pool value)

*/

invariant  isMarketSolvency(
    DataStore dataStore,
    Market.Props market,
    Price.Props indexTokenPrice,
    Price.Props longTokenPrice,
    Price.Props shortTokenPrice,
    bytes32 pnlFactorType,
    bool maximize
) 
    getPoolValueInfo( dataStore, market, indexTokenPrice, longTokenPrice, shortTokenPrice, pnlFactorType, maximize) >= 0 