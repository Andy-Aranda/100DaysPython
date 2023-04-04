from art import logo


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

def calculator():
    print(logo)
    a = float(input("Enter the first number: "))

    for symbol in operations:
        print(symbol)

    restart = True

    while restart:
        operation_symbol = input("Choose an operation symbol from above: ")
        b = float(input("Enter the second number: "))
        result = operations[operation_symbol] #guarda lo que retorne la operación seleccionada de acuerdo a operations
        result1 = result(a, b) #en result se guarda lo que resulte de llamar a result (que ees una funcio+on definida en la línea 34 para )
        print(f"{a} {operation_symbol} {b} = {result1}")


        if input("Do you want to realize another operation? Y/N ").lower() == "y":
            a = result1
        else:
            restart = False
    print("Come back soon!")


calculator()


