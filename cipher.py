def caesar_encrypt(text, shift):
    encrypted_text = ""
    # Loop through each character in the plaintext
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Determine whether it's uppercase or lowercase
            if char.isupper():
                # Apply the shift for uppercase letters
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Apply the shift for lowercase letters
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            # For non-alphabetic characters, just append them unchanged
            encrypted_text += char
    return encrypted_text

# Function to decrypt Caesar cipher (optional)
def caesar_decrypt(text, shift):
    # Implement the decryption logic here
    pass

def main():
    # Get user input
    plaintext = input("Enter the message to encrypt: ")
    shift = int(input("Enter the shift value: "))
    
    # Encrypt the message
    encrypted_message = caesar_encrypt(plaintext, shift)
    print("Encrypted message:", encrypted_message)

    # Decrypt the message (optional)
    # decrypted_message = caesar_decrypt(encrypted_message, shift)
    # print("Decrypted message:", decrypted_message)

if __name__ == "__main__":
    main()



