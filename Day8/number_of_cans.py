import math

#Write your code below this line ๐
def paint_calc(height, width, cover):
    number_of_cans = (height*width)/cover
    number_of_cans =math.ceil(number_of_cans) #para redondear al nรบmero que sigue
    #aunque el decimal sea menor a .5
    print(f"You'll need {number_of_cans} cans of paint.")

#Write your code above this line ๐
# Define a function called paint_calc() so that the code below works.   

# ๐จ Don't change the code below ๐
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)