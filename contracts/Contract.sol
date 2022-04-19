pragma ton-solidity >=0.57.0;

pragma AbiHeader expire;
pragma AbiHeader pubkey;

import "./libs/Errors.sol";

contract Contract {

    uint public val;

    constructor() public {
        require(tvm.pubkey() != 0, Errors.pubkeyIsZero);
        require(tvm.pubkey() == msg.pubkey(), Errors.pubkeyNotMatch);
        tvm.accept();
    }

    function add(uint v) external {
        require(tvm.pubkey() == msg.pubkey(), Errors.pubkeyNotMatch);
        tvm.accept();

        val += v;
    }
}