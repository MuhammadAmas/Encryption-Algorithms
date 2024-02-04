def generate_vigenere_table():
    vigenere_table = [[chr((i + j) % 26 + 65)
                       for j in range(26)] for i in range(26)]
    return vigenere_table


def print_vigenere_table(table):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    print("    ", end="")
    for letter in alphabet:
        print(f"{letter}   ", end="")
    print("\n   -----------------------------------------")

    for i, row in enumerate(table):
        print(f"{alphabet[i]} |", end="")
        for entry in row:
            print(f"  {entry} ", end="")
        print()
