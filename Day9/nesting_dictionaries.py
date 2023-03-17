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

travel_log["France"]["total_visits"] = 1 #agrego una nueva llave al diccionario "France" (primero lo creé como lista, ahora es diccionario con una lista
#dentro, su key es cities_visited y el valor es una lista)
#la llave es total_visits y el valor es 1 porque sólo he ido una vez

travel_log["Switzerland"] = {"cities_visited": ["Geneva"], "total_visits": 1}

travel_log["Colombia"] = {"cities_visited": ["Bogotá", "Santa Marta"], "total_visits": 3}



#print(f"travel_log = {travel_log}")
for country in travel_log: #para cada llave en travel_log
    print(country) #imprime el país (llave)
    print(travel_log[country]) #imprime el valor de la llave, se accede así: nombre_de_la_lista[key] (así accedo al valor de la llave)

'''es mejor anidar listas en diccionarios o diccionarios en diccionarios, 
por la forma en que se estructuran los datos'''