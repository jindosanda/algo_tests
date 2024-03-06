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
    def test_array_remove_pos(self):
        A = [1,2,3,4,5]
        array_remove_pos(A,2)
        self.assertEqual(A,[1,2,5,4])
        array_remove_pos(A,2)
        self.assertEqual(A,[1,2,4])
        array_remove_pos(A,0)
        self.assertEqual(A,[4,2])
        array_remove_pos(A,0)
        self.assertEqual(A,[2])
        array_remove_pos(A,0)
        self.assertEqual(A,[])
        A = [1,2,3,4,5]
        array_remove_pos(A,4)
        self.assertEqual(A,[1,2,3,4])
        array_remove_pos(A,0)
        self.assertEqual(A,[4,2,3])
        array_remove_pos(A,1)
        self.assertEqual(A,[4,3])
        
        
if __name__ == '__main__':
    unittest.main()
        