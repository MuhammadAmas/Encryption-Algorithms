from VigenereTable import generate_vigenere_table, print_vigenere_table


def encrypt_vigenere(plaintext, key, method):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key_repeated = (key * (len(plaintext) // len(key))) + \
        key[:len(plaintext) % len(key)]
    ciphertext = ''

    for i in range(len(plaintext)):
        if method == 'matrix':
            ciphertext += generate_vigenere_table()[alphabet.index(
                plaintext[i])][alphabet.index(key_repeated[i])]
        elif method == 'math':
            p_num = ord(plaintext[i]) - 65
            k_num = ord(key_repeated[i]) - 65
            c_num = (p_num + k_num) % 26
            ciphertext += chr(c_num + 65)

    return ciphertext


def decrypt_vigenere(ciphertext, key, method):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    key_repeated = (key * (len(ciphertext) // len(key))) + \
        key[:len(ciphertext) % len(key)]
    plaintext = ''

    for i in range(len(ciphertext)):
        if method == 'matrix':
            row = generate_vigenere_table()[alphabet.index(key_repeated[i])]
            col_index = row.index(ciphertext[i])
            plaintext += alphabet[col_index]
        elif method == 'math':
            c_num = ord(ciphertext[i]) - 65
            k_num = ord(key_repeated[i]) - 65
            p_num = (c_num - k_num) % 26
            plaintext += chr(p_num + 65)

    return plaintext


print("""
      ################################################################################
                                    Vigenère Cipher
      ################################################################################
      """)
plaintext = "GIVEMONEY"
key = "LOCK"
vigenere_table = generate_vigenere_table()
print_vigenere_table(vigenere_table)
print('\n')


# Method 1: Table Matrix
ciphertext_matrix = encrypt_vigenere(plaintext, key, 'matrix')
decrypted_matrix = decrypt_vigenere(ciphertext_matrix, key, 'matrix')

# Method 2: Mathematical Calculation
ciphertext_math = encrypt_vigenere(plaintext, key, 'math')
decrypted_math = decrypt_vigenere(ciphertext_math, key, 'math')

print(f"Plaintext: {plaintext}")
print(f"Key: {key}")

print(f"\nMethod 1 (Table Matrix):")
print(f"Ciphertext: {ciphertext_matrix}")
print(f"Decrypted: {decrypted_matrix}")

print(f"\nMethod 2 (Mathematical Calculation):")
print(f"Ciphertext: {ciphertext_math}")
print(f"Decrypted: {decrypted_math}")
