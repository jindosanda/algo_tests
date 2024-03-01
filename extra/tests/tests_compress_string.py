import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from compress_string import compress_string
# include all modules in exercises directory
# from exercises import *

class TestExercises(unittest.TestCase):
    def test_compress_string(self):
        self.assertEqual(compress_string("aabcccccaaa"), "a2b1c5a3")
        self.assertEqual(compress_string("aabbcc"), "aabbcc")
        self.assertEqual(compress_string("aa"), "aa")
        self.assertEqual(compress_string("a"), "a")
        self.assertEqual(compress_string("abc"), "abc")
        self.assertEqual(compress_string("aabbccaa"), "aabbccaa")
        self.assertEqual(compress_string("aabbccaaa"), "a2b2c2a3")
        self.assertEqual(compress_string("aabbccaaaa"), "a2b2c2a4")
        self.assertEqual(compress_string("aabbccaaaaa"), "a2b2c2a5")
        self.assertEqual(compress_string("aabbccaaaaaa"), "a2b2c2a6")
        self.assertEqual(compress_string("aabbccaaaaaaa"), "a2b2c2a7")
        self.assertEqual(compress_string("aabbccaaaaaaaa"), "a2b2c2a8")
        self.assertEqual(compress_string("aabbccaaaaaaaaa"), "a2b2c2a9")
        self.assertEqual(compress_string("aabbccaaaaaaaaaa"), "a2b2c2a10")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaa"), "a2b2c2a11")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaaa"), "a2b2c2a12")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaaaa"), "a2b2c2a13")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaaaaa"), "a2b2c2a14")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaaaaaa"), "a2b2c2a15")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaaaaaaa"), "a2b2c2a16")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaaaaaaaa"), "a2b2c2a17")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaaaaaaaaa"), "a2b2c2a18")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaaaaaaaaaa"), "a2b2c2a19")
        self.assertEqual(compress_string("aabbccaaaaaaaaaaaaaaaaaaaa"), "a2b2c2a20")

    def test_compress_string_empty(self):
        self.assertEqual(compress_string(""), "")
    
    def test_compress_string_single(self):
        self.assertEqual(compress_string("a"), "a")
        self.assertEqual(compress_string("b"), "b")
        self.assertEqual(compress_string("c"), "c")
        self.assertEqual(compress_string("d"), "d")
        self.assertEqual(compress_string("e"), "e")
    
    def test_compress_string_double(self):
        self.assertEqual(compress_string("aa"), "aa")
        self.assertEqual(compress_string("bb"), "bb")
        self.assertEqual(compress_string("cc"), "cc")
        self.assertEqual(compress_string("dd"), "dd")
        self.assertEqual(compress_string("ee"), "ee")

    def test_compress_string_triple(self):
        self.assertEqual(compress_string("aaa"), "a3")
        self.assertEqual(compress_string("bbb"), "b3")
        self.assertEqual(compress_string("ccc"), "c3")
        self.assertEqual(compress_string("ddd"), "d3")
        self.assertEqual(compress_string("eee"), "e3")
    
    def test_compress_string_quadruple(self):
        self.assertEqual(compress_string("aaaa"), "a4")
        self.assertEqual(compress_string("bbbb"), "b4")
        self.assertEqual(compress_string("cccc"), "c4")
        self.assertEqual(compress_string("dddd"), "d4")
        self.assertEqual(compress_string("eeee"), "e4")

    def test_compress_string_quintuple(self):
        self.assertEqual(compress_string("aaaaa"), "a5")
        self.assertEqual(compress_string("bbbbb"), "b5")
        self.assertEqual(compress_string("ccccc"), "c5")
        self.assertEqual(compress_string("ddddd"), "d5")
        self.assertEqual(compress_string("eeeee"), "e5")

    def test_compress_string_unique(self):
        self.assertEqual(compress_string("abcde"), "abcde")
        self.assertEqual(compress_string("fghij"), "fghij")
        self.assertEqual(compress_string("klmno"), "klmno")
        self.assertEqual(compress_string("pqrst"), "pqrst")
        self.assertEqual(compress_string("uvwxy"), "uvwxy")
        
        
if __name__ == '__main__':
    unittest.main()