import data
import basic


def main():
    MAX = 10
    a = data.random_all(MAX)
    print basic.bubble_sort(a[:])
    print basic.insertion_sort(a[:])
    print basic.selection_sort(a[:])


if __name__ == '__main__':
    main()
