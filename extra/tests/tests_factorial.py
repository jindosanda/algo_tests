import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from factorial import factorial

class TestExercises(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(7), 5040)
        self.assertEqual(factorial(8), 40320)
        self.assertEqual(factorial(9), 362880)
        self.assertEqual(factorial(10), 3628800)
        self.assertEqual(factorial(11), 39916800)
        self.assertEqual(factorial(12), 479001600)
        self.assertEqual(factorial(13), 6227020800)
        self.assertEqual(factorial(14), 87178291200)
        self.assertEqual(factorial(15), 1307674368000)
        self.assertEqual(factorial(16), 20922789888000)
        self.assertEqual(factorial(17), 355687428096000)
        self.assertEqual(factorial(18), 6402373705728000)
        self.assertEqual(factorial(19), 121645100408832000)
        self.assertEqual(factorial(20), 2432902008176640000)
        self.assertEqual(factorial(21), 51090942171709440000)
        self.assertEqual(factorial(22), 1124000727777607680000)
        self.assertEqual(factorial(23), 25852016738884976640000)


        

        
if __name__ == '__main__':
    unittest.main()