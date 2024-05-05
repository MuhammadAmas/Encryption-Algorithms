import base64
from Crypto.Random import get_random_bytes
from Crypto.Cipher import DES


def pad_message(message):
    padding_length = 8 - (len(message) % 8)
    padded_message = message + bytes([padding_length]) * padding_length
    return padded_message


def unpad_message(padded_message):
    padding_length = padded_message[-1]
    return padded_message[:-padding_length]


def encrypt_message(message, key):
    des_cipher = DES.new(key, DES.MODE_ECB)
    padded_message = pad_message(message.encode())
    encrypted_message = des_cipher.encrypt(padded_message)
    return base64.b64encode(encrypted_message).decode()


def decrypt_message(encrypted_message, key):
    des_cipher = DES.new(key, DES.MODE_ECB)
    decoded_message = base64.b64decode(encrypted_message)
    decrypted_message = des_cipher.decrypt(decoded_message)
    return unpad_message(decrypted_message).decode()


message = "Karachi"
print("Text: ", message)
key = get_random_bytes(8)
# DES key size is 8 bytes
encrypted = encrypt_message(message, key)
print("Encrypted:", encrypted)
decrypted = decrypt_message(encrypted, key)
print("Decrypted:", decrypted)
