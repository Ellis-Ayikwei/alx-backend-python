#!/usr/bin/env python3
"""Defines tests for the utils module"""
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
memoize = utils.memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function
    """
    def setUp(self) -> None:
        self.access_nested_map = access_nested_map

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self,
                               nested_map: Mapping[str, Any],
                               path: Sequence[str],
                               expected_value: Any) -> None:
        """Test access_nested_map function
        """
        self.assertEqual(self.access_nested_map(nested_map, path),
                         expected_value)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map: Mapping[str, Any],
                                         path: Sequence[str]) -> None:
        """Test that a KeyError is raised when a key does not exist in the
        nested map
        """
        with self.assertRaises(KeyError) as cm:
            self.access_nested_map(nested_map, path)

        # Verify the exception message
        expected_message = f"'{path[-1]}'"
        self.assertEqual(str(cm.exception), expected_message)

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


class TestMemoize(unittest.TestCase):
    """Test memoize decorator with the test memoize method"""

    def test_memoize(self):
        """
        Tests the function when calling a_property twice,
        the correct result is returned but a_method is only
        called once using assert_called_once
        """
        class TestClass:
            """ Test Class for wrapping with memoize """

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            instance = TestClass()
            instance.a_property()
            instance.a_property()
            mock_a_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
