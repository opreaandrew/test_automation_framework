#!/usr/bin/env python

from abc import ABC, abstractmethod

class BaseDriver(ABC):
    """
    Abstract base class for all drivers in the framework.
    """

    @abstractmethod
    def get_driver(self):
        """Returns the underlying driver instance."""
        pass

    @abstractmethod
    def quit(self):
        """Quits the driver and closes any associated resources."""
        pass

    @abstractmethod
    def navigate(self, url: str):
        """Navigates to the specified URL."""
        pass

    @abstractmethod
    def screenshot(self, path: str):
        """Takes a screenshot and saves it to the specified path."""
        pass
