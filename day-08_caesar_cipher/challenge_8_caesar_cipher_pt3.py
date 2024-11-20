#Final Project Day 8 - Caesar Cipher
#5nd November 2024
#Pt3 - Reorganizing the Code
#Her link: https://appbrewery.github.io/python-day8-demo
import caesar_cipher_logo
print(caesar_cipher_logo.logo)  # TODO-1: Import and print the logo from art.py when the program starts.

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shift_amount, direction):
    output_text = ""
    if direction == "decode":
        shift_amount *= -1

    for letter in original_text:           
        if letter in alphabet:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            output_text += letter
        
    print(f"The {direction}d word is {output_text}")

rerun = ""
while rerun != "no":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text,shift,direction)

    rerun = input("Type 'yes' if you want to go again. Otherwise, type 'no' ")

    if rerun == "no":
        print("Goodbye! =)")
        print("Built by Juan Borges")