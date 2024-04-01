
def caesar_encrypt(plaintext, shift):
    encrypted_text = ""  
    for char in plaintext: 
        if char.isalpha():  
            if char.isupper():  
                # Apply shift to uppercase letters
                encrypted_text += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:  # The character is lowercase
                # Apply shift to lowercase letters
                encrypted_text += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:  # If the character is not a letter.
            encrypted_text += char 
    return encrypted_text 

def main():
    # Prompt the user to enter the plaintext message.
    plaintext = input("please enter your message here: ")
    shift = int(5)
    
    encrypted_message = caesar_encrypt(plaintext, shift)
    print("Encrypted message:", encrypted_message)

<<<<<<< HEAD

=======
if __name__ == "__main__":
    main()
