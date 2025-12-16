#!/usr/bin/env python
"""
    Awesome copyright text
"""

import core.abstract_test as at
from core.common import wait

class TAFTest(at.AbstractTest):
    def __init__(self, parameters, logger):
        super().__init__(parameters)
        self.logger = logger

    def setup(self):
        return True

    def test(self):
        self.logger.info("Test login")
        wait(5)
        return True

    def teardown(self):
        return True