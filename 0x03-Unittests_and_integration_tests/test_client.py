#!/usr/bin/env python3
"""Defines tests for the client module"""
import unittest
from typing import Dict
from unittest import mock
from unittest.mock import PropertyMock, patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient
import utils
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
    def test_public_repos(
        self, get_json_mock: MagicMock  # type: ignore
    ) -> None:
        """Tests the `public_repos` method.

        Args:
            get_json_mock: A mock for `get_json` function.

        Returns:
            None.
        """
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


if __name__ == '__main__':
    unittest.main()
