#!/usr/bin/python3
import time
import pep8
i=0
while i<10000000:
    i+=1
    time.sleep(0)
"""
    see https://lwn.net/Articles/629155/
    "With current 10Gb adapters, there are 1,230ns between two 1538-byte packets. "
    
    There is no way to reach this precision for waiting in any os I know, at least
    So this feature is useless
    """
