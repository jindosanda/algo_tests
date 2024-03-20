from contextlib import AbstractContextManager
import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from largest_subarray_sum import largest_subarray_sum


class LargestSubarraySum(unittest.TestCase):
    def test_basic(self):
        A = [1,-4, 2, 1, -2]
        self.assertEqual(largest_subarray_sum(A), 3)
        
    def test_ones(self):  
        A = [1, 1, 1, 1, 1]
        self.assertEqual(largest_subarray_sum(A), 5)
        
    def test_negative(self):      
        A = [-6, -7, -3, -2]
        self.assertEqual(largest_subarray_sum(A), 0)
        
    def test_jump(self):      
        A = [1, 2, 3, 4, -9, 95]
        self.assertEqual(largest_subarray_sum(A), 96)
        
    def test_empty(self):  
        A = []
        self.assertEqual(largest_subarray_sum(A), 0)
        
    def test_zero(self):      
        A = [8, 2, 4, 9, 0]
        self.assertEqual(largest_subarray_sum(A), 23)
        
        
        
if __name__ == '__main__':
    unittest.main()
        