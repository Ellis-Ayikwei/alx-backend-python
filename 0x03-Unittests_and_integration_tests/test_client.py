#!/usr/bin/env python3
"""Defines tests for the client module"""
import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient
import utils
from utils import (
    get_json,
)


class TestGitHubOrgClient(unittest.TestCase):
    """Defines a class to test the GitHUbOrgClient in the Client Module"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org method"""
        org_client = GithubOrgClient(org_name)
        result = org_client.org
        mock_get_json.assert_called_once_with(f"https://api.github.\
com/orgs/{org_name}")


if __name__ == '__main__':
    unittest.main()
