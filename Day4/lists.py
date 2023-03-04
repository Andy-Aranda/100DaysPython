fruits = ["Cherry", "Apple", "Grapes"]
states_of_america = ["Delaware", "Pennsylvania", "Nueva York", "Texas"] #...etc

print(states_of_america[0])

print(states_of_america[-2]) #puedo agregar numeros negativos y comenzara a contar 
#desde atras

#puedo cambiar el dato de una posicion

states_of_america[0] = "Washington" #cambie Delaware por Washington

states_of_america.append("New Mexico") #puedo añadir elementos a la lista

states_of_america.extend(["Candyland", "Lulaland", "Canelaland"]) #uso extend para agregar otra lista a 
#la lista

#o puedo declarar la lista y luego usar extend
mis_lugares = ["Izcalli", "Santa Fe"]

states_of_america.extend(mis_lugares)

print(states_of_america)

