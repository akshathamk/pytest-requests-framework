# pytest-requests-framework
Python - Pytest - Requests

##Steps followed to create this framework from scratch:

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


##Commands to run:

to activate virtual env : `source venv/bin/activate;  `

1. `pytest`

   will run all tests under test folder
2. `pytest -s`
   
   will run tests with  --capture=no , hence will display all print statements in console
3. `ENV=TEST pytest -s`

   set an environment variable ENV to be read by config.py to filter data from properties.ini file based on sections
4. `ENV=TEST pytest -s --user_id=2`

   run tests by passing env variable and also setting a pytest option 'user-id' as a fixture to be used in test methods directly(processed in conftest.py)
