import pytest

def pytest_addoption(parser):
    """
    add an option to pytest command to read variables from command line and use in test methods
    :param parser:
    :return:
    """
    parser.addoption("--sample_value", action="store", default="DEFAULT",help="Please enter sample value")
    parser.addoption("--user_id", action="store", default="2",help="Please enter user ID value")

@pytest.fixture(scope="session")
def sample_value(request):
    """
    get or return an pytest option that's already added and use in test methods
    :param parser:
    :return:
    """
    return request.config.getoption("--sample_value")

@pytest.fixture(scope="session")
def user_id(request):
    return request.config.getoption("--user_id")
