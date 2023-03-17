dictionary1= {
    "Bug": "An error in a  program.",
    "Function": "A piece of code that you can easily call over again and again.",
    "Loop": "The action of do something again and again."
    }

'''para extraer algo de un diccionario puedo sólo escribirlo como si fuera una lista'''

print(dictionary1["Bug"]) #me refiero al contenido usando la clave
#si escribo mal la clave me arrojará un error

dictionary2 = {
    123 : "Numero de ejemplo 123",
}

print(dictionary2[123])

'''Para agregar elementos al diccionario basta con que lo hagamos de la siguiente manera:'''

dictionary1["if"] = "Sentence that ask if something is real, then do something."

print(dictionary1)

'''Puedo crear un diccionario vacío así'''

empty_dictionary = {}