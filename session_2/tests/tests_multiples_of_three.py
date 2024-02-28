import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from multiples_of_three import multiples_of_three

class TestExercises(unittest.TestCase):
    def test_multiples_of_three(self):
        self.assertEqual(multiples_of_three([1, 2, 3, 4, 5]), 1)
        self.assertEqual(multiples_of_three([1, 2, 3, 4, 5, 6]), 2)
        self.assertEqual(multiples_of_three([1, 2, 3, 4, 5, 6, 7, 8, 9]), 3)
        self.assertEqual(multiples_of_three([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 3)
        self.assertEqual(multiples_of_three([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), 3)
        self.assertEqual(multiples_of_three([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), 4)
        self.assertEqual(multiples_of_three([34, 31, 45, 5, 38, 19, 19, 26, 25, 19, 39, 40]), 2)
        self.assertEqual(multiples_of_three([7, 2, 0]), 1)

    def test_multiples_of_three_empty(self):
        self.assertEqual(multiples_of_three([]), 0)

    def test_multiples_of_three_negative(self):
        self.assertEqual(multiples_of_three([-1, -2, -3, -4, -5]), 1)
        self.assertEqual(multiples_of_three([-1, -2, -3, -4, -5, -6]), 2)
        self.assertEqual(multiples_of_three([-1, -2, -3, -4, -5, -6, -7, -8, -9]), 3)
        self.assertEqual(multiples_of_three([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), 3)
        self.assertEqual(multiples_of_three([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]), 3)
        self.assertEqual(multiples_of_three([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]), 4)
        self.assertEqual(multiples_of_three([-34, -31, -45, -5, -38, -19, -19, -26, -25, -19, -39, -40]), 2)
        self.assertEqual(multiples_of_three([-7, -2, 0]), 1)

    def test_multiples_of_three_float(self):
        self.assertEqual(multiples_of_three([1.0, 2.0, 3.0, 4.0, 5.0]), 1)
        self.assertEqual(multiples_of_three([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]), 2)
        self.assertEqual(multiples_of_three([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]), 3)
        self.assertEqual(multiples_of_three([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]), 3)
        self.assertEqual(multiples_of_three([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0]), 3)
        self.assertEqual(multiples_of_three([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]), 4)
        self.assertEqual(multiples_of_three([34.0, 31.0, 45.0, 5.0, 38.0, 19.0, 19.0, 26.0, 25.0, 19.0, 39.0, 40.0]), 2)
        self.assertEqual(multiples_of_three([7.0, 2.0, 0.0]), 1)
    
    def test_multiples_of_three_mixed(self):
        self.assertEqual(multiples_of_three([1, 2.0, 3, 4.0, 5]), 1)
        self.assertEqual(multiples_of_three([1, 2.0, 3, 4.0, 5, 6.0]), 2)
        self.assertEqual(multiples_of_three([1, 2.0, 3, 4.0, 5, 6.0, 7, 8.0, 9]), 3)
        self.assertEqual(multiples_of_three([1, 2.0, 3, 4.0, 5, 6.0, 7, 8.0, 9, 10.0]), 3)
        self.assertEqual(multiples_of_three([1, 2.0, 3, 4.0, 5, 6.0, 7, 8.0, 9, 10.0, 11]), 3)
        self.assertEqual(multiples_of_three([1, 2.0, 3, 4.0, 5, 6.0, 7, 8.0, 9, 10.0, 11, 12.0]), 4)
        self.assertEqual(multiples_of_three([34, 31.0, 45, 5.0, 38, 19, 19.0, 26, 25, 19.0, 39, 40]), 2)
        self.assertEqual(multiples_of_three([7, 2.0, 0]), 1)
        
if __name__ == '__main__':
    unittest.main()