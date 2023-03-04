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

elements = [paper, scissors, rock]
"""Aquí el usuario escoge qué quiere jugar"""

my_choose = int(input("\nWhat do you choose? Type 0 for paper, 1 for scissors or 2 for rock: "))

if my_choose == 0:
    print("\nYou choose paper")

elif my_choose == 1:
    print("\nYou choose scissors")

else:
    print("\nYou choose rock")

print(elements[my_choose])

computer_choice = ["paper", "scissors", "rock"]

computer_election_num = random.randint(0, len(computer_choice)-1) #eleccion de la pc

computer_choice = computer_choice[computer_election_num]

print(f"\nComputer choose {computer_choice}\n")
print(elements[computer_election_num])

if my_choose == 0 and computer_election_num == 2: 
    print("You win")

elif computer_election_num == 0 and my_choose == 2:
    print("You lose")

elif my_choose > computer_election_num:
    print("You win")

elif my_choose < computer_election_num:
    print("You lose")

elif my_choose == computer_election_num:
    print("Try again. You both win.")

else:
    print("You lose")