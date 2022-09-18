import timeit

def bubble_sort():
    """Sorts lists."""
    list_x = [1, 3, 21, 12, 5, 4, 8, 10, 7, 88, 2, 35, 100, 6, 20, 15, 50, 43, 47, 55, 78, 31, 22, 34, 55, 66, 22, 12, 89, 1000, 1000000, 123498, 230897243098, 8753824, 238478975, 234903284, 2398479, 9895, 324979, 873, 11, 234, 1234]
    swap = False
    while not swap:
        print(f"bubble sort: {list_x}")
        swap = True
        for i in range(1, len(list_x)):
            if list_x[i - 1] > list_x[i]:
                swap = False
                list_x[i - 1], list_x[i] = list_x[i], list_x[i - 1]


print(f"bubble\t\t{timeit.timeit(bubble_sort,  number=1)}")
