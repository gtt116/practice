import unittest
import data
import sort


class BasicTests(unittest.TestCase):

    def _test_sort(self, sort_method, side_effect=True):
        """
        If side_effect is False means the sort method will return a new list.
        """
        items = data.random_all(100)
        expected = sorted(items)
        if side_effect:
            sort_method(items)
        else:
            items = sort_method(items)
        self.assertEqual(expected, items)

    def test_bubble(self):
        self._test_sort(sort.bubble_sort)

    def test_insertion(self):
        self._test_sort(sort.insertion_sort)

    def test_selection(self):
        self._test_sort(sort.selection_sort)

    def test_shell(self):
        self._test_sort(sort.shell_sort)

    def test_merge(self):
        self._test_sort(sort.merge_sort, False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
