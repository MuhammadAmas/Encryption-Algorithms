def get_base_index(char_code):
    if 97 <= char_code <= 122:
        return 97
    elif 65 <= char_code <= 90:
        return 65
    else:
        return None


def encrypt(text, key):
    cipher_text = ''

    for character in text:
        char_code = ord(character)
        starting_index = get_base_index(char_code)

        if starting_index is not None:
            char_code -= starting_index
            char_code = ((char_code + key) % 26 + starting_index)
            cipher_character = chr(char_code)
            cipher_text += cipher_character
        else:
            cipher_text += character

    return cipher_text


def decrypt(text, key):
    decrypted_text = ''

    for character in text:
        char_code = ord(character)
        starting_index = get_base_index(char_code)
        if starting_index is not None:
            char_code -= starting_index
            char_code = ((char_code - key) % 26 + starting_index)
            decrypted_character = chr(char_code)
            decrypted_text += decrypted_character
        else:
            decrypted_text += character

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
