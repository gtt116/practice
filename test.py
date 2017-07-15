import unittest
import data
import sort


class BasicTests(unittest.TestCase):

    def _test_sort(self, sort_function):
        items = data.random_all(100)
        expected = sorted(items)
        sort_function(items)
        self.assertEqual(expected, items)

    def test_bubble(self):
        self._test_sort(sort.bubble_sort)

    def test_insertion(self):
        self._test_sort(sort.insertion_sort)

    def test_selection(self):
        self._test_sort(sort.selection_sort)


if __name__ == '__main__':
    unittest.main()
