import random


class OneTime:
    """
    A class to implement a custom encryption and decryption algorithm using a one-time random key.

    Methods:
        encrypt(text: str) -> tuple[list[int], list[int]]:
            Encrypts a given plaintext string into a list of cipher values using randomly generated keys.
        
        decrypt(cipher: list[int], key: list[int]) -> str:
            Decrypts a list of cipher values back into the original plaintext string using the provided keys.
    """

    def encrypt(self, text):
        """
        Encrypts a plaintext string using randomly generated keys.

        Args:
            text (str): The plaintext string to be encrypted.

        Returns:
            tuple[list[int], list[int]]:
                - cipher (list[int]): A list of encrypted numeric values.
                - key (list[int]): A list of randomly generated keys used for encryption.

        Encryption process:
            1. Each character in the plaintext is converted to its ASCII value.
            2. A random key is generated for each character.
            3. The cipher value for each character is calculated using the formula:
               c = (i + k) * k
               where:
                   c = cipher value,
                   i = ASCII value of the character,
                   k = random key.
        """
        plain = [ord(i) for i in text]
        key = []
        cipher = []
        for i in plain:
            k = random.randint(1, 300)
            c = (i + k) * k
            cipher.append(c)
            key.append(k)

        return cipher, key

    def decrypt(self, cipher, key):
        """
        Decrypts a list of cipher values back into the original plaintext string.

        Args:
            cipher (list[int]): A list of encrypted numeric values.
            key (list[int]): A list of keys used for encryption.

        Returns:
            str: The decrypted plaintext string.

        Decryption process:
            1. For each cipher value and its corresponding key, the original ASCII value
               is calculated using the formula:
               p = (c - k^2) / k
               where:
                   p = ASCII value of the original character,
                   c = cipher value,
                   k = key.
            2. The ASCII values are converted back to characters to reconstruct the plaintext string.
        """
        plain = []
        for i in range(len(key)):
            p = int((cipher[i] - key[i] ** 2) / key[i])
            plain.append(chr(p))
        result = ''.join([i for i in plain])
        
        return result


# Example usage
# Create an instance of the OneTime class
otp = OneTime()

# Input text to be encrypted
text = "amir"

# Encrypt the text
cipher, key = otp.encrypt(text)
print("Original Text:", text)
print("Cipher Values:", cipher)
print("Keys:", key)

# Decrypt the cipher text
decrypted_text = otp.decrypt(cipher, key)
print("Decrypted Text:", decrypted_text)
