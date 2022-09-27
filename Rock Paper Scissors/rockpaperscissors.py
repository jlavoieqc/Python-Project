import random

def main():
    # Get the computer's play.
    computer = random.randint(1, 3)

    # Get the player's play from the keyboard.
    player = int(input('Enter your play: '))

    # Display what the player and computer plays.
    print('You played', player_name(player))
    print('The computer played', player_name(computer))

    # Determine the winner.
    if player == 1 and computer == 2:
        print('You win!')
    elif player == 1 and computer == 3:
        print('You lose!')
    elif player == 2 and computer == 1:
        print('You lose!')
    elif player == 2 and computer == 3:
        print('You win!')
    elif player == 3 and computer == 1:
        print('You win!')
    elif player == 3 and computer == 2:
        print('You lose!')
    else:
        print('A tie!')

    # Ask if the player wants to play again.
    answer = input('Do you want to play again? ')

    while answer == 'y' or answer == 'Y':

        # Get the computer's play.
        computer = random.randint(1, 3)

        # Get the player's play from the keyboard.
        player = int(input('Enter your play: '))

        # Display what the player and computer plays.
        print('You played', player_name(player))
        print('The computer played', player_name(computer))

        # Determine the winner.
        if player == 1 and computer == 2:
            print('You win!')
        elif player == 1 and computer == 3:
            print('You lose!')
        elif player == 2 and computer == 1:
            print('You lose!')
        elif player == 2 and computer == 3:
            print('You win!')
        elif player == 3 and computer == 1:
            print('You win!')
        elif player == 3 and computer == 2:
            print('You lose!')
        else:
            print('A tie!')

        # Ask if the player wants to play again.
        answer = input('Do you want to play again? ')

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

    

        
# The player_name function converts computer's number to a name using if/elif/else.  Don't forget to return the result.
def player_name(number):
    if number == 1:
        return 'Rock'
    elif number == 2:
        return 'Paper'
    else:
        return 'Scissors'

    
# Call the main function.
main()
