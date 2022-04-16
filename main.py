#import module

from distutils.command import clean
import random

from word_list import word_list
from graphics import logo,stage

from os import system, name 
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 

# write a code for random chosen word by computer
chosen_word = random.choice(word_list)
print(chosen_word)

# find length of chosen word 

len_chosen_word = len(chosen_word)

# Lifeline for hangman gaming

lifeline = 5

# make a emplty list

display = []

for i in range(len_chosen_word):

    display += "_"

end_game = False

print(logo)
print("Welcome in Hangman game  :")


while not end_game :
    print(display)
    print(f"Your Remain Lifeline For Guessing Letter is : {stage[lifeline]}")


    guess = input("Enter a word : ").lower()  # Take a letter from user and change into a lower case

    clear()

    # if guess in chosen_word :
    #     print(display)

    

 

    for position in range(0,len_chosen_word):

        if guess == chosen_word[position]:

            

            display[position] = chosen_word[position]
            

    if guess not in chosen_word :
        lifeline-=1

        

    if lifeline == 0 :
        print("You Loose This Game Looser")
        end_game = True

    if "_" not in display :
        end_game = True
        print("Winner winner Chicken Dinner")