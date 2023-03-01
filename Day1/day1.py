# Band name generator program
#So easy

print("Welcome to the banda name generator program\n")
city = input("What's the name of the city you grew up?\n")
pet = input("What's the name of your pet?\n")


def band_name(city,pet):

    name_band = ("The name of your band is " + city + " " + pet + " satanica")

    return(name_band)

print(band_name(city,pet))

'''
The code of the teacher:


print("Welcome to the Band Name Generator.")
street = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)
'''