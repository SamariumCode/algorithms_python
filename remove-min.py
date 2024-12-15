def remove_min(sequence):
    """
    Removes all occurrences of the minimum value from the given sequence.

    The function first checks if the sequence is empty and raises an exception if it is. 
    Then, it finds the minimum value in the sequence and returns a new list with 
    all occurrences of that minimum value removed.

    Parameters:
    sequence (list): A list of numerical elements (integers or floats).

    Returns:
    list: A new list with all occurrences of the minimum value removed from the original sequence.

    Raises:
    Exception: If the input sequence is empty.

    Example:
    >>> remove_min([4, 7, 9, 2, 3, -6, 7])
    [4, 7, 9, 2, 3, 7]

    Note:
    - If there are multiple occurrences of the minimum value, all will be removed.
    - The original sequence is not modified; a new list is returned.
    """
    
    if len(sequence) == 0:
        raise Exception("Sequence must have at least one element")
    
    min_num = sequence[0]
    
    for i in sequence:
        if i < min_num:
            min_num = i
    
    return [x for x in sequence if x != min_num]


print(remove_min([4, 7, 9, 2, 3, -6, 7]))
