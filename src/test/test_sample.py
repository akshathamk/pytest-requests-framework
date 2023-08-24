import pytest
from src.utils.rest_client import RestClient
from config import allure_logs


class TestSample:

    def setup(self):
        print("*** in set up ***")
        self.rest_client = RestClient()
        self.user_id=''

    def test_get(self):
        """
        GET all users
        :return:
        """
        allure_logs("Testing the GET users endpoint")
        path = 'users'
        response = self.rest_client.get(path)
        assert response.status_code == 200
        resp_json = response.json()
        assert resp_json.get('page') is 1

    def test_post(self):
        """
        POST create a new user and get newly generated user id in response
        :return:
        """
        path = 'users'
        name = "sample_user"
        job = "sampler"
        json_body = {
                        "name": name,
                        "job": job
                    }
        response = self.rest_client.post(path=path, json_payload=json_body)
        assert response.status_code == 201
        resp_json = response.json()
        assert resp_json.get('name') == name
        assert resp_json.get('job') == job
        assert "id" in resp_json.keys()
        self.user_id = resp_json.get("id")
        print(self.user_id)

    def test_get_user(self,user_id):
        """
        GET user details by reading user_id via fixtures in conftest.py passed along with pytest command in console
        :param user_id:
        :return:
        """
        path = 'users/'+user_id
        response = self.rest_client.get(path=path)
        assert response.status_code == 200
        resp_json = response.json()
        assert resp_json.get('data').get('id') is int(user_id)

    def teardown_method(self):
        """
        to delete created users, keep state same before and after test run
        :return:
        """
        print("*** in tear down ***")
        if self.user_id:
            print("*** deleting user ***")
            path = 'users/'+self.user_id
            self.rest_client.delete(path=path)

