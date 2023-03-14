alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() 
# functions into a single function called caesar(). 

def caesar(text, shift, direction):
    new_text = []
    for letter in text: #para saber qué letras hay en la palabra
        position = alphabet.index(letter) #index me ayuda a encontrar la posición del dato entre parentesis
        if direction == "encode":
            new_position = position + shift
        else:
            new_position = position - shift
        new_letter = alphabet[new_position]
        new_text.append(new_letter)
        
    if direction == "encode":
        print(f"El texto cifrado es: {''.join(new_text)}") #concatena los elementos de la lista, '' hace que no quede espacio entre ellos
    else:
        print(f"El texto decifrado es: {''.join(new_text)}") #concatena los elementos de la lista, '' hace que no quede espacio entre ellos


caesar(text, shift, direction)








#TODO-2: Call the caesar() function, 
# passing over the 'text', 'shift' and 'direction' values.