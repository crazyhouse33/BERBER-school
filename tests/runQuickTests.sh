#!/bin/bash
dir="${0%/*}"
cd "$dir"/blackboxTesting
python3 -m unittest quick

