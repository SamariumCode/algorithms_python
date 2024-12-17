def last_occurrence(array, element):
    """
    Finds the last occurrence of the given element in a sorted array using binary search.

    Parameters:
        array (list): A sorted list of elements.
        element (int): The element to find the last occurrence of.

    Returns:
        int: The index of the last occurrence of the element in the array.
             Returns None if the element is not found.
    
    Example:
        >>> last_occurrence([2, 2, 2, 3, 3, 4, 4, 5, 5, 5], 4)
        6
    """
    low, high = 0, len(array) - 1
    while low <= high:
        mid = (high + low) // 2
        if (array[mid] == element and mid == len(array)-1) or \
                (array[mid] == element and array[mid + 1] > element):
            return mid
        elif (array[mid] <= element):
            low = mid + 1
        else:
            high = mid - 1
