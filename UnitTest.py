import unittest
from Lab7 import Node, sublist, create_linked_list

class TestLinkedListFunctions(unittest.TestCase):
    
    def test_create_linked_list(self):
        # Перевірка, що створення списку працює коректно
        linked_list = create_linked_list()
        self.assertIsNotNone(linked_list)

    def test_sublist(self):
        # Перевірка, що копіювання підсписку працює коректно
        linked_list = Node(1)
        linked_list.next = Node(2)
        linked_list.next.next = Node(3)
        linked_list.next.next.next = Node(4)

        sub_list = sublist(linked_list, 2, 2)
        self.assertEqual(sub_list.data, 2)
        self.assertEqual(sub_list.next.data, 3)
        self.assertIsNone(sub_list.next.next)

if __name__ == '__main__':
    unittest.main()
