for number in range (1, 10): #en el rango que yo le de, va a imprimir los números
    print(number)
print("\n")
for number in range (1, 10, 3): #si quiero que avance de 3 en 3 lo especifico en el tercer
    #indice de lo que recibe
    print(number)

'''Si quisiera obtener el total de la suma de los numeros
del 1 al 100'''

print("\n")

total = 0
for number in range(1, 101):
    total += number
print(total)
