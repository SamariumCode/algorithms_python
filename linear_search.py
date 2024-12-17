def linear_search(array, element):
    """
    Perform a linear search on a list to find the position of a given element.

    Args:
        array (list): The list of elements to search in.
        element (any): The element to search for in the list.

    Returns:
        int: The 1-based index of the element if found; otherwise, -1.

    Example:
        >>> linear_search([1, 25, 8, 11, 14, 18, 23, 32, 48], 23)
        7
        >>> linear_search([1, 2, 3, 4], 5)
        -1
    """
    for i in range(len(array)):
        if array[i] == element:
            return i + 1

    return -1


print(linear_search([1, 25, 8, 11, 14, 18, 23, 32, 48], 23))
