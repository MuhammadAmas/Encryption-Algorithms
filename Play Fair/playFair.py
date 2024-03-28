def prepare_input(text):
    # Replace spaces with X and convert to uppercase
    text = text.replace(" ", "X").upper()

    # Replace J with I
    text = text.replace("J", "I")

    # Add a trailing X if the length is odd
    if len(text) % 2 != 0:
        text += "X"

    return text


def generate_key_square(key):
    # Create a 5x5 matrix (key square) with unique characters from the key
    key = key.upper().replace("J", "I")
    key_square = []
    for char in key:
        if char not in key_square:
            key_square.append(char)

    # Fill in the remaining characters
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for char in alphabet:
        if char not in key_square:
            key_square.append(char)

    # Reshape the list into a 5x5 matrix
    key_square = [key_square[i:i+5] for i in range(0, 25, 5)]

    return key_square


def find_position(matrix, char):
    # Find the position of a character in the key square
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)


def encrypt(text, key):
    # Prepare input and generate key square
    text = prepare_input(text)
    key_square = generate_key_square(key)

    # Perform encryption
    ciphertext = ""
    for i in range(0, len(text), 2):
        char1, char2 = text[i], text[i+1]

        # Find positions in key square
        row1, col1 = find_position(key_square, char1)
        row2, col2 = find_position(key_square, char2)

        # Apply Playfair cipher rules
        if row1 == row2:
            ciphertext += key_square[row1][(col1 + 1) % 5]
            ciphertext += key_square[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += key_square[(row1 + 1) % 5][col1]
            ciphertext += key_square[(row2 + 1) % 5][col2]
        else:
            ciphertext += key_square[row1][col2]
            ciphertext += key_square[row2][col1]

    return ciphertext


def decrypt(ciphertext, key):
    # Prepare input and generate key square
    key_square = generate_key_square(key)

    # Perform decryption
    plaintext = ""
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i+1]

        # Find positions in key square
        row1, col1 = find_position(key_square, char1)
        row2, col2 = find_position(key_square, char2)

        # Apply Playfair cipher rules
        if row1 == row2:
            plaintext += key_square[row1][(col1 - 1) % 5]
            plaintext += key_square[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += key_square[(row1 - 1) % 5][col1]
            plaintext += key_square[(row2 - 1) % 5][col2]
        else:
            plaintext += key_square[row1][col2]
            plaintext += key_square[row2][col1]

    return plaintext


# Example usage:
key = "PLAYFAIR"
plaintext = "AGENDA"
ciphertext = encrypt(plaintext, key)
decrypted_text = decrypt(ciphertext, key)

print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
print("Decrypted Text:", decrypted_text)
