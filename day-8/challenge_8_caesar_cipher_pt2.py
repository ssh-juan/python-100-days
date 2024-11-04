#Final Project Day 8 - Caesar Cipher
#4nd November 2024
#Pt2 - Decryption
#Her link: https://appbrewery.github.io/python-day8-demo
import caesar_cipher_logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# def encrypt(original_text, shift_amount):
#     encrypted_text = ""
#     for letter in original_text:
        
#         shifted_position = alphabet.index(letter) + shift_amount

#         shifted_position %= len(alphabet)
#         encrypted_text += alphabet[shifted_position]
    
#     print(f"The encrypted word is {encrypted_text}")

# def decrypt(original_text, shift_amount):
#     decrypted_text = ""
#     for letter in original_text:
        
#         shifted_position = alphabet.index(letter) - shift_amount

#         shifted_position %= len(alphabet)
#         decrypted_text += alphabet[shifted_position]
    
#     print(f"The decrypted word is {decrypted_text}")

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def caesar(original_text, shift_amount, direction):
    output_text = ""
    for letter in original_text:
        
        if direction == "decode":
            shift_amount *= 1
        
        shifted_position = alphabet.index(letter) + shift_amount

        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    
    print(f"The {direction}d word is {output_text}")