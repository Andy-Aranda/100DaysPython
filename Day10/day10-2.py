def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "There's no name"
    
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"Result: {formated_f_name} {formated_l_name}"

print(format_name(input("Whats your first name: "), input("Whats your last name: ")))

#usamos print en la linea 10 porque está imprimiendo lo que retorna la función, en ese caso, el resultado