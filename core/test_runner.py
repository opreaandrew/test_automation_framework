#!/usr/bin/env python

import os
import re
import threading
import importlib
import importlib.util
from .logger import Logger

class TestRunner:
    def __init__(self, config: dict):
        self.config = config
    
    def run(self):
        test_status = {}
        tests = []

        tests = self.get_tests_from_path(self.config["selection"]["test_paths"])

        if tests:
            print(f"[Test_path] Resolved to: {tests}")

        print("\n" + "=" * 50)
        print("Starting tests...")
        print("=" * 50 + "\n")
        for test in tests:
            for _ in range(self.config["execution"]["parallel"]):
                test_status[test] = self._start_test_thread(test)
        return test_status


    def get_tests_from_path(self, path: str | list[str]) -> list[str]:
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


    def _start_test_thread(self, test_path: str) -> str:
        # Find the test file
        test_file = None
        for file in os.listdir(test_path):
            if file.endswith(".py") and file != "__init__.py":
                test_file = file

        if not test_file:
            print(f"Error: No .py test file found in {test_path}")
            return False

        logger = Logger(test_path)
        logger.start()
        logger.info(f"Starting test execution for {test_path}")
        test_thread = threading.Thread(target=self._run_single_test, args=(test_path, test_file, logger))
        test_thread.start()
        test_result = test_thread.join()
        logger.info(f"Test execution completed for {test_path}")
        logger.stop()
        return test_result


    def _run_single_test(self, test_path: str, test_file: str, logger: Logger):
        try:
            module_path = os.path.join(test_path, test_file)
            module_path = module_path.replace("/", ".").replace(".py", "")
            test_module = importlib.import_module(module_path)
            test_instance = test_module.TAFTest(self.config, logger)
            if not test_instance.setup():
                print(f"Test setup failed for {path}")
                return False
            if not test_instance.test():
                print(f"Test failed for {path}")
                return False
            if not test_instance.teardown():
                print(f"Test teardown failed for {path}")
                return False
            return True
        except Exception as e:
            print(f"An error occurred during test execution for {path}: {e}")
            return False