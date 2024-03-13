from contextlib import AbstractContextManager
import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from session4 import find_peak
    
class TestExercises(unittest.TestCase):
    def test_find_peak(self):
        self.assertEqual(find_peak([1, 3, 20, 4, 1, 0]),20)
        self.assertEqual(find_peak([1, 3, 20, 4, 1, 0, 1]),20)
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

    def tests_find_peak_flat(self):
        self.assertEqual(find_peak([0,0,0,0]),0)
        self.assertEqual(find_peak([1,1,1,1]),1)
        self.assertEqual(find_peak([2,2,2,2]),2)
        self.assertEqual(find_peak([3,3,3,3]),3)
        self.assertEqual(find_peak([4,4,4,4]),4)
        self.assertEqual(find_peak([5,5,5,5]),5)
        self.assertEqual(find_peak([6,6,6,6]),6)
        self.assertEqual(find_peak([7,7,7,7]),7)
        self.assertEqual(find_peak([8,8,8,8]),8)
        self.assertEqual(find_peak([9,9,9,9]),9)
        self.assertEqual(find_peak([10,10,10,10]),10)

    def tests_find_peak_negative(self):
        self.assertEqual(find_peak([-1,-3,-20,-4,-1,0]),0)
        self.assertEqual(find_peak([-1,-3,-20,-4,-1,0,-1]),0)
        self.assertEqual(find_peak([-1,-2,-3]),-1)
        self.assertEqual(find_peak([-1,-2,-7,-8,-9]),-1)
        self.assertEqual(find_peak([-9,-6,-5]),-5)
        self.assertEqual(find_peak([-1,-2,-1,-3]),-1)
        self.assertEqual(find_peak([-1,-2,-1,0,-3]),0)
        self.assertEqual(find_peak([-1,-2,-3,-2,-1]),-1)
        self.assertEqual(find_peak([-1,-2,-3,-4]),-1)
        self.assertEqual(find_peak([-1,-2]),-1)
        self.assertEqual(find_peak([-4,-7,-4]),-4)
        self.assertEqual(find_peak([-7]),-7)
        self.assertEqual(find_peak([-7,-4]),-4)
        self.assertEqual(find_peak([-4,-7]),-4)

        
        
if __name__ == '__main__':
    unittest.main()
        