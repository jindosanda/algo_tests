from contextlib import AbstractContextManager
import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from session5 import two_sum

# O(n^2) for test comparison
def two_sum_n2(A, t):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] + A[j] == t:
                return True
    return False

class LargestSubarraySum(unittest.TestCase):
    def tests_two_sum(self):
        A = [-3, 1]
        t = -2
        self.assertEqual(two_sum(A, t), True)

    def tests_two_sum_2(self):
        A = [-5, -4, -4, -3, -1, 2, 2, 3, 4, 6, 8]
        t = 12
        self.assertEqual(two_sum(A, t), True)

    def tests_two_sum_3(self):
        A = [-3, -1, 4, 9, 10]
        t = 1
        self.assertEqual(two_sum(A, t), True)

    def tests_two_sum_4(self):
        A = [-5, -5, -4, -1, 6, 7, 8]
        t = 12
        self.assertEqual(two_sum(A, t), False)

    def tests_two_sum_5(self):
        A = []
        t = 20
        self.assertEqual(two_sum(A, t), False)

    def tests_two_sum_6(self):
        A = [-4, -2, -2, 2, 8, 8]
        t = 15
        self.assertEqual(two_sum(A, t), False)

    def tests_two_sum_7(self):
        A = [-4, -3, -3, -1, 0, 0, 0, 4, 6, 6, 8, 9]
        t = 4
        self.assertEqual(two_sum(A, t), True)

    def test_comparison_on_on2(self):
        import random
        n = 200
        for _ in range(n):
            l = random.randint(0, 15)
            A = [random.randint(-5, 10) for _ in range(l)]
            A.sort()
            t = random.randint(-10, 25)
            assert two_sum(A, t) == two_sum_n2(A, t)
        
if __name__ == '__main__':
    unittest.main()
        