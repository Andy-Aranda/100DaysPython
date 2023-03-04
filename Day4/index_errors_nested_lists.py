""" states_of_america = ["Delaware", "Pennsylvania", "Nueva York", "Texas"] #...etc

num_of_states = len(states_of_america)

#print(states_of_america[num_of_states]) 

#esta linea de arriba me da error porque busco el indice 4 cuando 
#el indice mayor es 3, porque empiezo a contar en 0 

print(states_of_america[num_of_states - 1]) #esta linea no arrojará error

fruits = ["Pera", "Manzana", "Uva", "Limón"]
vegetables = ["Jitomate", "Papa", "Chile", "Calabaza"]
fruver = [fruits, vegetables] #lista anidada

print(fruver) """

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen[1][0]) #el primer indice indica la lista, el segundo la posicion del
#elemento a extraer 