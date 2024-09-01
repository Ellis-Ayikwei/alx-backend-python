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
        ('google', {'login': 'google'}),
        ('abc', {'login': 'abc'}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, expected_result: Dict[str, str],
                 mock: unittest.mock.MagicMock) -> None:
        """Test org method
        
        Args:
        org_name (str): The organization name
        expected_result (Dict[str, str]): The expected result
        mock (unittest.mock.MagicMock): The mock object
        
        Returns:
        None
        """
        mock.return_value = expected_result
        org_client = GithubOrgClient(org_name)
        org_client.org
        mock.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")


if __name__ == '__main__':
    unittest.main()
