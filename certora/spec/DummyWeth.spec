methods {
    function myAddress() public returns (address) envfree;
    function totalSupply() external returns (uint256) envfree;
    function balanceOf(address) external returns (uint256) envfree;
    function transfer(address, uint256) external returns (bool);
    function allowance(address, address) external returns (uint256) envfree;
    function approve(address, uint256) external returns (bool);
    function transferFrom(address, address, uint256) external returns (bool);
    // WETH
    function deposit() external; // payable 
    function withdraw(uint256) external; 
}