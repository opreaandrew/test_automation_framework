# Test Automation Framework (TAF)

A cross-platform test automation framework in Python supporting web and mobile testing through a unified CLI.

## Current State

What works:
- Multi-driver support via Factory pattern (Playwright, Selenium, Appium)
- Parallel test execution using ThreadPoolExecutor
- CLI argument parsing with structured config
- Test discovery (folders matching T[0-9]+ pattern)
- Per-test logging to result.log
- CSV report generation after test runs
- Headless mode, browser selection, and debug flag
- Abstract test class with setup/test/teardown lifecycle

Project structure:
- core/ - test runner, logger, reporter, actions, abstract test
- drivers/ - Playwright, Selenium, Appium wrappers + factory
- environment/ - config files (placeholder)
- models/ - page models (placeholder)
- tests/ - test cases organized in web/ and mobile/
- taf.py - main entry point

## Usage

```bash
python taf.py                       # runs all tests
python taf.py --test tests/web      # runs tests in a specific folder
python taf.py --driver selenium     # use Selenium instead of Playwright
python taf.py --parallel 4          # run 4 tests in parallel
python taf.py --headless            # headless browser mode
```

## CLI Modifiers

### Test Selection

| Flag | Status | Description |
|------|--------|-------------|
| --test PATH | Working | Run tests in specified folder(s) |
| --target TARGET | TODO | Filter by target |
| --env ENV | TODO | Load environment config |
| --browser BROWSER | Working | Specify browser (chromium, firefox, etc.) |

### Execution Behavior

| Flag | Status | Description |
|------|--------|-------------|
| --driver TYPE | Working | playwright, selenium, or appium |
| --headless | Working | Run in headless mode |
| --debug | Parsed | Flag exists but no debug behavior implemented |
| --dry-run | TODO | Do everything except run tests |
| --fail-fast | TODO | Stop on first failure |
| --timeout SECONDS | TODO | Global test timeout |
| --base-url URL | TODO | Set base URL for tests |
| --retry COUNT | TODO | Retry failed tests |
| --parallel COUNT | Working | Number of parallel workers |

### Reporting and Artifacts

| Flag | Status | Description |
|------|--------|-------------|
| --report TYPE | Parsed | Only CSV implemented, html/json/junit not wired |
| --screenshot MODE | Parsed | Manual method exists, auto-capture not wired |

## TODOs

- [ ] Implement --target filtering
- [ ] Implement --env environment config loading
- [ ] Implement --dry-run mode
- [ ] Implement --fail-fast behavior
- [ ] Implement --timeout for test execution
- [ ] Implement --base-url injection
- [ ] Implement --retry logic for failed tests
- [ ] Wire up --screenshot auto-capture on failure
- [ ] Add HTML/JSON/JUnit report formats
- [ ] Build out Page Object Models in models/