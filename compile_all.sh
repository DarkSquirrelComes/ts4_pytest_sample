#!/bin/bash
mkdir target
set -e

cd contracts

for CONTRACT in "Contract"
do
	everdev sol compile "$CONTRACT.sol"
    mv "$CONTRACT.tvc" ../target/
    mv "$CONTRACT.abi.json" ../target/
done
