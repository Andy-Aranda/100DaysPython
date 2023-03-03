print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

first = input("Right or left? R or L: ")
if first.lower() == "r":
    print("Fall into a hole.\n Game over")
else:
    print("Good job!")
second = input("Swim or wait? S or W: ")
if second.lower() == "s":
    print("Attacked by trout\n Game over")
else:
    print("Good job!")
third = input("Which door? Red, blue or yellow? R, B, Y: ")
if third.lower() == "r":
    print("Burned by fire\n Game over")
elif third.lower() == "b":
    print("Eaten by beasts\n Game over")
elif third.lower() == "y":
    print("You win!")
else:
    print("Game over")


