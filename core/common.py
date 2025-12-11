#!/usr/bin/env python
"""
    Common functions for the framework
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def search_for_paths(keywords: list[str], base_dir: str=BASE_DIR) -> list[str]:
    tests_dir = os.path.join(base_dir, "tests")
    resolved_paths = []
    
    for keyword in keywords:
        found = False
        for root, dirs, files in os.walk(tests_dir):
            for dir_name in dirs:
                if keyword.lower() in dir_name.lower() or dir_name.lower() in keyword.lower():
                    resolved_paths.append(os.path.join(root, dir_name))
                    found = True
        
        if not found:
            print(f"[WARNING] No match found for keyword: '{keyword}'")
    
    return resolved_paths