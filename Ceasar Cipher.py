def encrypt(message, shift):
    encrypted_text = ""

    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted_text += char

    return encrypted_text


def decrypt(message, shift):
    decrypted_text = ""

    for char in message:
        if char.isalpha():
            if char.isupper():
                decrypted_text += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted_text += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted_text += char

    return decrypted_text


while True:
    print("\n--- Caesar Cipher ---")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))

        encrypted = encrypt(message, shift)
        print("Encrypted Message:", encrypted)

    elif choice == '2':
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value: "))

        decrypted = decrypt(message, shift)
        print("Decrypted Message:", decrypted)

    elif choice == '3':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
