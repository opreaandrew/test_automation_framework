#!/usr/bin/env python

"""
    Main entry point for the framework
"""

import argparse
import glob
import os
import re
import core.common as common

def parse_arguments() -> argparse.ArgumentParser:
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

    return parser


def process_arguments(args: argparse.Namespace) -> dict:
    config = {
        "selection": {
            "test_paths": args.test or [],
            "target": args.target,
            "environment": args.env,
            "browser": args.browser,
        },
        "execution": {
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
    print(f"  Test paths:  {config['selection']['test_paths'] or None}")
    print(f"  Target:      {config['selection']['target'] or 'default'}")
    print(f"  Environment: {config['selection']['environment'] or 'default'}")
    print(f"  Browser:     {config['selection']['browser'] or 'default'}")
    
    print("\n[Execution Behavior]")
    print(f"  Headless:    {config['execution']['headless']}")
    print(f"  Debug:       {config['execution']['debug']}")
    print(f"  Dry run:     {config['execution']['dry_run']}")
    print(f"  Fail fast:   {config['execution']['fail_fast']}")
    print(f"  Timeout:     {config['execution']['timeout'] or 'default'}s")
    print(f"  Base URL:    {config['execution']['base_url'] or 'from config'}")
    print(f"  Retry:       {config['execution']['retry']}")
    print(f"  Parallel:    {config['execution']['parallel']} worker(s)")
    
    print("\n[Reporting]")
    print(f"  Report type: {config['reporting']['report_type']}")
    print(f"  Screenshots: {config['reporting']['screenshot']}")
    print("=" * 50)
    
    return config


def get_tests_from_path(path: str | list[str]) -> list[str]:
    tests_to_run = []
    paths_to_scan = [path] if isinstance(path, str) else path

    for current_path in paths_to_scan:
        if os.path.isdir(current_path):
            # Check if this path itself is a test folder
            if re.match(r"T\d+$", os.path.basename(current_path)):
                tests_to_run.append(current_path)
            else:
                # Search recursively for test folders
                for root, dirs, _ in os.walk(current_path):
                    for dir_name in dirs:
                        if re.match(r"T\d+$", dir_name):
                            tests_to_run.append(os.path.join(root, dir_name))
    return tests_to_run


def main() -> None:
    parser = parse_arguments()
    args = parser.parse_args()
    
    config = process_arguments(args)

    if not config["selection"]["test_paths"]:
        print("\n[Test_path] is not specified. Running all tests from /tests folder.")
        test_path = os.path.join(common.BASE_DIR, "tests")
    else:
        keywords = config["selection"]["test_paths"]
        print(f"\n[Test_path] Searching for keywords: {keywords}")
        test_path = common.search_for_paths(keywords)
        if test_path:
            print(f"[Test_path] Resolved to: {test_path}")

    tests = get_tests_from_path(test_path)
    print(f"\nFound {len(tests)} test(s): {[os.path.basename(t) for t in tests]}")

    if config["execution"]["dry_run"]:
        print("\n[DRY RUN] Would execute tests with above configuration.")
    else:
        print("\n[TODO] Test execution not yet implemented.")


if __name__ == "__main__":
    main()
