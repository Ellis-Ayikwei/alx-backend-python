import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map function
    """
    def setUp(self):
        self.access_nested_map = access_nested_map

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), 2),
        ({"a": {"b": 2}}, ("a", "b"), 2)
        ])
    def test_access_nested_map(self, nested_map: Mapping[str, Any],
                               path: Sequence[str], expected_outcome: Any) -> None:
        """Test access_nested_map function

        Args:
            nested_map (Mapping[str, Any]): A dictionary with nested values
            path (Sequence[str]): A sequence of keys used to access a value
            expected_outcome (Any): The expected outcome of the function

        Returns:
            None
        """
        self.assertEqual(self.access_nested_map(nested_map, path),
                         expected_outcome)


if __name__ == '__main__':
    unittest.main()
