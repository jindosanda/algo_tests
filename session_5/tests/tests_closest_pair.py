from contextlib import AbstractContextManager
import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from session5 import closest_pair


class LargestSubarraySum(unittest.TestCase):
    def test_closest_pair(self):
        A = [1, 7, 5, 3, 32, 9]
        B = [2, 3, 4, 5, 6, 7]
        n = 15
        self.assertEqual(closest_pair(A, B, n), (9, 6))

    def test_closest_pair_2(self):
        A = [1, 7, 5, 3, 32, 9]
        B = [2, 3, 4, 5, 6, 7]
        n = 25
        self.assertTrue( closest_pair(A, B, n) in [(9, 7), (32, 2)] )
        
    def test_closest_pair_3(self):
        A = [1, 1, 1, 1, 1]
        B = [2, 2, 2, 2, 2]
        n = 5
        self.assertEqual(closest_pair(A, B, n), (1, 2))

    def test_closest_pair_4(self):
        A = [1, 10, 100, 1000, 10000]
        B = [2, 3, 4, 5, 6]
        n = 10000
        self.assertEqual(closest_pair(A, B, n), (10000, 2))

        
        
        
if __name__ == '__main__':
    unittest.main()
        