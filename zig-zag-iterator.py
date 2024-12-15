def zig_zag_iterator(nums1, nums2):
    """
    Alternates between elements of two lists (odd_nums and even_nums) and 
    returns a new list where elements are taken from both lists in a zigzag pattern.

    The function first adds elements from both lists alternately (first from 
    odd_nums, then from even_nums) until one list is exhausted. Then, it adds 
    the remaining elements of the longer list to the result.

    Parameters:
    odd_nums (list): A list of integers representing odd numbers.
    even_nums (list): A list of integers representing even numbers.

    Returns:
    list: A list containing the elements from both input lists in a zigzag order, 
          starting with an element from odd_nums, followed by an element from even_nums.

    Example:
    >>> zig_zag_iterator([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Note:
    The function handles cases where the input lists have different lengths. 
    Remaining elements from the longer list are appended after alternating 
    between the two lists.
    """
    result = []
    min_len = min(len(nums1), len(nums2))

    for i in range(min_len):
        result.append(nums1[i])
        result.append(nums2[i])

    for i in range(min_len, len(nums1)):
        result.append(nums1[i])

    for i in range(min_len, len(nums2)):
        result.append(nums2[i])

    return result


print(zig_zag_iterator([1, 3, 5, 7, 9, 11, 13], [2, 4, 6, 8, 10, 12]))
