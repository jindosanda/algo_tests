import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from ex290 import square_root

class TestExercises(unittest.TestCase):
    def test_square_root(self):
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(1), 1)
        self.assertEqual(square_root(2), 1)
        self.assertEqual(square_root(3), 1)
        self.assertEqual(square_root(4), 2)
        self.assertEqual(square_root(5), 2)
        self.assertEqual(square_root(6), 2)
        self.assertEqual(square_root(7), 2)
        self.assertEqual(square_root(8), 2)
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(10), 3)
        self.assertEqual(square_root(11), 3)
        self.assertEqual(square_root(12), 3)
        self.assertEqual(square_root(13), 3)
        self.assertEqual(square_root(14), 3)
        self.assertEqual(square_root(15), 3)
        self.assertEqual(square_root(16), 4)
        self.assertEqual(square_root(17), 4)
        self.assertEqual(square_root(18), 4)
        self.assertEqual(square_root(19), 4)
        self.assertEqual(square_root(20), 4)
        self.assertEqual(square_root(21), 4)
        self.assertEqual(square_root(22), 4)
        self.assertEqual(square_root(23), 4)
        self.assertEqual(square_root(24), 4)
        self.assertEqual(square_root(25), 5)
        self.assertEqual(square_root(26), 5)
        self.assertEqual(square_root(27), 5)
        self.assertEqual(square_root(28), 5)
        self.assertEqual(square_root(29), 5)
        self.assertEqual(square_root(30), 5)
        self.assertEqual(square_root(31), 5)
        self.assertEqual(square_root(32), 5)
        self.assertEqual(square_root(33), 5)
        self.assertEqual(square_root(34), 5)
        self.assertEqual(square_root(35), 5)
        self.assertEqual(square_root(36), 6)
        self.assertEqual(square_root(37), 6)
        self.assertEqual(square_root(38), 6)
        self.assertEqual(square_root(39), 6)
        self.assertEqual(square_root(40), 6)
        self.assertEqual(square_root(41), 6)
        self.assertEqual(square_root(42), 6)
        self.assertEqual(square_root(43), 6)
        self.assertEqual(square_root(44), 6)
    
        
if __name__ == '__main__':
    unittest.main()
        