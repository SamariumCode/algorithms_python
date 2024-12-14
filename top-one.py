def top_one(arr):
    """
    This function takes a list of integers and returns a list of elements that appear most frequently in the list.
    
    Parameters:
        arr (list): A list of integers. The function will count the frequency of each element in the list.
    
    Returns:
        list: A list containing the elements that have the highest frequency in the input list. 
              If multiple elements have the same frequency, all of them will be returned.
    
    Example:
        >>> top_one([1, 1, 2, 3, 3, 3, 4])
        [3]
        
        >>> top_one([1, 1, 2, 3, 3, 4, 4])
        [1, 3, 4]
        
    Notes:
        - If the input list is empty, the function will return an empty list.
        - The function iterates through the list twice: first to count the occurrences and second to find the elements with the highest frequency.
    """
    values = {}
    result = []
    f_val = 0
    
    for i in arr:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1
            
    f_val = max(values.values())
    
    for i in values.keys():
        if values[i] == f_val:
            result.append(i)
        else:
            continue
    
    return result
    
    
print(top_one([1, 1, 2, 3, 3, 3, 4]))