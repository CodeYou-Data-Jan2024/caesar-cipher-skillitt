# create alphabet dictionary
def create_caesar_cipher_dict(shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    caesar_dict = {}
    for i in range(len(alphabet)):
        caesar_dict[alphabet[i]] = alphabet[(i + shift) % len(alphabet)]
    return caesar_dict

caesar_dict_shift_5 = create_caesar_cipher_dict(5)

print(caesar_dict_shift_5)





#Create a function to shift a single letter by a specified amount
    #- Input: letter, shift amount
    #- Output: shifted letter
    #- Shift the letter by the specified amount, considering wrapping around the alphabet

def shift_letter(letter, shift_amount):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    if letter in alphabet:
        shifted_index = (alphabet.index(letter) + shift_amount) % 26
        shifted_letter = alphabet[shifted_index]
        return shifted_letter
    else:
        return letter 
    
    original_letter = 'a'
shifted_letter = shift_letter(original_letter, 5)
print(shifted_letter)


#Create a function to encrypt a message using the Caesar cipher
    #- Input: message, shift amount
    #- Output: encrypted message
    #- For each letter in the message, use the shift function to encrypt the letter



#Create a function to decrypt a message encrypted with the Caesar cipher
    #- Input: encrypted message, shift amount
    #- Output: decrypted message
    #- For each letter in the encrypted message, use the shift function to decrypt the letter

