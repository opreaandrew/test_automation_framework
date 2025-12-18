#!/usr/bin/env python

"""
    Main entry point for the framework
"""

import argparse
from core.test_runner import TestRunner

def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="taf",
        description="Test Automation Framework - Main entry point"
    )

    # Test selection
    selection = parser.add_argument_group("Test Selection")
    selection.add_argument(
        "--test", "-t",
        action="append",
        metavar="PATH",
        help="Run test cases in specified folder(s). Can be used multiple times."
    )
    selection.add_argument(
        "--target",
        metavar="TARGET",
        help="Run test cases with a specific target."
    )
    selection.add_argument(
        "--env", "-e",
        metavar="ENV",
        help="Run test cases with a specific environment."
    )
    selection.add_argument(
        "--browser", "-b",
        metavar="BROWSER",
        help="Run test cases with a specific browser."
    )

    # Execution behavior
    execution = parser.add_argument_group("Execution Behavior")
    execution.add_argument(
        "--driver", "-d",
        choices=["playwright", "selenium", "appium"],
        default="playwright",
        metavar="DRIVER",
        help="Driver type: playwright, selenium, appium. Default is playwright."
    )
    execution.add_argument(
        "--headless",
        action="store_true",
        help="Run test cases in headless mode."
    )
    execution.add_argument(
        "--debug",
        action="store_true",
        help="Run test cases in debug mode."
    )
    execution.add_argument(
        "--dry-run",
        action="store_true",
        help="Do everything except run the test cases."
    )
    execution.add_argument(
        "--fail-fast",
        action="store_true",
        help="Fail on first test case failure."
    )
    execution.add_argument(
        "--timeout",
        type=int,
        metavar="SECONDS",
        help="Run test cases with a specific timeout."
    )
    execution.add_argument(
        "--base-url",
        metavar="URL",
        help="Run test cases with a specific base URL."
    )
    execution.add_argument(
        "--retry",
        type=int,
        default=0,
        metavar="COUNT",
        help="Retry count for failed test cases. Default is 0."
    )
    execution.add_argument(
        "--parallel", "-p",
        type=int,
        default=1,
        metavar="COUNT",
        help="Number of parallel workers. Default is 1."
    )

    # Reporting and artifacts
    reporting = parser.add_argument_group("Reporting and Artifacts")
    reporting.add_argument(
        "--report",
        choices=["html", "json", "junit"],
        default="html",
        metavar="TYPE",
        help="Report type: html, json, junit. Default is html."
    )
    reporting.add_argument(
        "--screenshot",
        choices=["on", "off", "only_failed"],
        default="only_failed",
        metavar="TYPE",
        help="Screenshot mode: on, off, only_failed. Default is only_failed."
    )

    args = parser.parse_args()

    config = {
        "selection": {
            "test_paths": args.test or "tests",
            "target": args.target,
            "environment": args.env,
            "browser": args.browser,
        },
        "execution": {
            "driver": args.driver,
            "headless": args.headless,
            "debug": args.debug,
            "dry_run": getattr(args, "dry_run", False),
            "fail_fast": getattr(args, "fail_fast", False),
            "timeout": args.timeout,
            "base_url": getattr(args, "base_url", None),
            "retry": args.retry,
            "parallel": args.parallel,
        },
        "reporting": {
            "report_type": args.report,
            "screenshot": args.screenshot,
        },
    }
    
    # Log configuration summary
    print("=" * 50)
    print("TAF Configuration")
    print("=" * 50)
    
    print("\n[Test Selection]")
    print(f"  Test paths:  {config['selection']['test_paths'] or 'All tests'}")
    print(f"  Target:      {config['selection']['target'] or 'default'}")
    print(f"  Environment: {config['selection']['environment'] or 'default'}")
    print(f"  Browser:     {config['selection']['browser'] or 'default'}")
    
    print("\n[Execution Behavior]")
    print(f"  Driver:      {config['execution']['driver']}")
    print(f"  Headless:    {config['execution']['headless'] or 'default'}")
    print(f"  Debug:       {config['execution']['debug'] or 'default'}")
    print(f"  Dry run:     {config['execution']['dry_run'] or 'default'}")
    print(f"  Fail fast:   {config['execution']['fail_fast'] or 'default'}")
    print(f"  Timeout:     {config['execution']['timeout'] or 'default'}s")
    print(f"  Base URL:    {config['execution']['base_url'] or 'default'}")
    print(f"  Retry:       {config['execution']['retry'] or 'default'}")
    print(f"  Parallel:    {config['execution']['parallel']} worker(s)")
    
    print("\n[Reporting]")
    print(f"  Report type: {config['reporting']['report_type'] or 'default'}")
    print(f"  Screenshots: {config['reporting']['screenshot'] or 'default'}")
    print("=" * 50)
    
    return config


def main() -> None:
    # Parse arguments
    config = parse_arguments()

    # Initialize test runner and run tests
    test_runner = TestRunner(config)
    test_status = test_runner.run()

    print("\nTest results:")
    for test_path, status in test_status.items():
        result = "Passed" if status else "Failed"
        print(f"  {test_path}: {result}")

    # # Parse individual logs and generate report
    # report = Reports(config)
    # report.generate_report()

if __name__ == "__main__":
    main()
