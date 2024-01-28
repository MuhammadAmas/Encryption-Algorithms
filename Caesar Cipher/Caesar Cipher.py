def get_base_index(char_code):
    if 97 <= char_code <= 122:
        return 97
    elif 65 <= char_code <= 90:
        return 65
    else:
        return None


def transform_character(char_code, key, is_encrypt):
    base_index = get_base_index(char_code)

    if base_index is not None:
        char_code -= base_index
        if is_encrypt:
            char_code = (char_code + key) % 26 + base_index
        else:
            char_code = (char_code - key) % 26 + base_index
        return chr(char_code)
    else:
        return chr(char_code)


def encrypt(text, key):
    cipher_text = ''

    for character in text:
        encrypted_character = transform_character(ord(character), key, True)
        cipher_text += encrypted_character

    return cipher_text


def decrypt(text, key):
    decrypted_text = ''

    for character in text:
        decrypted_character = transform_character(ord(character), key, False)
        decrypted_text += decrypted_character

    return decrypted_text


def main():
    input_text = "Cryptography!"
    encryption_key = 3

    encrypted_text = encrypt(input_text, encryption_key)
    decrypted_text = decrypt(encrypted_text, encryption_key)

    print("Original text:", input_text)
    print("Encrypted text:", encrypted_text)
    print("Decrypted text:", decrypted_text)


if __name__ == "__main__":
    main()
