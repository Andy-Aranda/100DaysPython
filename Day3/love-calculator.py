# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()
t_true = (name1_lower.count("t")) + (name2_lower.count("t"))
r_true = (name1_lower.count("r")) + (name2_lower.count("r"))
u_true = (name1_lower.count("u")) + (name2_lower.count("u"))
e_true = (name1_lower.count("e")) + (name2_lower.count("e"))

l_love = (name1_lower.count("l")) + (name2_lower.count("l"))
o_love = (name1_lower.count("o")) + (name2_lower.count("o"))
v_love = (name1_lower.count("v")) + (name2_lower.count("v"))
e_love = (name1_lower.count("e")) + (name2_lower.count("e"))

sum_true = str(t_true+r_true+u_true+e_true)
sum_love = str(l_love+o_love+v_love+e_love)

total = int(sum_true+sum_love)

if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total > 40 and total < 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}.")
