from string import ascii_letters

def caesar_cipher(txt, shift):
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
print(caesar_cipher(txt, 2))
