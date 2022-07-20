import string

def shift_letter(letter, shift):  
    if letter.isupper():
        letter_index = ord(letter) - ord("A")
        new_index = (letter_index + shift) % 26
        new_unicode = new_index + ord("A")
        return chr(new_unicode)
    else:
        print(' ')
shift_letter('Z', 1)

def caesar_cipher(message, shift):
    encryption = ""
    for letter in message:
        if letter.isupper():
            letter_index = ord(letter) - ord("A")
            new_index = (letter_index + shift) % 26
            new_unicode = new_index + ord("A")
            new_character = chr(new_unicode)
            encryption = encryption + new_character
        else:
            encryption += letter
    return encryption
caesar_cipher('ABCDEFG HIJKLMNOP QRSTUV WXY Z', 1)

def shift_by_letter(letter, letter_shift):  
    if letter.isupper():
        letter_index = ord(letter) - ord("A")
        letter_shift_index = ord(letter_shift) - ord("A")
        new_index = (letter_index + letter_shift_index) % 26
        new_unicode = new_index + ord("A")
        return chr(new_unicode)
    else:
        print(' ')
shift_by_letter('B','K')

def vigenere_cipher(message, key):
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'    
    text = message.upper()
    key = key.upper()
    length_key = len(key) 
    result = ''
    key_int = [abc.find(i) for i in key] 
    text_int = [abc.find(i) for i in text] 
    for i in range(len(text_int)): 
        if text_int[i] == -1:
            result += ' '
        else: 
            character = (text_int[i] + key_int[i % length_key]) % 26
            result += abc[character]
    return result
vigenere_cipher("LONGTEXT", "KEY")

def scytale_cipher(message, shift):
    while len(message) % shift != 0:
            message += '_'
    n = len(message)
    columns = n // shift
    ciphertext = ['_'] * n
    for i in range(n):
        row = i // columns
        col = i % columns
        ciphertext[col * shift + row] = message[i]
    return "".join(ciphertext)
scytale_cipher("INFORMATION_AGE", 4)

def scytale_decipher(message, shift):
    while len(message) % shift != 0:
            message += '_'
    n = len(message)
    rows = len(message) // shift
    columns = n // rows
    ciphertext = ['-'] * n
    for i in range(n):
        row = i // columns
        col = i % columns
        ciphertext[col * rows + row] = message[i]
    return "".join(ciphertext)

    return encrypt(len(ciphertext) // rows, ciphertext)
scytale_decipher('IRIANMOGFANEOT__', 4)