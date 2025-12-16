#!/usr/bin/env python

import os
import re
import threading
from concurrent.futures import ThreadPoolExecutor
import importlib
import importlib.util
from .logger import Logger

class TestRunner:
    def __init__(self, config: dict):
        self.config = config
    
    def run(self) -> dict[str, str]:
        test_status = {}
        tests = []

        tests = self.get_tests_from_path(self.config["selection"]["test_paths"])

        if tests:
            print(f"[Test_path] Resolved to: {tests}")

        print("\n" + "=" * 50)
        print("Starting tests...")
        print("=" * 50 + "\n")

        max_workers = self.config["execution"]["parallel"]
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {executor.submit(self._instantiate_test, test): test for test in tests}
            for future in futures:
                test_status[futures[future]] = future.result()
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


    def _instantiate_test(self, test_path: str):
        logger = Logger(test_path)
        logger.start()

        if not self._execute_test(test_path, logger):
            return False
        
        logger.stop()
        return True


    def _execute_test(self, test_path: str, logger: Logger):
        try:
            module_path = os.path.join(test_path, "test.py")
            module_path = module_path.replace("/", ".").replace(".py", "")
            test_module = importlib.import_module(module_path)
            test_instance = test_module.TAFTest(self.config, logger)
            if not test_instance.setup():
                logger.error(f"Test setup failed")
                return False
            logger.info(f"Test setup successful")
            if not test_instance.test():
                logger.error(f"Test failed")
                return False
            logger.info(f"Test execution successful")
            if not test_instance.teardown():
                logger.error(f"Test teardown failed")
                return False
            logger.info(f"Test teardown successful")
            return True
        except Exception as e:
            logger.error(f"An error occurred during test execution for {test_path}: {e}")
            return False