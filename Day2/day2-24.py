print(8/3)
print(int(8/3)) #para que sea un entero lo que sakga, sin decimales
print(round(8/3)) #para redondear el número al siguiente número más alto
print(round(8/3, 2)) #para decirle cuántos dígitos después del punto quiero que se impriman 
print(8//3) #lo mismo que en la línea 2

#también podemos escribir el resultado en una variable y luego usarlo nuevamente
result = 4/2
result/=2 #es como result += result
print(result)

#f-string
'''cuando tenemos una cadena de texto que queremos mezclar con otros tipos de datos al momento de imprimir'''

score = 0
height = 1.8
isWinning = True
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")