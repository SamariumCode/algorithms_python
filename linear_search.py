

def linear_search(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i + 1

    return -1


print(linear_search([1, 25, 8, 11, 14, 18, 23, 32, 48], 23))
