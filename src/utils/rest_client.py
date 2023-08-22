import requests
import logging
from config import *


class RestClient:

    def get(self,path, headers=None, params=None):
        url = get_config(get_env())['base_url'] + path
        print(url)
        logging.info("requesting get url: {0}".format(url))
        try:
            get_response = requests.get(url, params=params, headers=headers)
            print("*** in  get***")
            return get_response
        except Exception as e:
            # what is the order?
            print(" *** in exception ***")
            assert False
            logging.exception("There was a problem: " + e)

    def post(self, path, json_payload, headers=None, params=None):
        url = get_config(get_env())['base_url'] + path
        print(url)
        logging.info("requesting post url: " + url)
        try:
            post_response = requests.post(url, json=json_payload, params=params, headers=headers)
            return post_response
        except Exception as e:
            assert False
            logging.exception("There was a problem: " + e)

    def delete(self, path, headers=None, params=None):
        url = get_config(get_env())['base_url'] + path
        print(url)
        logging.info("requesting delete url: " + url)
        try:
            delete_response = requests.delete(url, params=params, headers=headers)
            return delete_response
        except Exception as e:
            assert False
            logging.exception("There was a problem: " + e)
