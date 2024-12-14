def search_insert(arr, num):
    """
    Determines the index of `num` in the array `arr` if it exists.
    Otherwise, returns -1.

    Args:
        arr (list): A list of integers, assumed to be sorted.
        num (int): The number to search for in the list.

    Returns:
        int: The index of `num` if it exists in `arr`, otherwise -1.

    Examples:
        >>> search_insert([1, 3, 5, 6], 5)
        2
        >>> search_insert([1, 3, 5, 6], 2)
        -1
    """
    arr_inserts = {item: index for index, item in enumerate(arr)}
    return arr_inserts[num] if num in arr_inserts else -1


print(search_insert([1, 3, 5, 6], 55))