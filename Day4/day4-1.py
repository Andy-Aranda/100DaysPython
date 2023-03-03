import random

random_int = random.randint(1, 10) #numero aleatorio entre 1 y 10
print(random_int)

random_float = random.random() #numero aleatorio entre 0 y 1
print(random_float)

random_float_upper5 = random.random() * 5 #no hay forma de generar números flotantes aleatorios
#pero puedo generar un numero aleatorio entre 0 y 1 y multiplicarlo por 5 para tener numeros aleatorios 
#entre 0 y 5
random_float_upper5 = round(random_float_upper5, 1) #usamos round para redondear los decimales de
#nuestro número a sólo uno
print(random_float_upper5)