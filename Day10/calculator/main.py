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

def operation(symbol, num1, num2):
    if symbol == "+":
        return num1 + num2
    
    elif symbol == "-":
        return num1 - num2
    
    elif symbol == "/":
        return num1 / num2
    
    else:
        return num1 * num2

operations = {
    #llama a las funciones de acuerdo a la clave que se elige
    "+": add,
    "-": substract,
    "*": multiply,
    "/": division
}

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Choose an operation symbol from above: ")
result = operation(operation_symbol, a, b) #guarda lo que retorne final_operation

print(f"{a} {operation_symbol} {b} = {result}")


