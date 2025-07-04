# ai-driven-e2e-automation
An AI driven e2e automation solution.

## Local

Go to last block of this document.

## Remote

1. Install NodeJs.
2. Install selenium-standalone package.
   https://www.npmjs.com/package/selenium-standalone

```commandline
npm install selenium-standalone -g

selenium-standalone install

selenium-standalone start
```

3. Add selenium_server to [environment.properties](environment.properties) such as:

```commandline
selenium_server=http://localhost:4444/wd/hub
```

4. python runner.py - run - generate_report - open_report

Or:

1. Install Java.
2. Download selenium jar and start grid/hub
   https://www.selenium.dev/downloads/
3. Add selenium_server to [environment.properties](environment.properties) such as:

```commandline
selenium_server=http://localhost:4444/wd/hub
```

## Install npm package allure for your project.

```commandline
npm install -g allure
```

## Install git commit hook.

```commandline
pre-commit install
```

## Use commands like below to run your test cases(both for local and remote).

```commandline
python runner.py - run

python runner.py - generate_report

python runner.py - open_report

python runner.py - generate_report - open_report

python runner.py - run - generate_report - open_report

python runner.py - run --keyword=test_baidu

python runner.py - run --mark=P0

python runner.py - run --keyword=test_baidu --mark=P0

python runner.py - run --case_files=tests\test_baidu_demo.py

python runner.py - run --last_failed=True

python runner.py - run --concurrency=2

python runner.py - run --maxfail=2

python runner.py - run --failed_first=True

python runner.py - run --ignore=tests\test_baidu_demo.py

python runner.py - run --keyword=test_baidu --mark=P0 - generate_report - open_report
```
