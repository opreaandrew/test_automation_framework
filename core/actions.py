import time

"""
High-level Actions API for tests.
"""

class Actions:
    def __init__(self, driver, logger):
        self.driver = driver
        self.logger = logger

    def navigate_to(self, url: str):
        """
        Navigates to the specified URL.
        """
        self.logger.message(f"Navigating to {url}")
        driver = self.driver
        if driver:
            driver.navigate(url)
        else:
            raise RuntimeError("No active driver set. Ensure the test is running through taf.py")

    def take_screenshot(self, path: str):
        """
        Takes a screenshot.
        """
        self.logger.message(f"Taking screenshot at {path}")
        driver = self.driver
        if driver:
            driver.screenshot(path)
        else:
            raise RuntimeError("No active driver set.")

    def wait(self, seconds: int):
        time.sleep(seconds)

