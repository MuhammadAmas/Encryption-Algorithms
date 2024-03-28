def encrypt_rail_fence(text, key):
    rail = ['' for _ in range(key)]
    direction = 1
    level = 0
    for char in text:
        rail[level] += char
        level += direction
        if level == key - 1 or level == 0:
            direction *= -1
    return ''.join(rail)


def decrypt_rail_fence(ciphertext, key):
    rail = ['' for _ in range(key)]
    direction = 1
    level = 0
    for char in ciphertext:
        rail[level] += '*'
        level += direction
        if level == key - 1 or level == 0:
            direction *= -1
    idx = 0
    for i in range(key):
        for j in range(len(rail[i])):
            rail[i] = rail[i][:j] + ciphertext[idx] + rail[i][j+1:]
            idx += 1
    direction = 1
    level = 0
    plaintext = ''
    for _ in range(len(ciphertext)):
        plaintext += rail[level][0]
        rail[level] = rail[level][1:]
        level += direction
        if level == key - 1 or level == 0:
            direction *= -1
    return plaintext


# Example
text = "BYE WORLD"
key = 3
encrypted_text = encrypt_rail_fence(text, key)
decrypted_text = decrypt_rail_fence(encrypted_text, key)
print("Original Text:", text)
print("Encrypted Text:", encrypted_text)
print("Decrypted Text:", decrypted_text)
