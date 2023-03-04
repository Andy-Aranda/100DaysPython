# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#position = random.randint(0, len(names))
#payer = names[position]
'''abajo estoy poniendo lo mismo que arriba pero en una sola línea de código'''
payer = names[random.randint(0, (len(names)-1))] #porque len me va a decir el total de elementos, pero 
#se empieza a contar en cero, entonces es el total -1

'''otra opcion pudo ser con el modulo random.choice() como se muestra abajo'''
#payer = random.choice(names)

print(f"{payer} is going to buy the meal today!")
