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
    
    
    def test_access_nested_map(self, nested_map, path, expected_outcome):
        """Test access_nested_map function"""
        self.assertEqual(self.access_nested_map(nested_map, path), expected_outcome)
        
        
if __name__ == '__main__':
    unittest.main()
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
    
    
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, expected_outcome: Any) -> Any:
        """Test access_nested_map function"""
        self.assertEqual(self.access_nested_map(nested_map, path), expected_outcome)
        
        
if __name__ == '__main__':
    unittest.main()