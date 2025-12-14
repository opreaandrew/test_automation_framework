#!/usr/bin/env python
"""
    Awesome copyright text
"""

import time
import core.abstract_test as at

class TAFTest(at.AbstractTest):
    def __init__(self, parameters, logger):
        super().__init__(parameters)
        self.logger = logger

    def setup(self):
        self.logger.info("Setup successful")
        return True

    def test(self):
        self.logger.info("Test login")
        time.sleep(5)
        self.logger.info("Login successful")
        return True

    def teardown(self):
        self.logger.info("Teardown successful")
        return True