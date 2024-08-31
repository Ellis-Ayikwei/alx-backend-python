#!/usr/bin/env python3
import unittest
from parameterized import parameterized
import utils
from unittest.mock import patch, PropertyMock
import requests
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)
access_nested_map = utils.access_nested_map
get_json = utils.get_json

class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function
    """
    def setUp(self) -> None:
        self.access_nested_map = access_nested_map

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), 2),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, input_map: Mapping,
                               input_path: Sequence,
                               expected_value: Any) -> None:
        """Test access_nested_map function

        Args:
            input_map (Mapping[str, Any]): A dictionary with nested values
            input_path (Sequence[str]): A sequence of keys used to access a value
            expected_value (Any): The expected outcome of the function

        Returns:
            None
        """
        self.assertEqual(self.access_nested_map(input_map, input_path),
                         expected_value)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_raises_key_error_on_invalid_key(
        self, input_map: Mapping, input_path: Sequence
    ) -> None:
        """Test that a KeyError is raised when a key does not exist in the
        nested map

        Args:
            input_map (Mapping[str, Any]): A dictionary with nested values
            input_path (Sequence[str]): A sequence of keys used to access a value

        Returns:
            None
        """
        with self.assertRaises(KeyError):
            self.access_nested_map(input_map, input_path)


    def tearDown(self) -> None:
        del self.access_nested_map
        return super().tearDown()

class TestGetJson(unittest.TestCase):
    """Test get_json function"""
    def setUp(self) -> None:
        self.get_json = get_json

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, url: str, expected_payload: Dict) -> None:
        """Test get_json function"""
        with patch('requests.get') as mock_get:
            mock_get.return_value.json.return_value = expected_payload
            payload = self.get_json(url)
            self.assertEqual(payload, expected_payload)



if __name__ == '__main__':
    unittest.main()
