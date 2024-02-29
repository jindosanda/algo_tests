import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from unique import unique

class TestExercises(unittest.TestCase):
    def test_unique(self):
        self.assertEqual(unique("unique"), False)
        self.assertEqual(unique("uniq"), True)
        self.assertEqual(unique("un"), True)
        self.assertEqual(unique("u"), True)
        self.assertEqual(unique(""), True)
        self.assertEqual(unique("hello"), False)
        self.assertEqual(unique("world"), True)
        self.assertEqual(unique("python"), True)
        self.assertEqual(unique("java"), False)
        self.assertEqual(unique("javascript"), False)
        self.assertEqual(unique("ruby"), True)
        self.assertEqual(unique("perl"), True)
        self.assertEqual(unique("php"), False)
        self.assertEqual(unique("c"), True)
        self.assertEqual(unique("c++"), False)
        
        


        

        
if __name__ == '__main__':
    unittest.main()