#functions with outputs

def format_name(f_name, l_name):
    '''Vamos a hacer que los nombres que agreguemos empiecen por mayúscula, 
    sin importar como los ingrese el usuario con .title()'''
    name = f_name.title()
    last_name = l_name.title()
    return f"{name} {last_name}"




""" f_name = input("What's your first name? ")
l_name = input("What's your last name? ") """

#format_name("f_name", "l_name")

print(format_name("ANDREA", "arAndA"))