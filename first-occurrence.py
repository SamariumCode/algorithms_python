def first_occurrence_linear_search(array, element):
    """
    Perform a linear search to find the index of the first occurrence of an element in a list.

    Args:
        array (list): The list of elements to search in.
        element (any): The element to search for in the list.

    Returns:
        int: The 0-based index of the first occurrence of the element if found; otherwise, None.

    Example:
        >>> first_occurrence_linear_search([2, 2, 2, 3, 3, 4, 4, 5, 5, 5], 4)
        5
        >>> first_occurrence_linear_search([1, 3, 5, 7], 2)
        None
    """
    for index, item in enumerate(array):
        if item == element:
            return index


def first_occurrence_binary_search(array, element):
    """
    Perform a binary search to find the index of the first occurrence of an element in a sorted list.

    Args:
        array (list): A sorted list of elements to search in.
        element (any): The element to search for in the list.

    Returns:
        int: The 0-based index of the first occurrence of the element if found; otherwise, None.

    Example:
        >>> first_occurrence_binary_search([2, 2, 2, 3, 3, 4, 4, 5, 5, 5], 4)
        5
        >>> first_occurrence_binary_search([1, 3, 5, 7], 2)
        None

    Note:
        - The input list must be sorted in ascending order for this function to work correctly.
        - If the list is not sorted, the output will be incorrect or undefined.
    """
    low, high = 0, len(array) - 1
    
    while low < high:
        mid = (low + high) // 2
        if low == high:
            break
        if array[mid] < element:
            low = mid + 1
        else:
            high = mid
    if array[low] == element:
        return low
