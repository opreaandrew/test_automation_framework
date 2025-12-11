#!/usr/bin/env python
"""
    Awesome copyright text
"""

import core.abstract_test as at
import core.logger as logger

class SlugTest(at.AbstractTest):
    def __init__(self, platform, parameters):
        super().__init__(platform, parameters)

    def setup(self):
        logger.info("Setup successful")
        return True

    def test(self):
        logger.info("Test login")
        if not self.login(self.platform, self.parameters):
            logger.error("Login failed")
            return False
        logger.info("Login successful")
        return True

    def teardown(self):
        logger.info("Teardown successful")
        return True