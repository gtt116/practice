import data
import sort


def main():
    MAX = 10
    a = data.random_all(MAX)
    print sort.bubble_sort(a[:])
    print sort.insertion_sort(a[:])
    print sort.selection_sort(a[:])


if __name__ == '__main__':
    main()
