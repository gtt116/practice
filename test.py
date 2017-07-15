import unittest
import time
import data
import sort


class SorterTests(unittest.TestCase):

    def _test_sort(self, sort_method, side_effect=True):
        """
        If side_effect is False means the sort method will return a new list.
        """
        items = data.random_all(3000)
        expected = sorted(items)
        start = time.time()
        if side_effect:
            sort_method(items)
        else:
            items = sort_method(items)
        end = time.time()
        print '%s using %.4fs' % (sort_method.__name__, end - start)
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

    def test_quick(self):
        self._test_sort(sort.quick_sort, False)


if __name__ == '__main__':
    unittest.main(verbosity=2)
