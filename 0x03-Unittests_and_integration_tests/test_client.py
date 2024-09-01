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
        expected_value = {
            "login": org_name,
            "id": 1,
            "node_id": "1234567890abcdef",
            "url": "https://api.github.com/orgs/google",
            "repos_url": "https://api.github.com/orgs/google/repos",
            "events_url": "https://api.github.com/orgs/google/events",
            "hooks_url": "https://api.github.com/orgs/google/hooks",
            "issues_url": "https://api.github.com/orgs/google/issues",
            "members_url": "https://api.github.com/orgs\
                /google/members{/member}",
            "public_members_url": "https://api.github.\
            com/orgs/google/public_members{/member}",
            "avatar_url": "https://avatars1.githubusercontent.com/u/1?v=4",
            "description": "test"
        }

        # Arrange
        mock_get_json.return_value = expected_value

        # Act
        org_client = GithubOrgClient(org_name)
        result = org_client.org

        # Assert
        mock_get_json.assert_called_once_with(f"https://api.github.\
            com/orgs/{org_name}")
        self.assertEqual(result, expected_value)


if __name__ == '__main__':
    unittest.main()
