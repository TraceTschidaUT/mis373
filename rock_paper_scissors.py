# import the random module
from random import randint

def computer_brain(user_stats):
    """Determines the optimal choice to beat the human in Rock Paper Scissors
    Returns: int
    Keyword Arguments:
    user_stats -- a dictionary containing the human's number of choices for rock, paper, and scissors
    """

    max_val = max(user_stats, key=user_stats.get)
    max_vals = [x for x, v in user_stats.items() if v == user_stats[max_val]]

    if len(max_vals) > 1:
        decision = randint(0, len(max_vals) -1)
    else:
        decision = 0
    
    choice = max_vals[decision]

    if choice == 'rock':
        return 1 
    elif choice == 'paper':
        return 2
    elif choice == 'scissors':
        return 0

def PlayRPS():
    """Starts and plays a game of Rock, Paper Scissors to challenge a human against a bot
    Returns:
    Keyword Arguments:
    """

    print("Hello and welcome to Rock Paper Scissors.")
    user_input = str(raw_input("Enter 0 for Rock, 1 for Paper, 2 for Scissors, or Q to quit: "))
    print ''

    user_stats = {'rock': 0, 'paper': 0, 'scissors': 0 }
    game_stats = {'wins': 0, 'games': 0}
    options = ['Rock', 'Paper', 'Scissors']

    # loop through until the user enters 'Q'
    while user_input != 'Q' and user_input != 'q':

        try:
            if user_input not in ['0','1', '2']:
                raise Exception('You must enter 0, 1, 2 or Q')
        
            # Convert the user's input to an int
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
            print ''
            user_input = raw_input("Enter 0 for Rock, 1 for Paper, 2 for Scissors, or Q to quit: ")

    # Print the output
    print 'Number of games played: {}'.format(game_stats['games'])
    print 'Number of game won {}'.format(game_stats['wins'])

PlayRPS()
