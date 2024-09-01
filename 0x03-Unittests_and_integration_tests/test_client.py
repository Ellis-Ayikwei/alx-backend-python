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


class TestGithubOrgClient(unittest.TestCase):
    """Tests the `GithubOrgClient` class."""

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org: str, expected_result: Dict, mock_get_json: MagicMock) -> None:
        """Tests the `org` method."""
        mock_get_json.return_value = expected_result  # Directly return the expected result

        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org, expected_result)  # Make sure to access the property directly

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org}")


if __name__ == '__main__':
    unittest.main()
