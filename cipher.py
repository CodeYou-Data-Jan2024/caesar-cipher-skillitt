# create alphabet dictionary
def create_caesar_cipher_dict(shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    caesar_dict = {}
    for i in range(len(alphabet)):
        caesar_dict[alphabet[i]] = alphabet[(i + shift) % len(alphabet)]
    return caesar_dict

caesar_dict_shift_5 = create_caesar_cipher_dict(5)

print(caesar_dict_shift_5)


#Create a function to encrypt a message using the Caesar cipher
    #- Input: message, shift amount
    #- Output: encrypted message
    #- For each letter in the message, use the shift function to encrypt the letter

def encrypt_caesar_cipher(message, shift_amount):
    encrypted_message = ''
    for letter in message:
        encrypted_message += shift_letter(letter, shift_amount)
    return encrypted_message



