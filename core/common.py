#!/usr/bin/env python
"""
    Common functions for the framework
"""
import os
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def wait(seconds: int):
    time.sleep(seconds)

def wait_for_string_to_appear():
    pass
