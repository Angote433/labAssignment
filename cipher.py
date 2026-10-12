# Assignment 2 - Shift (Caesar) cipher
# Handles alphabetic characters and white spaces only.
 
def encrypt(plain_text, key):
    cipher_text = ""
    for ch in plain_text:
        if ch == " ":
            cipher_text += " "
        else:
            position = ord(ch.upper()) - ord("A")      # A=0, B=1, ... Z=25
            shifted = (position + key) % 26
            cipher_text += chr(shifted + ord("A"))
    return cipher_text
 
 
def decrypt(cipher_text, key):
    plain_text = ""
    for ch in cipher_text:
        if ch == " ":
            plain_text += " "
        else:
            position = ord(ch.upper()) - ord("A")
            shifted = (position - key) % 26
            plain_text += chr(shifted + ord("A"))
    return plain_text.lower()
 
 
message = "cookie"
key = 4
 
encrypted = encrypt(message, key)
decrypted = decrypt(encrypted, key)
 
print("Original message :", message)
print("Encryption key   :", key)
print("Encrypted message:", encrypted)
print("Decrypted message:", decrypted)