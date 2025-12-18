#!/usr/bin/env python

import core.abstract_test as at

class TAFTest(at.AbstractTest):
    def __init__(self, parameters, logger, actions):
        super().__init__(parameters, logger, actions)

    def setup(self):
        return True

    def test(self):
        url = "https://www.google.com"
        self.actions.navigate_to(url)
        return True

    def teardown(self):
        return True
