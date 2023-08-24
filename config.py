import configparser
import os
import allure


def get_env():
    """
    read value of env from env variables and return the same
    :return: env
    """
    return os.environ['ENV']


def get_config(env):
    """
    read configs from properties.ini file and return the section correspondent to env value
    :param env: section name
    :return: configs
    """
    print(env)
    configure = configparser.ConfigParser()
    configure.read('properties.ini')
    return configure[env]


def allure_logs(text):
    with allure.step(text):
        pass
