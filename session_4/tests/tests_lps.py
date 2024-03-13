from contextlib import AbstractContextManager
import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from session4 import lps
    
class TestExercises(unittest.TestCase):
    def test_lps(self):
        self.assertEqual(lps('babad'),'bab' or 'aba')
        self.assertEqual(lps('cbbd'),'bb')
        self.assertEqual(lps('a'),'a')
        self.assertEqual(lps('ac'),'a')
        self.assertEqual(lps('bb'),'bb')
        self.assertEqual(lps('ccc'),'ccc')
        self.assertEqual(lps('aaaa'),'aaaa')
        self.assertEqual(lps('racecarlevel'),'racecar')

        
        
if __name__ == '__main__':
    unittest.main()
        