#!/usr/bin/env python

import os

class Logger:
    def __init__(self, test_folder):
        self.log_file = os.path.join(test_folder, 'result.log')
        os.makedirs(test_folder, exist_ok=True)

    def _log(self, message, color):
        formatted_message = f"\033[{color}m{message}\033[0m"
        print(formatted_message)
        with open(self.log_file, 'a') as f:
            f.write(formatted_message + '\n')

    def start(self):
        self._log("Starting test execution", self.Color.GREEN)
        with open(self.log_file, 'w') as f:
            f.write('')

    def stop(self):
        self._log("Test execution completed", self.Color.GREEN)

    def info(self, message):
        self._log(f"[INFO] {message}", self.Color.YELLOW)

    def error(self, message):
        self._log(f"[ERROR] {message}", self.Color.RED)

    def append(self, message):
        self._log(message, self.Color.BLUE)

    class Color:
        RED = "31"
        GREEN = "32"
        YELLOW = "33"
        BLUE = "34"
    