export const EXCLUDED_CONFIG_KEYS = {
  ACCOUNT_DEPOSIT_LIST: true,
  ACCOUNT_ORDER_LIST: true,
  ACCOUNT_POSITION_LIST: true,
  ACCOUNT_WITHDRAWAL_LIST: true,
  SAVED_CALLBACK_CONTRACT: true,
  AFFILIATE_REWARD: true,
  CLAIMABLE_COLLATERAL_AMOUNT: true,
  CLAIMABLE_COLLATERAL_TIME_DIVISOR: true,
  CLAIMABLE_FEE_AMOUNT: true,
  CLAIMABLE_FUNDING_AMOUNT: true,
  CLAIMABLE_UI_FEE_AMOUNT: true,
  CLAIMED_COLLATERAL_AMOUNT: true,
  COLLATERAL_SUM: true,
  CUMULATIVE_BORROWING_FACTOR: true,
  CUMULATIVE_BORROWING_FACTOR_UPDATED_AT: true,
  DEPOSIT_FEE_TYPE: true,
  DEPOSIT_LIST: true,
  FEE_RECEIVER: true,
  FUNDING_FEE_AMOUNT_PER_SIZE: true,
  CLAIMABLE_FUNDING_AMOUNT_PER_SIZE: true,
  FUNDING_UPDATED_AT: true,
  IS_ADL_ENABLED: true,
  LATEST_ADL_BLOCK: true,
  MARKET_LIST: true,
  MAX_PNL_FACTOR_FOR_TRADERS: true,
  MAX_PNL_FACTOR_FOR_ADL: true,
  MAX_PNL_FACTOR_FOR_DEPOSITS: true,
  MAX_PNL_FACTOR_FOR_WITHDRAWALS: true,
  MIN_ORACLE_SIGNERS: true,
  NONCE: true,
  OPEN_INTEREST: true,
  OPEN_INTEREST_IN_TOKENS: true,
  ORDER_LIST: true,
  POOL_AMOUNT: true,
  POSITION_FEE_TYPE: true,
  POSITION_IMPACT_POOL_AMOUNT: true,
  POSITION_LIST: true,
  PRICE_FEED: true,
  PRICE_FEED_MULTIPLIER: true,
  REENTRANCY_GUARD_STATUS: true,
  STABLE_PRICE: true,
  SWAP_FEE_TYPE: true,
  SWAP_IMPACT_POOL_AMOUNT: true,
  SWAP_PATH_MARKET_FLAG: true,
  TOTAL_BORROWING: true,
  UI_DEPOSIT_FEE_TYPE: true,
  UI_FEE_FACTOR: true,
  UI_POSITION_FEE_TYPE: true,
  UI_SWAP_FEE_TYPE: true,
  UI_WITHDRAWAL_FEE_TYPE: true,
  USER_INITIATED_CANCEL: true,
  WITHDRAWAL_FEE_TYPE: true,
  // exclude the WITHDRAWAL_GAS_LIMIT key because it is the hashed version
  // of the key that needs to be set instead
  WITHDRAWAL_GAS_LIMIT: true,
  WITHDRAWAL_LIST: true,
  WNT: true,
};
