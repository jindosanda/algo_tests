from contextlib import AbstractContextManager
import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from session5 import merge_intervals


class LargestSubarraySum(unittest.TestCase):
    def tests_merge_intervals(self):
        intervals = [[1,3],[2,6],[8,10],[15,18]]
        self.assertEqual(merge_intervals(intervals), [[1,6],[8,10],[15,18]])

    
    def tests_merge_intervals_2(self):
        intervals = [[1,4],[4,5]]
        self.assertEqual(merge_intervals(intervals), [[1,5]])

    def tests_merge_intervals_3(self):
        intervals = [[1,4],[0,4]]
        self.assertEqual(merge_intervals(intervals), [[0,4]])

    def tests_merge_intervals_4(self):
        intervals = [[1,4],[2,3]]
        self.assertEqual(merge_intervals(intervals), [[1,4]])

    def tests_merge_intervals_5(self):
        intervals = [[1,4],[0,0]]
        self.assertEqual(merge_intervals(intervals), [[0,0],[1,4]])
        
if __name__ == '__main__':
    unittest.main()
        