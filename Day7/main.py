import random
import os
from hangman_art import logo, stages
from hangman_words import word_list


end_of_game = False
word_list = word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
part_of_the_body = -1
part_of_the_body_old = part_of_the_body
lives = 6

print(logo)
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

#Use a while loop to let the user guess again. 
# The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks 
# ("_"). Then you can tell the user they've won.

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    os.system("clear")

    if guess in display:
      print(f"You've already choose this letter {guess} and is correct")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
      print(f"Your election {guess} is not in the chosen word. -1 live")
      lives -= 1


    print(f"{' '.join(display)}")
    print(stages[lives])

    #Check if there are no more "_" left in 'display'. Then all letters have been guessed.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    elif lives == 0:
        end_of_game = True
        print(f"You lose. The word was {chosen_word}")


    
