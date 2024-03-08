import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from ex289 import MinHeapAdd

def is_min_heap(H):
    n = len(H)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and H[i] > H[left]:
            return False
        if right < n and H[i] > H[right]:
            return False
    return True


class TestExercises(unittest.TestCase):
    def test_add(self):
        H = [10, 20, 15, 30, 40]
        MinHeapAdd(H, 5)
        self.assertTrue(is_min_heap(H))
        self.assertEqual(len(H), 6)
    
    def test_add_larger(self):
        H = [10, 20, 15, 30, 40]
        MinHeapAdd(H, 50)
        self.assertTrue(is_min_heap(H))
        self.assertEqual(len(H), 6)

    def test_add_middle_value(self):
        H = [10, 20, 15, 30, 40]
        MinHeapAdd(H, 25)
        self.assertTrue(is_min_heap(H))
        self.assertEqual(len(H), 6)
        
if __name__ == "__main__":
    unittest.main()