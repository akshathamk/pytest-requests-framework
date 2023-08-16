# pytest-requests-framework
Python - Pytest - Requests

Steps followed to create this framework from scratch:

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
10. 
