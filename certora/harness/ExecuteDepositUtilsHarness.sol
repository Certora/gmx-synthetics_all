import "../../contracts/deposit/ExecuteDepositUtils.sol";

contract ExecuteDepositUtilsHarness {
    ExecuteDepositUtils.ExecuteDepositParams p;
    function executeDeposit() external {
        ExecuteDepositUtils.executeDeposit(p);
    }
}