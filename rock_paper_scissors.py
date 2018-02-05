# everything is in main right now

# import the random module
from random import randint

def computer_choice(user_stat):

    max_val = max(user_stats, key=user_stats.get)
    max_vals = [x for x, v in user_stats.items() if v == user_stats[max_val]]
    print max_vals



print("Hello and welcome to Rock Paper Scissors.")
user_input = input("Enter 0 for Rock, 1 for Paper, 2 for Scissors, or Q to quit:")

user_stats = {'rock': 0, 'paper': 0, 'scissors': 0 }
game_stats = {'wins': 0, 'games': 0}
options = ['Rock', 'Paper', 'Scissors']

# loop through until the user enters 'Q'
while user_input != 'Q':

    if user_input not in ['0','1', '2']:
        raise Exception('You must enter 0, 1, 2 or Q')
    
    user_choice = int(user_input)

    rock = 0
    paper = 1
    scissors = 2 

    # get the computer input
    computer_choice = randint(0,2)

    if user_choice == computer_choice:
        
        print('It is a draw! You both played {}'.format(options[user_choice]))
        user_stats[options[user_choice].lower()] += 1

    elif user_choice == 0:

        if computer_choice == 1:
            print('You lose this round! Paper beats Rock')

        elif computer_choice == 2:
            print('You win this round! Rock beats Sicssors')

    elif user_choice == 1:

        if computer_choice == 0:
            print('You win this round! Paper beats Rock')

        elif computer_choice == 2:
            print('You lose this round! Sicssors beats Paper')

    
    elif user_choice == 2:

        if computer_choice == 0:
            print('You lose this round! Rock beats Sicssor')

        elif computer_choice == 1:
            print('You win this round! Sicssors beats Paper')

    except Exception as e:
        print str(e)
    
    finally:
        user_input = input("Enter 0 for Rock, 1 for Paper, 2 for Scissors, or Q to quit:")

# Print the output
print 'Number of games played: {}'.format(game_stats['games'])
print 'Number of game won {}'.format(game_stats['wins'])
