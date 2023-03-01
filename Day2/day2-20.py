#We can't add diferent types of data if we want to print it

num_char = len(input("Whats your name? "))

#But we can change the type of data to conctatenate it

new_num_char = str(num_char)

#and then we can print it

print("Your name has " + new_num_char + " characters.")

#we can check what type of data a variable has

a = 13524
print(type(a))