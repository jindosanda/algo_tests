from contextlib import AbstractContextManager
import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from session4 import better_algo_x
import timeit

def algo_x(n):
    assert n >= 0
    m = 0
    while m*m <= n:
        m = m + 1
    return m - 1

class TestExercises(unittest.TestCase):
    def test_better_algo_x(self):
        ns = [n for n in range(1000)]
        for n in ns:
            self.assertEqual(better_algo_x(n),algo_x(n))
    
    def test_better_algo_x_0(self):
        self.assertEqual(better_algo_x(0),algo_x(0))

    def test_performance(self):
        test_values = [10000, 100000, 1000000, 10000000, 100000000]

        for n in test_values:
            time_algo_x = timeit.timeit(lambda: algo_x(n), number=100)
            time_better_algo_x = timeit.timeit(lambda: better_algo_x(n), number=100)
            self.assertTrue(time_better_algo_x <= time_algo_x, f"better_algo_x is not faster than algo_x for n={n}")


        
        
if __name__ == '__main__':
    unittest.main()
        