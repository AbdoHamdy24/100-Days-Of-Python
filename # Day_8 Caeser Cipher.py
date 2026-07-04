# Caeser Cipher
alphabet = [' ','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J','K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 
'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z','0','1','2','3','4','5','6','7','8','9']

def encrypt(plain_text , shift_mount):
    new_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_mount
        new_letter = alphabet[new_position]
        new_text += new_letter
    print(f"The encoded text is {new_text}")


def decrypt(cipher_text , shift_mount):
    org_text = ""
    for letter in cipher_text:
        position = alphabet.index(letter)
        new_position = position - shift_mount
        new_letter = alphabet[new_position]
        org_text += new_letter
    print(f"The decoded text is {org_text}")


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n ")

if direction == "encode":
    text = input("Type your message: \n")
    shift = int(input("Type the shift number: \n"))
    encrypt(plain_text=text , shift_mount=shift)  
elif direction == "decode":
    text = input("Type your message: \n")
    shift = int(input("Type the shift number: \n"))
    decrypt(cipher_text=text , shift_mount=shift)  
else:
    print("Incorrect choice!")





