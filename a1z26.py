def encode(arr):
    """
    Encodes a string by converting each character to a number based on its 
    ASCII value, offset by 92.

    Parameters:
        arr (str): The string to encode.

    Returns:
        list[int]: A list of integers representing the encoded characters.

    Examples:
        >>> encode("amir")
        [97, 109, 105, 114]
    """
    return [ord(item) - 92 for item in arr]


def decode(encode):
    """
    Decodes a list of integers into a string by converting each number back 
    to its corresponding character using an offset of 92.

    Parameters:
        encode (list[int]): A list of integers to decode.

    Returns:
        str: The decoded string.

    Examples:
        >>> decode([97, 109, 105, 114])
        'amir'
    """
    return ''.join([chr(item + 92) for item in encode])

