def zig_zag_iterator(nums1, nums2):
    """
    Alternates between elements of two lists (nums1 and nums2) and 
    returns a new list where elements are taken from both lists in a zigzag pattern.

    The function first adds elements from both lists alternately (first from 
    nums1, then from nums2) until one list is exhausted. Then, it appends 
    the remaining elements from the longer list to the result.

    Parameters:
    nums1 (list): A list of integers.
    nums2 (list): A list of integers.

    Returns:
    list: A list containing the elements from both input lists in a zigzag order, 
          starting with an element from nums1, followed by an element from nums2.

    Example:
    >>> zig_zag_iterator([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    Note:
    The function handles cases where the input lists have different lengths. 
    The remaining elements from the longer list are appended after alternating 
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
