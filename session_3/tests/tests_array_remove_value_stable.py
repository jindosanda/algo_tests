from contextlib import AbstractContextManager
import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from array_rem import array_remove_pos, array_remove_value, array_remove_value_stable
import random 

def test_time():
    A_len = random.randint(10000,100000)
    A = [random.randint(0,100) for _ in range(A_len)]
    array_remove_pos(A,random.randint(0,A_len-1))
    
class TestExercises(unittest.TestCase):
    def test_array_remove_value_stable(self):
        A = [7, 5, 2, 3, 5, 7, 3, 4, 2, 1]
        array_remove_value_stable(A, 7)
        self.assertEqual(A,[5, 2, 3, 5, 3, 4, 2, 1])
        array_remove_value_stable(A, 5)
        self.assertEqual(A,[2, 3, 3, 4, 2, 1])
        array_remove_value_stable(A, 3)
        self.assertEqual(A,[2, 4, 2, 1])
        array_remove_value_stable(A, 2)
        self.assertEqual(A,[4, 1])
        array_remove_value_stable(A, 1)
        self.assertEqual(A,[4])
        array_remove_value_stable(A, 4)
        self.assertEqual(A,[])

    def test_array_remove_value_stable_2(self):
        A = [1,1,1,1,1,1,1,1,1,1]
        array_remove_value_stable(A, 1)
        self.assertEqual(A,[])
    
    def test_array_remove_value_stable_3(self):
        A = [1,2,3,4,5]
        array_remove_value_stable(A, 6)
        self.assertEqual(A,[1,2,3,4,5])

    def test_array_remove_value_stable_4(self):
        A = [1,2,3,4,5]
        array_remove_value_stable(A, 1)
        self.assertEqual(A,[2,3,4,5])

    def test_array_remove_value_stable_5(self):
        A = [1,2,3,4,5,5]
        array_remove_value_stable(A, 5)
        self.assertEqual(A,[1,2,3,4])



        
if __name__ == '__main__':
    unittest.main()
        