# pytest-requests-framework
Python - Pytest - Requests

## Commands to run:

Create virtual env: either using Pycharm setup option or `python3 -m venv venv`

To activate virtual env : `source venv/bin/activate;  `

1. `pytest`

   will run all tests under test folder
2. `pytest -s`
   
   will run tests with  --capture=no , hence will display all print statements in console
3. `ENV=TEST pytest -s`

   set an environment variable ENV to be read by config.py to filter data from properties.ini file based on sections
4. `ENV=TEST pytest -s --user_id=2`

   run tests by passing env variable and also setting a pytest option 'user-id' as a fixture to be used in test methods directly(processed in conftest.py)
5. `ENV=TEST pytest --alluredir=src/reports/allure_json -s`

   run tests and generate allure reports related JSON files in the path provided(replace path as required)
6. `allure serve src/reports/allure_json`

   to generate allure reports from the JSON files in HTML format that opens in default browser(replace path as required)
7. ` allure generate src/reports/allure_json --clean -o src/reports/html_reports`

   to generate allure reports in HTML and store them in provided path(replace path as required)

## Details:
* All tests are to be under test folder with filename and test method name starting with 'test' for pytest to recognize
* setup and teardown methods also should start with same text
* Any values/constants can be stored in properties.ini section-wise. Here I have sectioned it on env names with a DEFAULT as fall-back section
* These values are read by config.py and can be used anywhere in the framework by importing the same
* To add fixtures to pytest so that different values are available for test metods, add a fixture in conftest.py or in the same test class. We can even read a value from command line and use it as a fixture Eg: user_id. Read more about fixtures on https://docs.pytest.org/en/7.1.x/how-to/fixtures.html
* To add cstom markers to group tests, use pytest.ini
* requirements.txt will contain all required libraries and their dependencies
* Add files not to be stored remotely in .gitignore
* Makefile can give us a handy command to run multiple commands in an order , also helping read values from command line - TO BE ADDED
* src>utils>rest_client acts as a wrapper on requests library of Python
* allure reporting has been integrated and the commnads required to generate and store reports are mentioned here
* We can also add custom logging for allure reports and same is also covered

## Steps followed to create this framework from scratch[self-notes]:

1. create repo on GitHub
2. clone on local
3. set required git user.name and user.email
4. add a sample file and commit
5. Verify proper commit user
6. Create virtual env:

    python3 -m venv venv

    source venv/bin/activate;
7. add a .gitignore file and we can copy contents from https://github.com/github/gitignore/blob/main/Python.gitignore
8. This will ensure venv is not committed
9. Now to add required content to requirements.txt:(to start with)
    
    pip install pytest

    pip install requests

    pip freeze
   (shows all installed libraries and their dependencies in this venv)

    pip freeze > requirements.txt
   (will copy all libraries to requirements.txt)
10. We can use the same steps to add more libraries as and when required
11. For allure command to be recognised:
   `npm install -g allure-commandline --save-dev`



