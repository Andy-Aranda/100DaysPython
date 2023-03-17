dictionary1= {
    "Bug": "An error in a program.",
    "Function": "A piece of code that you can easily call over again and again.",
    "Loop": "The action of do something again and again."
    }

'''para extraer algo de un diccionario puedo sólo escribirlo como si fuera una lista'''

#print(dictionary1["Bug"]) #me refiero al contenido usando la clave
#si escribo mal la clave me arrojará un error

dictionary2 = {
    123 : "Numero de ejemplo 123",
}

#print(dictionary2[123])

'''Para agregar elementos al diccionario basta con que lo hagamos de la siguiente manera:'''

dictionary1["if"] = "Sentence that ask if something is real, then do something."

#print(dictionary1)

'''Puedo crear un diccionario vacío así'''

empty_dictionary = {}

'''También puedo borrar un diccionario sin asignarle nada a uno ya existente que tiene
contenido'''

#dictionary1 = {}

'''Para editar elementos de un diccionario'''

#dictionary1["Bug"] = "A moth in your computer" #cambié el valor que contiene la llave

'''Para imprimir cada elemento de un diccionario (llaves y valores) hago lo siguiente'''

for key in dictionary1:
    print(key) #esto devuelve la llave
    print(dictionary1[key]) #esto devuelve el valor