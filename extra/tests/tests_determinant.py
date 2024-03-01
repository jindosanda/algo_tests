import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from determinant import determinant

class TestExercises(unittest.TestCase):
    # only 2x2 matrices
    def test_determinant(self):
        A = [[1, 2], [3, 4]]
        self.assertEqual(determinant(A), -2)
        A = [[1, 2], [4, 5]]
        self.assertEqual(determinant(A), -3)
        A = [[1, 2], [5, 6]]
        self.assertEqual(determinant(A), -4)
        A = [[1, 2], [6, 7]]
        self.assertEqual(determinant(A), -5)
        A = [[1, 2], [7, 8]]
        self.assertEqual(determinant(A), -6)
        A = [[1, 2], [8, 9]]
        self.assertEqual(determinant(A), -7)
    
    def test_determinant_negatives(self):
        A = [[-1, -2], [-3, -4]]
        self.assertEqual(determinant(A), -2)
        A = [[-1, -2], [-4, -5]]
        self.assertEqual(determinant(A), -3)
        A = [[-1, -2], [-5, -6]]
        self.assertEqual(determinant(A), -4)
        A = [[-1, -2], [-6, -7]]
        self.assertEqual(determinant(A), -5)
        A = [[-1, -2], [-7, -8]]
        self.assertEqual(determinant(A), -6)
        A = [[-1, -2], [-8, -9]]
        self.assertEqual(determinant(A), -7)
    
    def test_determinant_zeros(self):
        A = [[0, 0], [0, 0]]
        self.assertEqual(determinant(A), 0)
        A = [[0, 0], [0, 1]]
        self.assertEqual(determinant(A), 0)
        A = [[0, 0], [1, 0]]
        self.assertEqual(determinant(A), 0)
        A = [[0, 0], [1, 1]]
        self.assertEqual(determinant(A), 0)
        A = [[0, 1], [0, 0]]
        self.assertEqual(determinant(A), 0)
        A = [[0, 1], [0, 1]]
        self.assertEqual(determinant(A), 0)
        A = [[0, 1], [1, 0]]
        self.assertEqual(determinant(A), -1)
        A = [[0, 1], [1, 1]]
        self.assertEqual(determinant(A), -1)
        A = [[1, 0], [0, 0]]
        self.assertEqual(determinant(A), 0)
        A = [[1, 0], [0, 1]]
        self.assertEqual(determinant(A), 1)
        A = [[1, 0], [1, 0]]
        self.assertEqual(determinant(A), 0)
        A = [[1, 0], [1, 1]]
        self.assertEqual(determinant(A), 1)
        A = [[1, 1], [0, 0]]
        self.assertEqual(determinant(A), 0)
        A = [[1, 1], [0, 1]]
        self.assertEqual(determinant(A), 1)
        A = [[1, 1], [1, 0]]
        self.assertEqual(determinant(A), -1)
        A = [[1, 1], [1, 1]]
        self.assertEqual(determinant(A), 0)

        
if __name__ == '__main__':
    unittest.main()