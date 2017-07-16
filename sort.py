def _swap(l, a, b):
    l[a], l[b] = l[b], l[a]


def bubble_sort(items):
    """
    O(n^2), swap the largest one to the end of list.
    """
    _ = 0
    n = len(items)
    for i in range(n):
        for j in range(1, n-i):
            if items[j-1] > items[j]:
                _swap(items, j-1, j)
            _ += 1
    return _


def selection_sort(items):
    """
    O(n^2), select the smallest item insert to the start of the list.
        the less data movement algorithm.
    """
    _ = 0
    n = len(items)
    for i in range(n):
        min_ = i
        for j in range(i+1, n):
            if items[j] < items[min_]:
                min_ = j
            _ += 1
        _swap(items, i, min_)
    return _


def insertion_sort(items):
    """
    O(n^2), insert the smallest item to the start of the line.
    """
    _ = 0
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            _swap(items, j, j-1)
            j -= 1
            _ += 1
    return _


def shell_sort(items):
    """
    A better insertion sort algorithm.
    """
    n = len(items)
    step = int(round(n/2))
    _ = 0
    while step > 0:
        for i in range(step, n):
            tmp = items[i]
            j = i
            while (j >= step and items[j-step] > tmp):
                items[j] = items[j-step]
                j = j - step
                _ += 1
            items[j] = tmp
        step = int(round(step / 2))
    return _


def merge_sort(items):
    """
    The first O(nlogn) sort algorithm.
    """
    if len(items) <= 1:
        return items

    num = int(len(items) / 2)
    left = merge_sort(items[:num])
    right = merge_sort(items[num:])
    return _merge(left, right)


def _merge(left, right):
    """
    Merge two list to one.

    :param left: list
    :param right: list
    :returns: the merged list.
    """
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]
    result += right[r:]
    return result


def quick_sort(items):
    """
    Another O(nlogn) algorithm
    """
    return _quick_sort(items, 0, len(items) - 1)


def _quick_sort(items, left, right):
    if left >= right:
        return items

    low = left
    high = right

    while low < high:
        while items[high] >= items[left] and low < high:
            high -= 1
        while items[low] <= items[left] and low < high:
            low += 1
        _swap(items, low, high)

    # here low == high, so swap left with low with the same result
    _swap(items, left, low)

    _quick_sort(items, left, low - 1)
    _quick_sort(items, high + 1, right)
    return items
