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
