#!/usr/bin/env python3
"""Defines tests for the client module"""
import unittest
from typing import Dict
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient
import utils
from utils import (
    get_json,
)


class TestGitHubOrgClient(unittest.TestCase):
    """Defines a class to test the GitHUbOrgClient in the Client Module"""

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock:  MagicMock) -> None:
        """Test org method"""
        expected_resp = {"login":f"{org_name}"}
        mock.return_value = MagicMock(return_value=expected_resp)
        org_client = GithubOrgClient(org_name)
        self.assertEqual(org_client.org(), expected_resp)
        mock.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")


if __name__ == '__main__':
    unittest.main()
