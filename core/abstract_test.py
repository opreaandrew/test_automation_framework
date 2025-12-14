#!/usr/bin/env python

"""
    Abstract test class
"""

from abc import ABC, abstractmethod

class AbstractTest(ABC):
    def __init__(self, parameters):
        self.parameters = parameters

    @abstractmethod
    def setup(self):
        pass

    @abstractmethod
    def test(self):
        pass

    @abstractmethod
    def teardown(self):
        pass