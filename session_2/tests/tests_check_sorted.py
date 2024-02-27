import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from check_sorted import check_sorted

class TestExercises(unittest.TestCase):
    def test_check_sorted(self):
        self.assertEqual(check_sorted([1, 2, 3, 4, 5]), True)
        self.assertEqual(check_sorted([1, 2, 3, 4, 5, 6]), True)
        self.assertEqual(check_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9]), True)
        self.assertEqual(check_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), True)
        self.assertEqual(check_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]), True)
        self.assertEqual(check_sorted([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), True)
        self.assertEqual(check_sorted([34, 31, 45, 5, 38, 19, 19, 26, 25, 19, 39, 40]), False)
        self.assertEqual(check_sorted([7, 2, 0]), False)

    def test_check_sorted_empty(self):
        self.assertEqual(check_sorted([]), True)

    def test_check_sorted_negative(self):
        self.assertEqual(check_sorted([-1, -2, -3, -4, -5]), False)
        self.assertEqual(check_sorted([-1, -2, -3, -4, -5, -6]), False)
        self.assertEqual(check_sorted([-1, -2, -3, -4, -5, -6, -7, -8, -9]), False)
        self.assertEqual(check_sorted([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), False)
        self.assertEqual(check_sorted([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11]), False)
        self.assertEqual(check_sorted([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, -11, -12]), False)
        self.assertEqual(check_sorted([-34, -31, -45, -5, -38, -19, -19, -26, -25, -19, -39, -40]), False)
        self.assertEqual(check_sorted([-7, -2, 0]), True)

    def test_check_sorted_float(self):
        self.assertEqual(check_sorted([1.0, 2.0, 3.0, 4.0, 5.0]), True)
        self.assertEqual(check_sorted([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]), True)
        self.assertEqual(check_sorted([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]), True)
        self.assertEqual(check_sorted([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]), True)
        self.assertEqual(check_sorted([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0]), True)
        self.assertEqual(check_sorted([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0]), True)
        self.assertEqual(check_sorted([34.0, 31.0, 45.0, 5.0, 38.0, 19.0, 19.0, 26.0, 25.0, 19.0, 39.0, 40.0]), False)
        self.assertEqual(check_sorted([7.0, 2.0, 0.0]), False)

    def test_check_sorted_mixed(self):
        self.assertEqual(check_sorted([1, 2.0, 3, 4.0, 5]), True)
        self.assertEqual(check_sorted([1, 2.0, 3, 4.0, 5, 6.0]), True)
        self.assertEqual(check_sorted([1, 2.0, 3, 4.0, 5, 6.0, 7, 8.0, 9]), True)
        self.assertEqual(check_sorted([1, 2.0, 3, 4.0, 5, 6.0, 7, 8.0, 9, 10.0]), True)
        self.assertEqual(check_sorted([1, 2.0, 3, 4.0, 5, 6.0, 7, 8.0, 9, 10.0, 11]), True)
        self.assertEqual(check_sorted([1, 2.0, 3, 4.0, 5, 6.0, 7, 8.0, 9, 10.0, 11, 12.0]), True)
        self.assertEqual(check_sorted([34, 31.0, 45, 5.0, 38, 19, 19.0, 26, 25, 19.0, 39, 40]), False)
        self.assertEqual(check_sorted([7, 2.0, 0]), False)

        
if __name__ == '__main__':
    unittest.main()