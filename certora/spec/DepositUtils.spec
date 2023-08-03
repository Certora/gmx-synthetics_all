using EventEmitter as EventEmitter;
using DataStore as dataStore;
using DummyERC20A as longToken;
using DummyERC20B as shortToken;

methods {
    // DepositUtils.sol
    function createDepositFn(address, address, address, address, DepositUtils.CreateDepositParams) external returns (bytes32) envfree;
    function cancelDepositFn(address, address, address, bytes32, address, uint256, string, bytes) external envfree;

    // DepositUtilsHarness.sol
    function getMaxSwapPathLength(address) external returns (uint256) envfree;

    // DepositStoreUtils.sol
    function _.set(address, bytes32, Deposit.Props) external => DISPATCHER(true);

    // DataStore.sol
    function _.getAddress(bytes32) external => DISPATCHER(true);
    function _.getUint(bytes32) external => DISPATCHER(true);
    function _.getBool(bytes32) external => DISPATCHER(true); // returns (bool)
    function _.incrementUint(bytes32, uint256) external => DISPATCHER(true); //onlyController returns (uint256)

    // RoleStore.sol
    function _.hasRole(address, bytes32) external => DISPATCHER(true);

    // EventEmitter.sol
    function EventEmitter._ external => NONDET;

    // DepositEventUtils.sol
    function DepositEventUtils._ external => NONDET;

    // DepositVault.sol
    // function _.recordTransferIn(address) external => DISPATCHER(true); // returms (uint256);
    function _.recordTransferIn(address) external => NONDET; // returms (uint256);

    // MarketStoreUtils.sol
    function _.get(address, address) external => DISPATCHER(true); // returns (Market.Props memory)

    // MarketUtils.sol
    function MarketUtils._ external => NONDET;

    function _.getAssetPrice(address) external => NONDET;
}

// function fixedDepositParams(DepositUtils.CreateDepositParams params, env e) {
//     require getMaxSwapPathLength() == 3;
//     require params.receiver == e.msg.sender ;
//     require params.callbackContract ;
//     require params.uiFeeReceiver ;
//     require params.market ;
//     require params.initialLongToken == longToken;
//     require params.initialShortToken == shortToken;
//     require params.longTokenSwapPath.length == 1;
//     require params.shortTokenSwapPath.length == 1;
//     require params.longTokenSwapPath[0] == ;
//     require params.shortTokenSwapPath[0] == ;
//     require params.minMarketTokens ;
//     require params.shouldUnwrapNativeToken == false;
//     require params.executionFee ;
//     require params.callbackGasLimit ;
//         struct CreateDepositParams {
//         address receiver;
//         address callbackContract;
//         address uiFeeReceiver;
//         address market;
//         address initialLongToken;
//         address initialShortToken;
//         address[] longTokenSwapPath;
//         address[] shortTokenSwapPath;
//         uint256 minMarketTokens;
//         bool shouldUnwrapNativeToken;
//         uint256 executionFee;
//         uint256 callbackGasLimit;
//     }
// }

rule integrityOfCreateDeposit(address account, address depositVault) {
    DepositUtils.CreateDepositParams params;
     
    createDepositFn(dataStore, EventEmitter, depositVault, account, params);

    assert false;
}

// rule complexity_check {
//     method f; env e; calldataarg args;
//     f(e, args);
//     assert false, "this assertion should fail";
// }

// rule integrityOfCreateDeposit() {}

// rule integrityOfCancelDeposit() {}
