import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choose = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for scissors: "))

if choose == 0:
    print("You choose rock")

elif choose == 1:
    print("You choose paper")

else:
    print("You choose scissors")

computer_choice = ["Rock", "Paper", "Scissors"]

num = random.randint(0, len(computer_choice)-1) #eleccion de la pc

computer_choice = computer_choice[num]

print(f"\nComputer choose {computer_choice}")

if choose == 0 and num == 2:
    print("You win")

if num == 0 and choose == 2:
    print("You lose")

elif choose > num:
    print("You win")

elif num > choose:
    print("You lose")

elif choose == num:
    print("Try again. You both win.")

else:
    print("You lose")