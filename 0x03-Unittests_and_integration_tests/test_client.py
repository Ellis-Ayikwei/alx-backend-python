#!/usr/bin/env python3
"""Defines tests for the client module"""

import unittest
import requests
from requests import HTTPError
from typing import Dict
from unittest import mock
from unittest.mock import PropertyMock, patch, MagicMock, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import utils
from fixtures import TEST_PAYLOAD
from utils import (
    get_json,
)


class TestGithubOrgClient(unittest.TestCase):
    """Tests the `GithubOrgClient` class."""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org: str, expected_result: Dict,
                 mock_get_json: MagicMock) -> None:
        """Tests the `org` method."""
        mock_get_json.return_value = expected_result

        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org, expected_result)

        mock_get_json.assert_called_once_with(f"https://api.github.com\
/orgs/{org}")

    def test_public_repos_url(self) -> None:
        with mock.patch('client.GithubOrgClient.org',
                        new_callable=PropertyMock) as mock_e:
            resp = {"repos_url": "https://api.github.com/orgs/google/repos"}

            mock_e.return_value = resp
            myclass = GithubOrgClient("google")
            self.assertEqual(myclass._public_repos_url, resp["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, get_json_mock: MagicMock) -> None:
        """Tests the `public_repos` method."""
        expected_repos_url = "https://api.github.com/orgs/google/repos"
        with mock.patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as public_repos_url_mock:
            get_json_mock.return_value = []
            public_repos_url_mock.return_value = expected_repos_url

            gh_org_client = GithubOrgClient("google")

            self.assertEqual(gh_org_client.public_repos(),
                             get_json_mock.return_value)
            get_json_mock.assert_called_once_with(expected_repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool) -> None:
        """Test has_license"""
        org_client = GithubOrgClient("google")
        client_has_licence = org_client.has_license(repo, key)
        self.assertEqual(client_has_licence, expected)


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    },
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Performs integration tests for the `GithubOrgClient` class.

    The tests are parameterized to run with different payloads.
    """

    @classmethod
    def setUpClass(cls) -> None:
        """Sets up class fixtures before running tests.

        This method is called once before all the tests in the class are run.
        """
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url: str) -> Mock:
            """Returns a Mock object with the response JSON set to the payload
            for the given URL.

            Args:
                url (str): The URL to mock

            Returns:
                Mock: The Mock object with the response JSON set
            """
            if url in route_payload:
                return Mock(**{'json.return_value': route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """Tests the `public_repos` method.

        Verifies that the method returns the expected list of public
        repositories.
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """Tests the `public_repos` method with a license.

        Verifies that the method returns the expected list of public
        repositories that have the specified license.
        """
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """Removes the class fixtures after running all tests.

        This method is called once after all the tests in the class are run.
        """
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
