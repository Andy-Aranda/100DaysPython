from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
shift = shift % 26 #si tenemos un número muy largo, usamos el módulo
#si tenemos 100, por ejemplo, se va a hacer la operación de cuántas veces cabe 26 en 100 y el restante
#es el número de la posición


def caesar(text, shift, direction):
    new_text = []
    for char in text: #para cada caracter que este en el texto hacer:
        if char in alphabet: #si el caracter es una letra (esta en la lista alfabeto)
            position = alphabet.index(char) #index me ayuda a encontrar la posición del dato entre parentesis en la lista alphabet
            if direction == "encode": #si tengo que encodear
                new_position = position + shift #si tengo que codificar, sumo la posición y el resultado es mi nueva posiciom
            else:
                new_position = position - shift #si no, la resto y esa es mi nueva posicion
            new_char = alphabet[new_position] #el nuevo caracter (la nueva letra) es la que esta en la posicion new_position
            #en alphabet
            new_text.append(new_char) #agrego esa nueva letra a la lista new_text
        else: #si el caracter no es una letra
            new_text.append(char) #lo agrego a new_text sin cambiarlo

    if direction == "encode":
        print(f"El texto cifrado es: {''.join(new_text)}") #concatena los elementos de la lista, '' hace que no quede espacio entre ellos
    else:
        print(f"El texto descifrado es: {''.join(new_text)}") #concatena los elementos de la lista, '' hace que no quede espacio entre ellos

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
caesar(text, shift, direction)

restart = True

while restart:
    again = input("Do you want to go again? Y/N: ").lower()
    if again == "n":
        restart = False
    else:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26 #si tenemos un número muy largo, usamos el módulo
        caesar(text, shift, direction)

print("Come back soon!")




