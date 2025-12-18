#!/usr/bin/env python

from .playwright import PlaywrightDriver
from .selenium import SeleniumDriver
from .appium import AppiumDriver

class DriverFactory:
    """
    Factory class to create driver instances.
    """

    @staticmethod
    def create_driver(driver_type: str = "playwright", **kwargs):
        """
        Creates and returns a driver instance based on the specified type.
        """
        if driver_type.lower() == "playwright":
            return PlaywrightDriver(**kwargs)
        elif driver_type.lower() == "selenium":
            return SeleniumDriver(**kwargs)
        elif driver_type.lower() == "appium":
            return AppiumDriver(**kwargs)
        else:
            raise ValueError(f"Unknown driver type: {driver_type}")
