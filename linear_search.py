def search(list_1, num):
    """Searches for a item linearly."""
    for i in range(len(list_1)):
        if list_1[i] == num:
            return True
    return False


lis = [1, 2, 3, 4, 5, 7, 8, 10, 22, 25, 31]
test = search(lis, 4)
print(test)
