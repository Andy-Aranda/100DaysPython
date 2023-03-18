travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, visits, cities):
    travel_log.append({"country": country, "visits": visits, "cities": cities})
    
    """
    Otra opción para hacerlo es así:

    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)

    """
    
#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)
""" for element in travel_log: #para cada llave en travel_log
    print(element) #imprime el valor de la llave, se accede así: nombre_de_la_lista[key] (así accedo al valor de la llave)
 """