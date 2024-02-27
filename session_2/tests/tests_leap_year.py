import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from leap_year import leap_year

class TestExercises(unittest.TestCase):
    def test_leap_year(self):
        self.assertEqual(leap_year(2000), True)
        self.assertEqual(leap_year(1969), False)
        self.assertEqual(leap_year(2023), False)
        self.assertEqual(leap_year(1984), True)
        self.assertEqual(leap_year(2022), False)
        self.assertEqual(leap_year(2200), False)
        self.assertEqual(leap_year(2400), True)
        self.assertEqual(leap_year(1900), False)
        self.assertEqual(leap_year(1600), True)
        self.assertEqual(leap_year(2004), True)
        self.assertEqual(leap_year(2008), True)
    
    def test_leap_year_negative(self):
        self.assertEqual(leap_year(-2000), True)
        self.assertEqual(leap_year(-1969), False)
        self.assertEqual(leap_year(-2023), False)
        self.assertEqual(leap_year(-1984), True)
        self.assertEqual(leap_year(-2022), False)
        self.assertEqual(leap_year(-2200), False)
        self.assertEqual(leap_year(-2400), True)
        self.assertEqual(leap_year(-1900), False)
        self.assertEqual(leap_year(-1600), True)
        self.assertEqual(leap_year(-2004), True)
        self.assertEqual(leap_year(-2008), True)

    def test_leap_year_float(self):
        self.assertEqual(leap_year(2000.0), True)
        self.assertEqual(leap_year(1969.0), False)
        self.assertEqual(leap_year(2023.0), False)
        self.assertEqual(leap_year(1984.0), True)
        self.assertEqual(leap_year(2022.0), False)
        self.assertEqual(leap_year(2200.0), False)
        self.assertEqual(leap_year(2400.0), True)
        self.assertEqual(leap_year(1900.0), False)
        self.assertEqual(leap_year(1600.0), True)
        self.assertEqual(leap_year(2004.0), True)
        self.assertEqual(leap_year(2008.0), True)

    
        
if __name__ == '__main__':
    unittest.main()