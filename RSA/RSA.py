from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding


def generate_rsa_keypair():
    # Generate an RSA key pair with a key size of 2048 bits
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key


def encrypt_message(message, public_key):
    # Convert the message to bytes
    message_bytes = message.encode()
    # Use RSA-OAEP encryption scheme for secure padding
    ciphertext = public_key.encrypt(
        message_bytes,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return ciphertext


def decrypt_message(ciphertext, private_key):
    # Decrypt the ciphertext using the private key
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    # Convert the decrypted bytes back to string
    return plaintext.decode()


# Example usage
message = "Karachi University"
print("Text:", message)
# Generate RSA key pair
private_key, public_key = generate_rsa_keypair()
# Encrypt the message using the public key
encrypted = encrypt_message(message, public_key)
# Print the encryptedciphertext in hexadecimal format
print("Encrypted:", encrypted.hex())
# Decrypt the ciphertext using the private key
decrypted = decrypt_message(encrypted, private_key)
print("Decrypted:", decrypted)
