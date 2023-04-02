from art import logo
print(logo)

def add(a, b):
    '''Función para sumar dos números'''
    return a + b

def substract(a, b):
    '''Función para restar dos números'''
    return a - b

def division(a, b):
    '''Función para dividir dos números'''
    return a / b

def multiply(a, b):
    '''Función para multiplicar dos números'''
    return a * b

operations = {
    #llama a las funciones de acuerdo a la clave que se elige
    "+": add,
    "-": substract,
    "*": multiply,
    "/": division
}

a = int(input("Enter the first number: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Choose an operation symbol from above: ")
result = operations[operation_symbol] #guarda lo que retorne la operación seleccionada de acuerdo a operations
b = int(input("Enter the second number: "))
result = result(a, b)

print(f"{a} {operation_symbol} {b} = {result}")


