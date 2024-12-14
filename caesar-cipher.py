from string import ascii_letters

def caesar_cipher(txt, shift):
    result = []
    
    for item in txt:
        if item in ascii_letters:
            new_index = (ascii_letters.index(item) + shift) % len(ascii_letters)
            result.append(ascii_letters[new_index])
        else:
            result.append(item)
    
    return "".join(result)

txt = input("Enter your String: ")
print(caesar_cipher(txt, 2))
