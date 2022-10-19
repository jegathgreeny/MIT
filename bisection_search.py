def search(list_1, num):
    """Runs the main loop."""

    def bisect_search(list_1, num, low, high):
        """Does the bisection search."""
        if high == low:
            # return list_1[low] == num
            return low
        # find the middle position, // preforms integer division, so only the integer part is returned while dividing
        mid = (low + high) // 2
        # 
        if list_1[mid] == num:
            return True
        elif list_1[mid] > num:
            if low == mid:
                # executes if the number doesn't exist in the list
                return False
            else:
                return bisect_search(list_1, num, low, mid - 1)
        else:
            return bisect_search(list_1, num, mid + 1, high)

    if len(list_1) == 0:
        return False
    else:
        test_1 = bisect_search(list_1, num, 0, len(list_1) - 1)
        print(test_1)


list_1 = [1, 2, 4, 55, 66, 78, 91, 120, 151, 152, 166]
search(list_1, 120)
