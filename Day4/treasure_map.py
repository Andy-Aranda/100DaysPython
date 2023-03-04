
# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal = int(position[0]) #filas
vertical = int(position[1]) #columnas

map[vertical - 1][horizontal - 1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")




""" # 🚨 Don't change the code below 👇
row1 = ["O","O","O"]
row2 = ["O","O","O"]
row3 = ["O","O","O"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

column = position[0]
row = position[1]

if row == "1":
    if column == "1":
        row1 = ["x","O","O"]
    elif column == "2":
        row1 = ["O","x","O"] 
    else:
        row1 = ["O","O","x"]
elif row == "2":
    if column == "1":
        row2 = ["x","O","O"]
    elif column == "2":
        row2 = ["O","x","O"] 
    else:
        row2 = ["O","O","x"]
else:
    if column == "1":
        row3 = ["x","O","O"]
    elif column == "2":
        row3 = ["O","x","O"]  
    else:
        row3 = ["O","O","x"] 
    


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

"""
