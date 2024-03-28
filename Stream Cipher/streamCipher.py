def streamcipher():
    option = input("Press 1 for encryption and 2 for decryption :")
    if (option == 1):
        binary = input("Enter the plaintext in binary: ")
    else:
        binary = input("Enter the ciphertext in binary: ")

    key = input("Enter the Key in binary: ")
    plaintext = int(binary, 2)
    key = int(key, 2)
    ciphertext = plaintext ^ key
    print(ciphertext)
    if (option == 1):

        print("Ciphertext is :", bin(ciphertext)[2:])
    else:
        print("Plaintext is :", bin(ciphertext)[2:])


streamcipher()

"""
Press 1 for encryption and 2 for decryption :1
Enter the plaintext in binary: 101010
Enter the Key in binary: 110011
Ciphertext is : 011001
011001 is 6
"""
