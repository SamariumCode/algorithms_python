

def search_range(sequence, num_search):
    sequence = sorted(sequence)
    first_index = -1
    last_index = -1

    for i in range(len(sequence)):
        if sequence[i] == num_search:
            if first_index == -1:
                first_index = i
            last_index = i

    return [first_index, last_index] if first_index != -1 else [-1, -1]

print(search_range((7, 8, 5, 7, 10, 8, 8), 8))
