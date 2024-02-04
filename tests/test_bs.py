from binary_search.bs import binary
import unittest

class TestBinarySearchFunction(unittest.TestCase):

    def test_bs(self):
        # Test case 1: Search for an item in the middle of the list
        self.assertEqual(binary([1, 2, 3, 4, 5], 3), 2)

        # Test case 2: Search for an item at the beginning of the list
        self.assertEqual(binary([1, 2, 3, 4, 5], 1), 0)

        # Test case 3: Search for an item at the end of the list
        self.assertEqual(binary([1, 2, 3, 4, 5], 5), 4)

        # Test case 4: Search for an item not in the list
        self.assertIsNone(binary([1, 2, 3, 4, 5], 6))

        # Test case 5: Search for an item in an empty list
        self.assertIsNone(binary([], 42))

if __name__ == '__main__':
    unittest.main()
