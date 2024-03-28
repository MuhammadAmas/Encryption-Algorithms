MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', ' ': '/'}


def encrypt(text):
    encrypted_text = ''
    for char in text:
        if char.upper() in MORSE_CODE_DICT:
            encrypted_text += MORSE_CODE_DICT[char.upper()] + ' '
        else:
            encrypted_text += ' '
    return encrypted_text


def decrypt(morse_code):
    morse_code = morse_code.split(' ')
    decrypted_text = ''
    for code in morse_code:
        for key, value in MORSE_CODE_DICT.items():
            if code == value:
                decrypted_text += key
    return decrypted_text


# Example usage:
text_to_encrypt = "Muhammad Amas"
encrypted_text = encrypt(text_to_encrypt)
print(f"Original text: {text_to_encrypt}")
print(f"Encrypted text: {encrypted_text}")

decrypted_text = decrypt(encrypted_text)
print(f"Decrypted text: {decrypted_text}")
