#!/usr/bin/env python
"""
    Awesome copyright text
"""

import core.abstract_test as at

class TAFTest(at.AbstractTest):
    def __init__(self, parameters, logger, actions):
        super().__init__(parameters, logger, actions)

    def setup(self):
        return True

    def test(self):
        self.logger.error("Test login")
        self.actions.wait(5)
        return True

    def teardown(self):
        return True