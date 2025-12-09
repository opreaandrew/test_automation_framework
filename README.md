Thought train so far:
- core: common utils, abstract_test_case, logging etc
- environment: config files
- targets: test runners
- tests: test cases
    Set up a sample test case. Going to model the framework after the test case, in order to keep it as simple as possible.
- models: page models
- taf.py: main entry point
    Should be as simple as possible to run a test case.
    python taf.py  -> runs all test cases with the config from environment
    Modifiers: 
        Test selection:
    --test <path> -> runs all test cases in a folder. If more than one folder is provided, runs all test cases in all folders.
    --target <target> -> runs all test cases with a specific target.
    --env <env> -> runs all test cases with a specific environment.
    --browser <browser> -> runs all test cases with a specific browser.
        Execution behavior:
    --headless -> runs all test cases in headless mode.
    --debug -> runs all test cases in debug mode.
    --dry-run -> do everything except run the test cases.
    --fail-fast -> fail on first test case failure.
    --timeout <timeout> -> runs all test cases with a specific timeout.
    --base-url <url> -> runs all test cases with a specific base url.
    --retry <count> -> runs all test cases with a specific retry count.
    --parallel <count> -> runs all test cases in parallel. Default is 1.
        Reporting and artifacts:
    --report <type> -> runs all test cases with a specific report type. Default is html. Alternatives are: html, json, junit.
    --screenshot <type> -> on, off, only_failed. Default is only_failed.