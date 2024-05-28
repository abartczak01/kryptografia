# Agata Bartczak 285755
import sys
import math

def ceasar_encrypt(key, input_text):
    result_text = ""
    for char in input_text:
        if char.isalpha():
            if char.islower():
                result_text += chr((ord(char) - 97 + key) % 26 + 97)
            else:
                result_text += chr((ord(char) - 65 + key) % 26 + 65)
        else:
            result_text += char
    return result_text


def ceasar_decrypt(key, input_text):
    return ceasar_encrypt(-key, input_text)


def affine_encrypt(a, b, plaintext):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                ciphertext += chr(((a * (ord(char) - 97)) + b) % 26 + 97)
            else:
                ciphertext += chr(((a * (ord(char) - 65)) + b) % 26 + 65)
        else:
            ciphertext += char
    return ciphertext


def mod_inverse(a):
    a = a % 26
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            return i


def affine_decrypt(a, b, ciphertext):
    plaintext = ""
    a_prim = mod_inverse(a)
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                plaintext += chr(((a_prim * ((ord(char) - 97) - b)) % 26) + 97)
            else:
                plaintext += chr(((a_prim * ((ord(char) - 65) - b)) % 26) + 65)
        else:
            plaintext += char
    return plaintext


def crack_ceaser_with_text(ciphertext):
    with open('extra.txt', 'r+') as f:
        plaintext = f.read().strip()
    for a in range(1, 27):
        if ceasar_encrypt(a, plaintext) == ciphertext[:len(plaintext)]:
            return a
    raise Exception("Key is unable to be found.")


def crack_affine_with_text(ciphertext):
    with open('extra.txt', 'r+') as f:
        plaintext = f.read().strip()
    for a in range(1, 26):
        for b in range(26):
            if affine_encrypt(a, b, plaintext) == ciphertext[:len(plaintext)]:
                return a, b
    raise Exception("Key is unable to be found.")


def crack_ceasar_without_text(ciphertext):
    plaintexts = []
    for key in range(1, 26):
        plaintexts.append(ceasar_decrypt(key, ciphertext))
    return plaintexts


def crack_affine_without_text(ciphertext):
    plaintexts = []
    for b in range(1, 26):
        for a in range(1, 26):
            if math.gcd(a, 26) == 1:
                plaintexts.append(affine_decrypt(a, b, ciphertext))
    return plaintexts

polish_letters = str.maketrans({
    'ą': 'a',
    'ć': 'c',
    'ę': 'e',
    'ł': 'l',
    'ń': 'n',
    'ó': 'o',
    'ś': 's',
    'ź': 'z',
    'ż': 'z',
    'Ą': 'A',
    'Ć': 'C',
    'Ę': 'E',
    'Ł': 'L',
    'Ń': 'N',
    'Ó': 'O',
    'Ś': 'S',
    'Ź': 'Z',
    'Ż': 'Z',
})

if len(sys.argv) != 3:
    raise Exception("Invalid number of arguments.")

if str(sys.argv[1]) not in ['-c', '-a']:
    raise Exception("Invalid first argument. Choose from -c, -a")

if str(sys.argv[2]) not in ['-e', '-d', '-j', '-k']:
    raise Exception("Invalid second argument. Choose from -e, -d, -j, -k")


if sys.argv[1] == '-c':
    if sys.argv[2] == '-e':
        with open('key.txt', 'r') as f:
            keys = f.read().split()
            key = int(keys[0])
            if key > 25 or key < 1:
                raise Exception("Invalid key. Key has to be an integer from range 1-25")
        with open('plain.txt', 'r') as f:
            plain = f.read()
            plain = plain.translate(polish_letters)
        with open('crypto.txt', 'w+') as f:
            f.write(ceasar_encrypt(key, plain))
            
    elif sys.argv[2] == '-d':
        with open('key.txt', 'r') as f:
            keys = f.read().split()
            key = int(keys[0])
            if key > 25 or key < 1:
                raise Exception("Invalid key. Key has to be an integer from range 1-25")
        with open('crypto.txt', 'r') as f:
            crypto = f.read()
            crypto = crypto.translate(polish_letters)
        with open('decrypt.txt', 'w+') as f:
            f.write(ceasar_decrypt(key, crypto))

    elif sys.argv[2] == '-j':
        with open('crypto.txt', 'r') as f:
            crypto = f.read()
            crypto = crypto.translate(polish_letters)
        with open('key-found.txt', 'w+') as f:
            key_found = crack_ceaser_with_text(crypto)
            f.write(str(key_found))
        with open('decrypt.txt', 'w+') as f:
            f.write(ceasar_decrypt(key_found, crypto))

    elif sys.argv[2] == '-k':
        with open('crypto.txt', 'r') as f:
            crypto = f.read()
            crypto = crypto.translate(polish_letters)
        with open('decrypt.txt', 'w+') as f:
            variants = crack_ceasar_without_text(crypto)
            for variant in variants:
                f.write(f"{variant}\n")

elif sys.argv[1] == '-a':
    if sys.argv[2] == '-e':
        with open('key.txt', 'r') as f:
            keys = f.read().split()
            key = int(keys[0])
            affine = int(keys[1])
            if key > 25 or key < 1:
                raise Exception("Invalid key. Key has to be an integer from range 1-25")
            if math.gcd(affine, 26) != 1:
                raise Exception("Invalid key")
        with open('plain.txt', 'r') as f:
            plain = f.read()
            plain = plain.translate(polish_letters)
        with open('crypto.txt', 'w+') as f:
            f.write(affine_encrypt(affine, key, plain))

    elif sys.argv[2] == '-d':
        with open('key.txt', 'r') as f:
            keys = f.read().split()
            key = int(keys[0])
            affine = int(keys[1])
            if key > 25 or key < 1:
                raise Exception("Invalid key. Key has to be an integer from range 1-25")
            if math.gcd(affine, 26) != 1:
                raise Exception("Invalid key.")
        with open('crypto.txt', 'r') as f:
            crypto = f.read()
            crypto = crypto.translate(polish_letters)
        with open('decrypt.txt', 'w+') as f:
            f.write(affine_decrypt(affine, key, crypto))

    elif sys.argv[2] == '-j':
        with open('crypto.txt', 'r') as f:
            crypto = f.read()
            crypto = crypto.translate(polish_letters)
        with open('key-found.txt', 'w+') as f:
            a, b = crack_affine_with_text(crypto)
            f.write(f"{b} {a}")
        with open('decrypt.txt', 'w+') as f:
            f.write(affine_decrypt(a, b, crypto))

    elif sys.argv[2] == '-k':
        with open('crypto.txt', 'r') as f:
            crypto = f.read()
            crypto = crypto.translate(polish_letters)
        with open('decrypt.txt', 'w+') as f:
            variants = crack_affine_without_text(crypto)
            for variant in variants:
                f.write(f"{variant}\n")
