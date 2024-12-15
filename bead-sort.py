def bead_sort(sequence):
    """
    Sorts a list of non-negative integers using the bead sort algorithm.

    Bead sort simulates the behavior of beads falling under gravity. Larger numbers
    "pull" the beads downward, resulting in a sorted sequence.

    Parameters:
        sequence (list[int]): A list of non-negative integers to sort.

    Returns:
        list[int]: The sorted list in ascending order.

    Raises:
        TypeError: If any element in the sequence is not a non-negative integer.

    Examples:
        >>> bead_sort([4, 7, 9, 2, 3, 6, 7])
        [2, 3, 4, 6, 7, 7, 9]
    """
    if any(not isinstance(x, int) or x < 0 for x in sequence):
        raise TypeError("sequence must be list of non-negative integers")

    for _ in range(len(sequence)):
        for i, (rod_upper, rod_lower) in enumerate(zip(sequence, sequence[1:])):
            if rod_upper > rod_lower:
                sequence[i] -= rod_upper - rod_lower
                sequence[i + 1] += rod_upper - rod_lower
    return sequence


print(bead_sort([4, 7, 9, 2, 3, 6, 7]))


def bubble_sort(sequence):
    """
    Sorts a list of non-negative integers using the bubble sort algorithm.

    Bubble sort repeatedly compares adjacent elements in the list and swaps them
    if they are in the wrong order. This process is repeated until the list is sorted.

    Parameters:
        sequence (list[int]): A list of non-negative integers to sort.

    Returns:
        list[int]: The sorted list in ascending order.

    Raises:
        TypeError: If any element in the sequence is not a non-negative integer.

    Examples:
        >>> bubble_sort([4, 7, 9, 2, 3, 6, 7])
        [2, 3, 4, 6, 7, 7, 9]
    """
    if any(not isinstance(x, int) or x < 0 for x in sequence):
        raise TypeError("sequence must be list of non-negative integers")

    for i in range(len(sequence) - 1):
        for j in range(len(sequence) - i - 1):
            if sequence[j] > sequence[j + 1]:
                sequence[j], sequence[j + 1] = sequence[j + 1], sequence[j]
    return sequence


print(bubble_sort([4, 7, 9, 2, 3, 6, 7]))
