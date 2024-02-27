import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from count_lower import count_lower

class TestExercises(unittest.TestCase):
    def test_count_lower(self):
        self.assertEqual(count_lower([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(count_lower([1, 2, 3, 4, 5], 6), 5)
        self.assertEqual(count_lower([1, 2, 3, 4, 5], 0), 0)
        self.assertEqual(count_lower([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(count_lower([1, 2, 3, 4, 5], 1), 0)
    
    def test_count_lower_empty(self):
        self.assertEqual(count_lower([], 3), 0)
    
    def test_count_lower_negative(self):
        self.assertEqual(count_lower([-1, -2, -3, -4, -5], -3), 2)
        self.assertEqual(count_lower([-1, -2, -3, -4, -5], -6), 0)
        self.assertEqual(count_lower([-1, -2, -3, -4, -5], 0), 5)
        self.assertEqual(count_lower([-1, -2, -3, -4, -5], -5), 0)
        self.assertEqual(count_lower([-1, -2, -3, -4, -5], -1), 4)

    def test_count_lower_float(self):
        self.assertEqual(count_lower([1.1, 2.2, 3.3, 4.4, 5.5], 3.3), 2)
        self.assertEqual(count_lower([1.1, 2.2, 3.3, 4.4, 5.5], 6.6), 5)
        self.assertEqual(count_lower([1.1, 2.2, 3.3, 4.4, 5.5], 0.0), 0)
        self.assertEqual(count_lower([1.1, 2.2, 3.3, 4.4, 5.5], 5.5), 4)
        self.assertEqual(count_lower([1.1, 2.2, 3.3, 4.4, 5.5], 1.1), 0)

    def test_count_lower_mixed(self):
        self.assertEqual(count_lower([1, 2.2, 3, 4.4, 5], 3), 2)
        self.assertEqual(count_lower([1, 2.2, 3, 4.4, 5], 6), 5)
        self.assertEqual(count_lower([1, 2.2, 3, 4.4, 5], 0), 0)
        self.assertEqual(count_lower([1, 2.2, 3, 4.4, 5], 5), 4)
        self.assertEqual(count_lower([1, 2.2, 3, 4.4, 5], 1), 0)

    def test_count_lower_string(self):
        self.assertEqual(count_lower(['a', 'b', 'c', 'd', 'e'], 'c'), 2)
        self.assertEqual(count_lower(['a', 'b', 'c', 'd', 'e'], 'f'), 5)
        self.assertEqual(count_lower(['a', 'b', 'c', 'd', 'e'], '0'), 0)
        self.assertEqual(count_lower(['a', 'b', 'c', 'd', 'e'], 'e'), 4)
        self.assertEqual(count_lower(['a', 'b', 'c', 'd', 'e'], 'a'), 0)

if __name__ == '__main__':
    unittest.main()