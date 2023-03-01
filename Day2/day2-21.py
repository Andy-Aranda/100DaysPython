'''Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8

Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

Example Input
39
Example Output
3 + 9 = 12
12'''


# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

first_number = two_digit_number[0]
second_number = two_digit_number[1]


first_number_int = int(first_number)
second_number_int = int(second_number)
sum = first_number_int + second_number_int
sum_str = str(sum)


print(first_number + " + " + second_number + " = "+ sum_str)

print(sum_str)