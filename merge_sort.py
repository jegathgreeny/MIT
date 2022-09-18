import timeit

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    while (i < len(left)):
        result.append(left[i])
        i += 1
    while (j < len(right)):
        result.append(right[j])
        j += 1
    print(f"merge: {str(left)} & str{(right)}")
    return result



def merge_sort(L=[1, 3, 21, 12, 5, 4, 8, 10, 7, 88, 2, 35, 100, 6, 20, 15, 50, 43, 47, 55, 78, 31, 22, 34, 55, 66, 22, 12, 89, 1000, 1000000, 123498, 230897243098, 8753824, 238478975, 234903284, 2398479, 9895, 324979, 873, 11, 234, 1234]):
    print(f'merge sort: {str(L)}')
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

print(f"merge\t\t{timeit.timeit(merge_sort, number=1)}")
