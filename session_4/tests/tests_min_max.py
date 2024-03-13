from contextlib import AbstractContextManager
import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from session4 import min, max
    
class TestExercises(unittest.TestCase):
    def test_min(self):
        A = [1,2,3,4,5]
        self.assertEqual(min(A),1)
        A = [5,4,3,2,1]
        self.assertEqual(min(A),1)
        A = [1,2,3,4,1]
        self.assertEqual(min(A),1)
        A = [1,2,3,4,0]
        self.assertEqual(min(A),0)
        A = [1,2,3,4,5,0]
        self.assertEqual(min(A),0)
        A = [1,2,3,4,5,0,0]
        self.assertEqual(min(A),0)
        A = [1,2,3,4,5,0,0,0]
        self.assertEqual(min(A),0)

    def test_max(self):
        A = [1,2,3,4,5]
        self.assertEqual(max(A),5)
        A = [5,4,3,2,1]
        self.assertEqual(max(A),5)
        A = [1,2,3,4,1]
        self.assertEqual(max(A),4)
        A = [1,2,3,4,0]
        self.assertEqual(max(A),4)
        A = [1,2,3,4,5,0]
        self.assertEqual(max(A),5)
        A = [1,2,3,4,5,0,0]
        self.assertEqual(max(A),5)
        A = [1,2,3,4,5,0,0,0]
        self.assertEqual(max(A),5)

        
        
if __name__ == '__main__':
    unittest.main()
        