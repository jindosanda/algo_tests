import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from partition_even_odd import partition_even_odd

def check_partition_even_odd( A ):
    for i in range(len(A)-1):
        if A[i] % 2 == 1:
            for j in range(i+1, len(A)):
                if A[j] % 2 == 0:
                    return False
    return True


class TestExercises(unittest.TestCase):
    def test_partition_even_odd(self):
        A = [1, 2, 3, 4, 5]
        partition_even_odd( A )
        self.assertEqual(check_partition_even_odd( A ), True)

        A = [1, 2, 3, 4, 5, 6]
        partition_even_odd( A )
        self.assertEqual(check_partition_even_odd( A ), True)

        A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        partition_even_odd( A )
        self.assertEqual(check_partition_even_odd( A ), True)

        A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        partition_even_odd( A )
        self.assertEqual(check_partition_even_odd( A ), True)

    def test_partition_even_odd_empty(self):
        A = []
        partition_even_odd( A )
        self.assertEqual(check_partition_even_odd( A ), True)

    def test_partition_even_odd_negative(self):
        A = [-1, -2, -3, -4, -5]
        partition_even_odd( A )
        self.assertEqual(check_partition_even_odd( A ), True)

        A = [-1, -2, -3, -4, -5, -6]
        partition_even_odd( A )
        self.assertEqual(check_partition_even_odd( A ), True)

        A = [-1, -2, -3, -4, -5, -6, -7, -8, -9]
        partition_even_odd( A )
        self.assertEqual(check_partition_even_odd( A ), True)

        A = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
        partition_even_odd( A )
        self.assertEqual(check_partition_even_odd( A ), True)

    

        
    
        
if __name__ == '__main__':
    unittest.main()