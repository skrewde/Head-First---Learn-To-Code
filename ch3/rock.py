import random
import time

# Assign the variable winner to an empty string, to be manipulated later
winner = ''

user_wins = 0
computer_wins = 0

# Initial random choice generator (feat. some tests); Lengthy, less readable, & convoluted
    #computer_choice = random.randint(0, 2)

    # if random_choice == 0:
    #     computer_choice = 'rock'
    # elif random_choice == 1:
    #     computer_choice = 'paper'
    # else:
    #     computer_choice = 'scissors'

    #Testing Logic
    #print ('The computer chooses', computer_choice)
    #print('You chose', user_choice,' and the computer chose', computer_choice)

# A list containing the possible choices
choices = ['rock', 'paper', 'scissors']



# user_choice = input('rock, paper, or scissors? \n')
user_choice = ''
computer_choice = ''


while (user_choice != 'rock' and user_choice != 'paper' and user_choice != 'scissors'):
    user_choice = input('rock, paper or scissors? \n').lower()

    # Pick a random choice using the random module
    computer_choice = random.choice(choices)

    # Logic for determining the winner
    if computer_choice == user_choice:
        winner = 'Tie'
    elif computer_choice == 'rock' and user_choice == 'scissors':
        winner = 'Computer'
        computer_wins += 1
    elif computer_choice == 'paper' and user_choice == 'rock':
        winner = 'Computer'
        computer_wins += 1
    elif computer_choice == 'scissors' and user_choice == 'paper':
        winner = 'Computer'
        computer_wins += 1
    else:
        winner = 'User'
        computer_wins += 1

    # Logic for user friendly output
    if winner == 'Tie':
        print('The computer also chose '+ computer_choice+', it\'s a tie :0')
    elif winner == 'Computer':
        print('The computer chose '+ computer_choice+', You lost :(')
    else:
        print('The computer chose '+ computer_choice+', You won!')


def get_scores():
    print("You won", user_wins, "times.")
    print("The computer won", computer_wins, "times.")
    print("Goodbye!")

## TO_DO!
#1 Create a scoreline function that saves the scores even when the program exits. DONE.
#2 Make all permutations of user's choice valid (e.g. All cases of 'rock' like 'Rock' or 'rOCk'). DONE.
#3 Create user input for scoreline function
#4 Make program run indefinitely till user quits