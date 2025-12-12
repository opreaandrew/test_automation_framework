#!/usr/bin/env python

import os
import core.common as common

class TestRunner:
    def __init__(self, config: dict):
        self.config = config
    
    def run(self):
        test_status = {}
        tests_path = []

        if not self.config["selection"]["test_paths"]:
            print("\n[Test_path] is not specified. Running all tests from /tests folder.")
            tests_path = os.path.join(common.BASE_DIR, "tests")
        else:
            keywords = self.config["selection"]["test_paths"]
            print(f"\n[Test_path] Searching for keywords: {keywords}")
            tests_path = self.get_tests_from_path(keywords)
        if tests_path:
            print(f"[Test_path] Resolved to: {tests_path}")

        return test_status


    def get_tests_from_path(path: str | list[str]) -> list[str]:
        tests_to_run = []
        paths_to_scan = [path] if isinstance(path, str) else path

        for current_path in paths_to_scan:
            if os.path.isdir(current_path):
                # Check if this path itself is a test folder
                if re.match(r"T\d+$", os.path.basename(current_path)):
                    tests_to_run.append(current_path)
                else:
                    # Search recursively for test folders
                    for root, dirs, _ in os.walk(current_path):
                        for dir_name in dirs:
                            if re.match(r"T\d+$", dir_name):
                                tests_to_run.append(os.path.join(root, dir_name))
        return tests_to_run


    def start_test_thread(self, test_path: str) -> str:
        # Find the test file
        test_file = None
        for files in os.listdir(test_path):
            if files.endswith(".py") and files != "__init__.py":
                test_file = files

        if not test_file:
            print(f"Error: No .py test file found in {test_path}")
            return False

        # TODO: Start test thread
        # Magic test logic
        return False

