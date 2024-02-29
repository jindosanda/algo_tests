import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from fibonacci import fibonacci

class TestExercises(unittest.TestCase):
    def test_fibonacci(self):
        # self.assertEqual(fibonacci(0), None)
        self.assertEqual(fibonacci(1), [0])
        self.assertEqual(fibonacci(2), [0, 1])
        self.assertEqual(fibonacci(3), [0, 1, 1])
        self.assertEqual(fibonacci(4), [0, 1, 1, 2])
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        self.assertEqual(fibonacci(6), [0, 1, 1, 2, 3, 5])
        self.assertEqual(fibonacci(7), [0, 1, 1, 2, 3, 5, 8])
        self.assertEqual(fibonacci(8), [0, 1, 1, 2, 3, 5, 8, 13])
        self.assertEqual(fibonacci(9), [0, 1, 1, 2, 3, 5, 8, 13, 21])
        self.assertEqual(fibonacci(10), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
        self.assertEqual(fibonacci(11), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55])
        self.assertEqual(fibonacci(12), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
        self.assertEqual(fibonacci(13), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144])
        self.assertEqual(fibonacci(14), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233])
        self.assertEqual(fibonacci(15), [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377])
    

        

        
if __name__ == '__main__':
    unittest.main()