def limit(arr, min=None, max=None):
    """
    Filters a list based on optional minimum and maximum limits.

    Parameters:
        arr (list): The input list of numbers to filter.
        min (int, optional): The upper limit for values to include. 
                             If provided, only values less than or equal to `min` are included.
        max (int, optional): The lower limit for values to include. 
                             If provided, only values greater than or equal to `max` are included.

    Returns:
        list: A filtered list containing elements that satisfy both the `min` and `max` conditions.
              If neither `min` nor `max` are provided, the original list is returned.

    Example:
        >>> limit([1, 2, 3, 4, 5, 6, 7, 8, 9], max=2)
        [3, 4, 5, 6, 7, 8, 9]
    """
    def min_check(val): return True if min is None else (val <= min)
    def max_check(val): return True if max is None else (val >= max)

    return [val for val in arr if min_check(val) and max_check(val)]


print(limit([1, 2, 3, 4, 5, 6, 7, 8, 9], max=2))


def limit2(arr, min=None, max=None):
    """
    Splits a list into two subsets based on optional minimum and maximum limits.

    Parameters:
        arr (list): The input list of numbers to split.
        min (int, optional): The upper limit for the first subset. 
                             If provided, the first subset will contain all values less than or equal to `min`.
        max (int, optional): The lower limit for the second subset. 
                             If provided, the second subset will contain all values greater than or equal to `max`.

    Returns:
        tuple:
            - A list of elements less than or equal to `min` (or all elements if `min` is not provided).
            - A list of elements greater than or equal to `max` (or all elements if `max` is not provided).

    Example:
        >>> limit2([1, 2, 3, 4, 5], min=2)
        ([1, 2], [3, 4, 5])

        >>> limit2([1, 2, 3, 4, 5], min=2, max=4)
        ([1, 2], [4, 5])
    """
    min_nums = [item for item in arr if (
        item <= min if min is not None else True)]
    max_nums = [item for item in arr if (
        item >= max if max is not None else True)]

    return min_nums, max_nums


print(limit2([1, 2, 3, 4, 5], min=2))
