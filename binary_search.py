def binary_search(list_1, num, low, high):

    # split the list from the middle
    mid = (high + low) // 2

    # the chosen middle number is the correct number
    if list_1[mid] == num:
        print(f'The number is at index: {mid}')
        return True 

    # the number doesn't exist in the list   
    if low == high:
        print(f'The number is not in the list')
        return False

    # check
    # the middle position is greater than the number
    if list_1[mid] > num:
        # set the highest position as the mid position, because the correct number is greater than the value at mid position
        high = mid - 1
        # run with the updated positions
        binary_search(list_1, num, low, high)
    # the middle position is less than the number
    elif list_1[mid] < num:
        # set the low position as the mid position, because the correct number is less than the value at mid position
        low = mid + 1
        binary_search(list_1, num, low, high)


integers = [1, 2, 3, 4, 5, 10, 20, 40, 44, 55, 60, 70, 80, 90, 110, 220, 333, 1111]
binary_search(integers, 4, 0, len(integers) - 1)
