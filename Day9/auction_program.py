from art import logo
import os

print(logo)



def apuestas(nombre, valor):

    apuestas = {}
    apuestas[nombre] = valor
    max_valor = 0
    max_apostador = 0
    max_apostador = "Nadie"

    respuesta = input("Quieres agregar a alguien? y/n: ").lower()


    while respuesta == "y":
        os.system("clear")
        nombre = input("Whats your name? ")
        valor = int(input("Whats your bid? $"))
        if valor > max_valor:
            max_valor = valor
            max_apostador = nombre
            apuestas[nombre] = valor

        respuesta = input("Quieres agregar a alguien? y/n: ").lower()


    print(f"El ganador es {max_apostador} con ${max_valor}")


nombre = input("Whats your name? ")
valor = int(input("Whats your bid? $"))

apuestas(nombre, valor)