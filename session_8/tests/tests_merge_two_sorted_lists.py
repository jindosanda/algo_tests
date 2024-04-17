from contextlib import AbstractContextManager
import unittest, sys
from pathlib import Path
current_dir = Path(__file__).parent
parent_dir = current_dir.parent
sys.path.append(str(parent_dir / 'exercises'))
from session8 import merge_two_sorted_lists

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
        
class TestMergeTwoSortedLists(unittest.TestCase):

    def list_to_array(self, head):
        """ Helper function to convert linked list to Python list for easy comparison. """
        result = []
        current = head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def test_equal_length(self):
        # Create the first list: 1 -> 3 -> 5
        l1_node1 = ListNode(1)
        l1_node2 = ListNode(3)
        l1_node3 = ListNode(5)
        l1_node1.next = l1_node2
        l1_node2.next = l1_node3

        # Create the second list: 2 -> 4 -> 6
        l2_node1 = ListNode(2)
        l2_node2 = ListNode(4)
        l2_node3 = ListNode(6)
        l2_node1.next = l2_node2
        l2_node2.next = l2_node3

        # Merge and test
        result = merge_two_sorted_lists(l1_node1, l2_node1)
        self.assertEqual(self.list_to_array(result), [1, 2, 3, 4, 5, 6])

    def test_different_length(self):
        # Create the first list: 1 -> 8
        l1_node1 = ListNode(1)
        l1_node2 = ListNode(8)
        l1_node1.next = l1_node2

        # Create the second list: 2 -> 3 -> 4 -> 7
        l2_node1 = ListNode(2)
        l2_node2 = ListNode(3)
        l2_node3 = ListNode(4)
        l2_node4 = ListNode(7)
        l2_node1.next = l2_node2
        l2_node2.next = l2_node3
        l2_node3.next = l2_node4

        # Merge and test
        result = merge_two_sorted_lists(l1_node1, l2_node1)
        self.assertEqual(self.list_to_array(result), [1, 2, 3, 4, 7, 8])

    def test_one_empty_list(self):
        # Empty List 1 and non-empty List 2: 2 -> 4 -> 6
        l2_node1 = ListNode(2)
        l2_node2 = ListNode(4)
        l2_node3 = ListNode(6)
        l2_node1.next = l2_node2
        l2_node2.next = l2_node3

        # Merge and test
        result = merge_two_sorted_lists(None, l2_node1)
        self.assertEqual(self.list_to_array(result), [2, 4, 6])

    def test_both_empty_lists(self):
        # Merge and test two empty lists
        result = merge_two_sorted_lists(None, None)
        self.assertEqual(self.list_to_array(result), [])

if __name__ == '__main__':
    unittest.main()
        
if __name__ == '__main__':
    unittest.main()
        