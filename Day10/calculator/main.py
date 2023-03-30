from art import logo

def add(a, b):
    '''Función para sumar dos números'''
    return a + b
    pass

def substract(a, b):
    '''Función para restar dos números'''
    return a - b
    pass

def division(a, b):
    '''Función para dividir dos números'''
    return a / b
    pass

def multiply(a, b):
    '''Función para multiplicar dos números'''
    return a * b
    pass

operations = {
    #llama a las funciones de acuerdo a la clave que se elige
    "+": add,
    "-": substract,
    "*": multiply,
    "/": division
}

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))