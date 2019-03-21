#!/bin/bash
dir="${0%/*}"
cd "$dir"/blackboxTest
#python3 -m unittest quick

cd ../unitTest
python3 testArgParser.py
python3 testRandomSimulation.py
python3 testBitWiseSupervisor.py
