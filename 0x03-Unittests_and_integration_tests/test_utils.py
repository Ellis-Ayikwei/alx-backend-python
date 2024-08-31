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
    """Test memoize decorator"""
    def setUp(self) -> None:
        self.memoize = utils.memoize

    def test_memoize(self) -> None:
        """Test memoize decorator"""
        class TestClass:

            def a_method(self) -> int:
                """Return 42"""
                return 42

            @memoize
            def a_property(self) -> Callable[[], int]:
                """
                A property that memoizes the result of a_method.
                Returns:
                    A callable that returns an int.
                """
                return self.a_method()

        instance = TestClass()
        result = instance.a_property
        self.assertEqual(result, 42)
        result1 = instance.a_property
        self.assertEqual(result, result1)

    def tearDown(self) -> None:
        del self.memoize
        return super().tearDown()


if __name__ == '__main__':
    unittest.main()
