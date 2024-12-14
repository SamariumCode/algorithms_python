from string import ascii_letters


def encrypt(txt, shift):
    """
    Encrypts a given string using a Caesar cipher.

    Args:
    txt (str): The string to encrypt.
    shift (int): The number of positions to shift each letter in the string.

    Returns:
    str: The encrypted string.
    """
    result = []

    for item in txt:
        if item in ascii_letters:
            for i, letter in enumerate(ascii_letters):
                if item == letter:
                    new_index = (i + shift) % len(ascii_letters)
                    result.append(ascii_letters[new_index])
                    break
        else:
            result.append(item)

    return "".join(result)


txt = input("Enter your String: ")
shift = int(input("Enter your shift: "))

res_encrypt = encrypt(txt, shift)
print("Encrypted:", res_encrypt)


def decrypt(txt, shift):
    """
    Decrypts a given string using a Caesar cipher.

    This function calls the `encrypt` function with a negative shift to reverse the encryption.

    Args:
    txt (str): The string to decrypt.
    shift (int): The number of positions to shift each letter in the string.

    Returns:
    str: The decrypted string.
    """
    return encrypt(txt, shift)


print("Decrypted with original shift:", decrypt(res_encrypt, shift * -1))


def brute_force(res_encrypt, ascii_letters):
    """
    Attempts to decrypt a string using all possible shift values from 0 to 25.

    Args:
    res_encrypt (str): The encrypted string to attempt brute-force decryption on.
    ascii_letters (str): The string of characters (letters) used in the cipher.

    Returns:
    dict: A dictionary where the keys are shift values (0 to 25) and the values are the decrypted strings.
    """
    shift = 1
    brute_force_data = {}

    for shift_value in range(len(ascii_letters)):
        brute_force_data[shift_value] = decrypt(res_encrypt, shift_value)
    return brute_force_data


print("Brute-force decryption attempts:")
print(brute_force(res_encrypt, ascii_letters))
