

// A simple rule that checks that any call to executeDeposit - the block had to be verified 

rule useOfUpdatedPriceAccordingToBlock(method f)


    bytes32 key;
    OracleUtils.SetPricesParams oracleParams; 

    uint256 blockNumber =  getDepositUpdatedAtBlock(key);

    executeDeposit( key, oracleParams );

    
   assert validateBlockNumberWithinRange(
                oracleParams.minOracleBlockNumbers,
                oracleParams.maxOracleBlockNumbers,
                blockNumber
            );

)




/* any change to a balance of any token by the system is executed only be a keeper:
Note that this takes into account only methods of the contract (i.e., not external transfers...)
*/ 
rule validateOfBalanceChange(address token, address user) {
    method f;
    calldataarg args;
    uint256 before = token.balanceOf(user);
    f(e,args);
    assert token.balanceOf(user) != before => ( hasRole(e.msg.sender,  ORDER_KEEPER)  || hasRole(e.msg.sender,  ORDER_LIQUIDATION)  ); 
}


/* Solvency: the value of a pool is positive.  The worth of the liquidity provider tokens in the pool is greater-equal the pending trader pnl.
Note: invariants are proved by induction. it is proven after the constructor and then for each function it is assumed and them proved to hold 
*/
invariant  isMarketSolvency(
    DataStore dataStore,
    Market.Props memory market,
    Price.Props memory indexTokenPrice,
    Price.Props memory longTokenPrice,
    Price.Props memory shortTokenPrice,
    bytes32 pnlFactorType,
    bool maximize
) 
    getPoolValueInfo( dataStore, market, indexTokenPrice, longTokenPrice, shortTokenPrice, pnlFactorType, maximize) >= 0 