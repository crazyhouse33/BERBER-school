#!/bin/bash
dir="${0%/*}"
cd "$dir"/blackboxTesting
python3 -m unittest quick
python3 -m unittest testFrame
python3 -m unittest testRandomSeriesSimulation
