#!/usr/bin/env python

from playwright.sync_api import sync_playwright
from .base_driver import BaseDriver

class PlaywrightDriver(BaseDriver):
    """
    Playwright implementation of the BaseDriver.
    """

    def __init__(self, browser_type: str = "chromium", headless: bool = True):
        self.browser_type = browser_type
        self.headless = headless
        self.playwright = None
        self.browser = None
        self.context = None
        self.page = None
        self._start()

    def _start(self):
        self.playwright = sync_playwright().start()
        if self.browser_type == "chromium":
            self.browser = self.playwright.chromium.launch(headless=self.headless)
        elif self.browser_type == "firefox":
            self.browser = self.playwright.firefox.launch(headless=self.headless)
        elif self.browser_type == "webkit":
            self.browser = self.playwright.webkit.launch(headless=self.headless)
        else:
            raise ValueError(f"Unsupported browser type: {self.browser_type}")
        
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

    def get_driver(self):
        return self.page

    def quit(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

    def navigate(self, url: str):
        self.page.goto(url)

    def screenshot(self, path: str):
        self.page.screenshot(path=path)
