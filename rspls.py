# rock, spock, paper, lizard, scissors
# rock = 0
# spock = 1
# paper = 2
# lizard = 3
# scissors = 4

import random

# Welcome and rules

print 'Welcom to Rock-scissors-paper-lizard-Spock game!\nFor rules type "rules".\nTo quit type "q"/"quit".\n'
rspls_rules = '''
\tScissors cut paper
\tPaper covers rock
\tRock crushes lizard
\tLizard poisons Spock
\tSpock smashes scissors
\tScissors decapitate lizard
\tLizard eats paper
\tPaper disproves Spock
\tSpock vaporizes rock
\tRock crushes scissors
    '''  

# The dictionaries for computer picks and valid entries to pick from
comp_entries = {0: 'rock', 1: 'spock', 2: 'paper', 3: 'lizard', 4: 'scissors'}
valid_entries = {'rock': 0, 'spock': 1, 'paper': 2 , 'lizard': 3, 'scissors': 4}

# Main function. Evaluates the data and chooses the winner
def rspls():
    pick = raw_input('Enter your pick:').lower()
    if pick == 'rules':
        print rspls_rules
        return rspls()
    elif pick == 'q' or pick == 'quit':
        return 'Thank you for playing!\n'
    elif pick in valid_entries:
        player_number = valid_entries[pick]
        computer_number = random.randrange(0,5)
        diff = (player_number - computer_number) % 5
        if diff == 1 or diff == 2:
            text = 'You win!'
        elif diff == 3 or diff == 4:
            text = 'Computer wins!'
        else:
            text = 'You and the computer tie!'
        return '\nYou chose ' + pick.upper() + '.' + '\nComputer chose ' + comp_entries[computer_number].upper() + '.' + '\n' + text + '\n'
    else:
        return "Not a valid pick.\n"

def new_game():
    decision = raw_input('Do you want to try again?(y/n):').lower()
    if decision == 'y':
        print rspls()
        new_game()
    elif decision == 'n':
        print 'Thank you for playing!\n'
        return
    else:
        new_game()

print rspls()
new_game()
