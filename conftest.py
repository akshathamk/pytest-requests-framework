import pytest

def pytest_addoption(parser):
    """
    add an option to pytest command to read variables from command line and use in test methods
    :param parser:
    :return:
    """
    parser.addoption("--sample_value", action="store", default="DEFAULT",help="Please enter sample value")

@pytest.fixture(scope="session")
def sample_value(request):
    """
    get or return an pytest option that's already added and use in test methods
    :param parser:
    :return:
    """
    return request.config.getoption("--sample_value")
