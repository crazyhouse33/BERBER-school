#!/bin/bash
dir="${0%/*}"
cd "$dir"/unitTest
#python3 -m unittest quick

python3 -m unittest testArgParser
#python3 -m unittest testController
#python3 -m unittest testFrame
#python3 -m unittest testSimulation
#python3 -m unittest testRandomSeriesSimulation
