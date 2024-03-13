from contextlib import AbstractContextManager
import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from session4 import palindrome
    
class TestExercises(unittest.TestCase):
    def tests_palindrome(self):
        self.assertEqual(palindrome('aba'),True)
        self.assertEqual(palindrome('abba'),True)
        self.assertEqual(palindrome('abcba'),True)
        self.assertEqual(palindrome('abccba'),True)
        self.assertEqual(palindrome('racecar'),True)
        self.assertEqual(palindrome('level'),True)
        self.assertEqual(palindrome('rotator'),True)
    
    def tests_palindrome_false(self):
        self.assertEqual(palindrome('ab'),False)
        self.assertEqual(palindrome('abc'),False)
        self.assertEqual(palindrome('abca'),False)
        self.assertEqual(palindrome('abcc'),False)
        self.assertEqual(palindrome('racecar1'),False)
        self.assertEqual(palindrome('level1'),False)
        self.assertEqual(palindrome('rotator1'),False)
        
if __name__ == '__main__':
    unittest.main()
        