from tkinter import W


print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

tip = percentage_tip / 100
total_tip_amount = total_bill * tip
total = total_bill + total_tip_amount
each_one = total / people

final_amount = round(each_one, 2) #cuando imprimo esto sólo sale un número después del punto
final_amount = "{:.2f}".format(each_one) #si imprimo esto, tengo dos números decimales, no sólo uno

#ejemplo: con la linea 15 tengo sólo 34.9
#con la linea 16 tengo 34.90

print(f"Each person should pay: ${final_amount}")