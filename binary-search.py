def binary_search(array, element):
    """
    Perform a binary search on a sorted list to find the position of a given element.

    Args:
        array (list): A sorted list of elements to search in.
        element (any): The element to search for in the list.

    Returns:
        int: The 0-based index of the element if found; otherwise, -1.

    Example:
        >>> binary_search([2, 3, 4, 6, 12, 19, 20, 21], 19)
        5
        >>> binary_search([1, 3, 5, 7], 6)
        -1

    Note:
        The input array must be sorted in ascending order for the binary search to work correctly.
    """
    low, high = 0, len(array) - 1

    while low <= high:
        mid = (high + low) // 2
        val = array[mid]
        if val == element:
            return mid
        elif val < element:
            low = mid + 1
        else:
            high = mid - 1
    return -1


print(binary_search([2, 3, 4, 6, 12, 19, 20, 21], 19))
