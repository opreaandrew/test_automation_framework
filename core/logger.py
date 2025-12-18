#!/usr/bin/env python

import os


class Color:
    RED = "31"
    GREEN = "32"
    YELLOW = "33"
    BLUE = "34"
    DEFAULT = "39"

class Logger:
    def __init__(self, test_folder):
        self.log_file = os.path.join(test_folder, 'result.log')
        self.test_name = os.path.basename(test_folder)
        os.makedirs(test_folder, exist_ok=True)

    def _log(self, message, color):
        if not color:
            color = Color.DEFAULT
        formatted_message = f"\033[{color}m{message}\033[0m"
        print(f"{self.test_name}: {formatted_message}")
        with open(self.log_file, 'a') as f:
            f.write(formatted_message + '\n')

    def start(self):
        self._log("Starting test execution", Color.GREEN)
        with open(self.log_file, 'w') as f:
            f.write('')

    def stop(self):
        self._log("Test execution completed", Color.GREEN)

    def info(self, message):
        self._log(f"[INFO] {message}", Color.YELLOW)

    def error(self, message):
        self._log(f"[ERROR] {message}", Color.RED)

    def message(self, message, color=None):
        self._log(message, color)  

    def append(self, message):
        self._log(message, Color.BLUE)

