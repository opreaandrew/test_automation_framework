#!/usr/bin/env python

"""
    Main entry point for the framework
"""

import argparse


def argument_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser."""
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


def main() -> None:
    """Main entry point."""
    parser = argument_parser()
    args = parser.parse_args()
    # TODO: Implementation
    print(f"Args: {args}")


if __name__ == "__main__":
    main()
