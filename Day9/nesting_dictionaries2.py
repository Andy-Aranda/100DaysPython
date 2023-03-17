'''Aquí se va a explicar cómo usar listas con diccionarios anidados'''

travel_log = {
    'France': {'cities_visited': ['Lyon', 'Grenoble', 'Meudon', 'Paris'], 'total_visits': 1}, 
    'Switzerland': {'cities_visited': ['Geneva'], 'total_visits': 1}, 
    'Colombia': {'cities_visited': ['Bogotá', 'Santa Marta'], 'total_visits': 3}
    } 


'''Vamos a cambiar el diccionario anterior para que cada entrada (país y sus valores) sea un diccionario por sí solo'''

travel_log = [
    #Tenemos una lista con tres diccionarios, cada diccionario tiene tres pares key-value
    {
        "country": 'France', 
        'cities_visited': ['Lyon', 'Grenoble', 'Meudon', 'Paris'], 
        'total_visits': 1
        }, 
    {
        "country": 'Switzerland', 
        'cities_visited': ['Geneva'], 
        'total_visits': 1
        }, 
    {
        "country": 'Colombia', 
        'cities_visited': ['Bogotá', 'Santa Marta'], 
        'total_visits': 3
        },
]