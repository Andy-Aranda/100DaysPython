capitals = {
    "France": "Paris",
    "Mexico": "Mexico City",
}

travel_log = {
    "France": ["Lyon", "Paris", "Grenoble"],
    "Switzerland": ["Geneve"],
}

#aquí estoy cambiando en la key Francia el valor, el nuevo valor es un diccionario que contiene 
#como key las ciudades visitadas y añade las ciudades como una lista:
travel_log["France"] = {"cities_visited": ["Lyon", "Grenoble", "Meudon", "Paris"]}

print(travel_log)

'''es mejor anidar listas en diccionarios o diccionarios en diccionarios, 
por la forma en que se estructuran los datos'''