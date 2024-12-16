def two_sum_using_dict(sequence, target):
    """
    Finds all pairs of indices in the sequence where the sum of the elements equals the target
    using a dictionary to store seen values and their indices.

    Args:
        sequence (list[int]): A list of integers.
        target (int): The target sum.

    Returns:
        list[list[int]]: A list of pairs of indices whose elements sum to the target.
    """
    seen = {}
    result = []

    for index, value in enumerate(sequence):
        complement = target - value
        if complement in seen:
            result.append([seen[complement], index])
        seen[value] = index

    return result


def two_sum_using_nested_loops(sequence, target):
    """
    Finds all pairs of indices in the sequence where the sum of the elements equals the target
    using nested loops and sorting the sequence.

    Args:
        sequence (list[int]): A list of integers.
        target (int): The target sum.

    Returns:
        list[list[int]]: A list of pairs of indices whose elements sum to the target.
    """
    result = []
    sequence_sorted = sorted(sequence)

    for i in range(len(sequence_sorted)):
        for j in range(i + 1, len(sequence_sorted)):
            if sequence_sorted[i] + sequence_sorted[j] == target:
                result.append([sequence.index(sequence_sorted[i]),
                              sequence.index(sequence_sorted[j])])

    return result


# Test code with similar inputs
print(two_sum_using_dict([11, 15, 7, 2, 3], 18))  # Output of method 1
print(two_sum_using_nested_loops([11, 15, 7, 2, 3], 18))  # Output of method 2
