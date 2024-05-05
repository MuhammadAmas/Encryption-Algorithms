from Crypto.Cipher import AES
import os


def pad_message(message):
    pad_length = AES.block_size - len(message) % AES.block_size
    padding = bytes([pad_length]) * pad_length
    return message + padding


def unpad_message(padded_message):
    pad_length = padded_message[-1]
    return padded_message[:-pad_length]


def encrypt_message(message, key):
    # Generate a random IV of the correct length
    iv = os.urandom(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_message = pad_message(message.encode())
    ciphertext = cipher.encrypt(padded_message)
    return iv + ciphertext


def decrypt_message(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = cipher.decrypt(ciphertext[AES.block_size:])
    unpadded_message = unpad_message(decrypted_message)
    return unpadded_message.decode()


message = "This is a secret message"
key = os.urandom(16)  # AES-128 key size
encrypted = encrypt_message(message, key)
print("Encrypted:", encrypted)
decrypted = decrypt_message(encrypted, key)
print("Decrypted:", decrypted)
