# everything is in main right now

# import the random module
from random import randint

def computer_brain(user_stats):

    max_val = max(user_stats, key=user_stats.get)
    max_vals = [x for x, v in user_stats.items() if v == user_stats[max_val]]

    if len(max_vals) > 1:
        decision = randint(0, len(max_vals))
    else:
        decision = 0
    
    choice = max_vals[decision]

    if choice == 'rock':
        return 1 
    elif choice == 'paper':
        return 2
    elif choice == 'scissors':
        return 0

computer_brain({'trace':0, '2':2, '3':3, '4': 3})

print("Hello and welcome to Rock Paper Scissors.")
user_input = raw_input("Enter 0 for Rock, 1 for Paper, 2 for Scissors, or Q to quit: ")

user_stats = {'rock': 0, 'paper': 0, 'scissors': 0 }
game_stats = {'wins': 0, 'games': 0}
options = ['Rock', 'Paper', 'Scissors']

# loop through until the user enters 'Q'
while user_input != 'Q':

    try:
        if user_input not in ['0','1', '2']:
            raise Exception('You must enter 0, 1, 2 or Q')
    
        user_choice = int(user_input)

        # Update the user's choice 
        user_stats[options[user_choice].lower()] += 1 

        # get the computer input
        computer_choice = computer_brain(user_stats)

        # Set the win variable to false until a user wins
        win = False

        if user_choice == computer_choice:
            
            print('It is a draw! You both played {}'.format(options[user_choice]))

        elif user_choice == 0:

            if computer_choice == 1:
                print('You lose this round! Paper beats Rock')

            elif computer_choice == 2:
                print('You win this round! Rock beats Sicssors')
                win = True

        elif user_choice == 1:

            if computer_choice == 0:
                print('You win this round! Paper beats Rock')
                win = True

            elif computer_choice == 2:
                print('You lose this round! Sicssors beats Paper')

        
        elif user_choice == 2:

            if computer_choice == 0:
                print('You lose this round! Rock beats Sicssor')

            elif computer_choice == 1:
                print('You win this round! Sicssors beats Paper')
                win = True

        # Update the game stats
        game_stats['games'] += 1
        if win == True:
            game_stats["wins"] += 1
    
    except Exception as e:
        print str(e)
    
    finally:
        user_input = raw_input("Enter 0 for Rock, 1 for Paper, 2 for Scissors, or Q to quit:")

# Print the output
print 'Number of games played: {}'.format(game_stats['games'])
print 'Number of game won {}'.format(game_stats['wins'])
