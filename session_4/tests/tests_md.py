from contextlib import AbstractContextManager
import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from session4 import md
    
class TestExercises(unittest.TestCase):
    # test maximal difference
    def test_md(self):
        self.assertEqual(md([2, 1, 5, 9, 4, 10, 8]),9)
        self.assertEqual(md([2, 1, 5, 9, 4, 10, 8, 6]),9)
        self.assertEqual(md([2, 1, 5, 9, 4, 10, 8, 6, 3]),9)
        self.assertEqual(md([1]),0)
        self.assertEqual(md([1, 1, 1]),0)
        self.assertEqual(md([10, -3, 4, 11, 0, 9]),14)


        
        
if __name__ == '__main__':
    unittest.main()
        