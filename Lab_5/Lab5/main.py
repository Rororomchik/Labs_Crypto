import os

def print_file_contents(filename):
    with open(filename, 'r') as file:
        print(file.read())

def one_time_pad_encrypt(plain_text):
    key = os.urandom(len(plain_text))
    encrypted_text = ""
    for i in range(len(plain_text)):
        encrypted_text += chr(ord(plain_text[i]) ^ key[i])
    return encrypted_text, key

def one_time_pad_decrypt(encrypted_text, key):
    decrypted_text = ""
    for i in range(len(encrypted_text)):
        decrypted_text += chr(ord(encrypted_text[i]) ^ key[i])
    return decrypted_text

def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

plain_text = read_file('input_text.txt')
encrypted_text, key = one_time_pad_encrypt(plain_text)
print("\nEncrypted Text:")
print(encrypted_text)

decrypted_text = one_time_pad_decrypt(encrypted_text, key)
print("\nDecrypted Text:")
print(decrypted_text)