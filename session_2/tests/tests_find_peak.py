import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from find_peak import find_peak

class TestExercises(unittest.TestCase):
   def test_find_peak(self):
        self.assertEqual(find_peak([1, 2, 3, 4, 5]), 5)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6]), 6)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9]), 9)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 11)
        self.assertEqual(find_peak([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 12)
        self.assertEqual(find_peak([34, 31, 45, 5, 38, 19, 19, 26, 25, 19, 39, 40]), 45)
        self.assertEqual(find_peak([7, 2, 0]), 7)
        self.assertEqual(find_peak([1,2,3]),3)
        self.assertEqual(find_peak([1,2,7,8,9]),9)
        self.assertEqual(find_peak([9,6,5]),9)
        self.assertEqual(find_peak([1,2,1,-3]),2)
        self.assertEqual(find_peak([1,2,1,0,-3]),2)
        self.assertEqual(find_peak([1,2,3,2,1]),3)
        self.assertEqual(find_peak([1,2,3,4]),4)
        self.assertEqual(find_peak([1,2]),2)
        self.assertEqual(find_peak([4,7,4]),7)
        self.assertEqual(find_peak([7]),7)
        self.assertEqual(find_peak([7,4]),7)
        self.assertEqual(find_peak([4,7]),7)

if __name__ == '__main__':
    unittest.main()