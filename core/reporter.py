#!/usr/bin/env python

import os
import csv
import re
from datetime import datetime

class Reporter:
    def generate_report(tests: list[str]):
        if not tests:
            return

        # Get current timestamp
        now = datetime.now()
        timestamp = now.strftime("%Y_%m_%d-%H_%M_%S")

        # Determine last common folder
        common_path = os.path.commonpath(tests)
        common_folder = os.path.basename(common_path)

        # Construct CSV filename
        filename = f"{common_folder}-{timestamp}.csv"
        reports_dir = os.path.join(os.getcwd(), "reports")
        os.makedirs(reports_dir, exist_ok=True)
        csv_path = os.path.join(reports_dir, filename)

        # Generate report data
        report_data = []
        for test_path in tests:
            test_name = os.path.basename(test_path)
            log_file = os.path.join(test_path, "result.log")

            driver = "N/A"
            headless = "N/A"
            browser = "N/A"
            status = "N/A"

            if os.path.exists(log_file):
                with open(log_file, "r") as f:
                    content = f.read()
                    if "TEST PASSED" in content:
                        status = "PASS"
                    elif "TEST FAILED" in content:
                        status = "FAIL"
                    match = re.search(r"Initializing driver:\s*([^,]+),\s*([^,]+),\s*(\w+)", content)
                    if match:
                        driver = match.group(1).strip()
                        browser = match.group(2).strip()
                        headless = match.group(3).strip()
                    
            report_data.append({"test name": test_name, "driver": driver, "headless": headless, "browser": browser, "status": status})

        # Write to CSV
        with open(csv_path, mode="w", newline="") as f:
            fieldnames = ["test name", "driver", "headless", "browser", "status"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(report_data)

        print(f"\nReport generated: {csv_path}")