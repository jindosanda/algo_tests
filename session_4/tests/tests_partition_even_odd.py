from contextlib import AbstractContextManager
import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from session4 import partition_even_odd

# Check if A contains a list of even numbers followed by odd numbers
def check_partition_even_odd( A ):
    even = True
    for i in range(len(A)):
        if A[i] % 2 == 0:
            if not even:
                return False
        else:
            even = False
    return True

class TestExercises(unittest.TestCase):
    def test_partition_even_odd(self):
        A = [-1,1,7,5,-2,1,2,7,7,5,5,1,1,4,1]
        partition_even_odd(A)
        self.assertTrue(check_partition_even_odd(A))

        A = [1,2,3,4,5,6,7,8,9,10]
        partition_even_odd(A)
        self.assertTrue(check_partition_even_odd(A))

        A = [1,1,1,1,1,1,1,1,1,1]
        partition_even_odd(A)
        self.assertTrue(check_partition_even_odd(A))

        A = [2,2,2,2,2,2,2,2,2,2]
        partition_even_odd(A)
        self.assertTrue(check_partition_even_odd(A))

        A = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
        partition_even_odd(A)
        self.assertTrue(check_partition_even_odd(A))

        A = [i for i in range(100)]
        partition_even_odd(A)
        self.assertTrue(check_partition_even_odd(A))

        A = [i for i in range(100,0,-1)]
        partition_even_odd(A)
        self.assertTrue(check_partition_even_odd(A))

        A = [i for i in range(100,0,2)]
        partition_even_odd(A)
        self.assertTrue(check_partition_even_odd(A))
        
if __name__ == '__main__':
    unittest.main()
        