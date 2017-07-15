def bubble_sort(items):
    """
    O(n^2), swap the largest one to the end of list.
    """
    times = 0
    n = len(items)
    for i in range(n):
        for j in range(1, n-i):
            if items[j-1] > items[j]:
                items[j-1], items[j] = items[j], items[j-1]
            times += 1
    return times


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
        items[i], items[min_] = items[min_], items[i]
    return _


def insertion_sort(items):
    """
    O(n^2), insert the smallest item to the start of the line.
    """
    _ = 0
    for i in range(1, len(items)):
        j = i
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
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
    The first O(nlogn)
    """
    if len(items) <= 1:
        return items

    num = int(len(items) / 2)
    left = merge_sort(items[:num])
    right = merge_sort(items[num:])
    return _merge(left, right)


def _merge(left, right):
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
    if left >= right :
        return items

    key = items[left]
    lp = left
    rp = right
    while lp < rp :
        while items[rp] >= key and lp < rp :
            rp -= 1
        while items[lp] <= key and lp < rp :
            lp += 1
        items[lp], items[rp] = items[rp], items[lp]
    items[left], items[lp] = items[lp], items[left]

    _quick_sort(items, left, lp - 1)
    _quick_sort(items, rp + 1, right)
    return items
