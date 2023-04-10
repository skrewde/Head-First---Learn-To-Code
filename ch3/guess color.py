# Colour guessing game in Python

# Import random module for use later.
import random

# A list containing the possible choices
color = ['blue', 'red', 'yellow', 'purple', 'orange', 'green', 'black', 'white']

# Pick a random choice using the random.choice() function
color_choice = random.choice(color)

guess = ''
guesses = 0

# Guessing game logic
while guess != color_choice:
    # Prompt user to guess, Save guess as a varible and update number of guesses
    guess = input('What color am I thinking of? ')
    guesses = guesses + 1

# Unlike in rock.py, concatenation wasn't used here because guesses isn't a string
# An if statement is used here to catch the 'guesses == 1' typo exception
if guesses == 1:
    print('You got it! It took you', guesses ,'guess!')
else:
    print('You got it! It took you', guesses ,'guesses!')