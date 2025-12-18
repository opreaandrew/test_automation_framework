#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from .base_driver import BaseDriver

class SeleniumDriver(BaseDriver):
    """
    Selenium implementation of the BaseDriver.
    """

    def __init__(self, browser_type: str = "chrome", headless: bool = True):
        self.browser_type = browser_type
        self.headless = headless
        self.driver = None
        self._start()

    def _start(self):
        if self.browser_type == "chrome":
            options = webdriver.ChromeOptions()
            if self.headless:
                options.add_argument("--headless")
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        elif self.browser_type == "firefox":
            options = webdriver.FirefoxOptions()
            if self.headless:
                options.add_argument("--headless")
            self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=options)
        else:
            raise ValueError(f"Unsupported browser type: {self.browser_type}")

    def get_driver(self):
        return self.driver

    def quit(self):
        if self.driver:
            self.driver.quit()

    def navigate(self, url: str):
        self.driver.get(url)

    def screenshot(self, path: str):
        self.driver.save_screenshot(path)
