from contextlib import AbstractContextManager
import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from session4 import prime_factorize
    
class TestExercises(unittest.TestCase):
    def test_prime_factorize(self):
        self.assertEqual(prime_factorize(2312).strip(), "2E3 17E2")
        self.assertEqual(prime_factorize(10242311).strip(), "19 701 769")
        self.assertEqual(prime_factorize(1).strip(), "")
        self.assertEqual(prime_factorize(2).strip(), "2")
        self.assertEqual(prime_factorize(3).strip(), "3")
        self.assertEqual(prime_factorize(4).strip(), "2E2")
        self.assertEqual(prime_factorize(5).strip(), "5")
        self.assertEqual(prime_factorize(6).strip(), "2 3")
        self.assertEqual(prime_factorize(7).strip(), "7")
        self.assertEqual(prime_factorize(8).strip(), "2E3")
        self.assertEqual(prime_factorize(9).strip(), "3E2")
        self.assertEqual(prime_factorize(10).strip(), "2 5")
        self.assertEqual(prime_factorize(11).strip(), "11")
        self.assertEqual(prime_factorize(12).strip(), "2E2 3")
        self.assertEqual(prime_factorize(13).strip(), "13")
        self.assertEqual(prime_factorize(14).strip(), "2 7")
        self.assertEqual(prime_factorize(15).strip(), "3 5")
        self.assertEqual(prime_factorize(16).strip(), "2E4")
        self.assertEqual(prime_factorize(17).strip(), "17")
        self.assertEqual(prime_factorize(18).strip(), "2 3E2")


        
        
if __name__ == '__main__':
    unittest.main()
        