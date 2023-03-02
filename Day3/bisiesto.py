# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year%4 == 0:
    if year%100 == 0:
        if year%400 == 0:
            print(f"El año {year} es bisiesto")
        else:
            print(f"El año {year} no es bisiesto")
    else:
        print(f"El año {year} es bisiesto")
else:
    print(f"El año {year} no es bisiesto")