alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    cipher_text = []
    for letter in text: #para saber qué letras hay en la palabra
        position = alphabet.index(letter) #index me ayuda a encontrar la posición del dato entre parentesis
        new_position = position + shift
        new_letter = alphabet[new_position]
        cipher_text.append(new_letter)

    print(f"{''.join(cipher_text)}") #concatena los elementos de la lista, '' hace que no quede espacio entre ellos
                

#TODO-1: Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.

def decrypt(text, shift):
    plain_text = []
    for letter in text: #para saber qué letras hay en la palabra
        position = alphabet.index(letter) #index me ayuda a encontrar la posición del dato entre parentesis
        new_position = position - shift
        new_letter = alphabet[new_position]
        plain_text.append(new_letter)

    print(f"{''.join(plain_text)}")


if direction == "encode":
    encrypt(text, shift)
else:
    decrypt(text, shift)
