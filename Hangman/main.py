import random
from urllib.request import urlopen
import urllib.request

def main():
    #create a list of words
    word_url = "https://raw.githubusercontent.com/jlavoieqc/Python-Project/main/Hangman/word.txt"
    response = urllib.request.urlopen(word_url)
    long_txt = response.read().decode()
    word_list = long_txt.splitlines()

    #randomly select a word from the list
    word = random.choice(word_list)

    #create a variable to track the number of guesses
    num_guesses = 0

    #create a list to store the letters that have been guessed
    letters_guessed = []

    #create a variable to track if the game is over
    game_over = False

    #create a variable to track if the player has won
    player_won = False

    #print out the instructions for the game
    print('Welcome to Hangman!')
    print('The goal is to guess the word within 6 tries.')

    #blocking maj or 2 letters
    blocked_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','BB','CC','DD','EE','FF','GG','HH','II','JJ','KK','LL','MM','NN','OO','PP','QQ','RR','SS','TT','UU','VV','WW','XX','YY','ZZ','AAA','BBB','CCC','DDD','EEE','FFF','GGG','HHH','III','JJJ',"1","2","3","4","5","6","7","8","9","0",'!','@','#','$','%','^','&','*','(',')','_','+','=','{','}','[',']','|',';',':','"',"'",'<','>','?','/',',','.','~','`','\\',' ','']

    #while the game is not over, keep playing
    while not game_over:

        #display the current status of the game
        display_hangman(num_guesses)
        print('')
        print('Letters guessed:', letters_guessed)

        #get the player's guess
        guess = input('Guess a letter: ')

        #blocking maj or 2 letters
        if guess in blocked_letters:
            print('Cannot use this letter')
            continue

        #if the player has already guessed that letter, tell them and don't do anything else
        if guess in letters_guessed:
            print('You already guessed that letter!')
            continue

        #if the player guessed a letter in the word, update the list of letters guessed and the list of letters in the word
        if guess in word:
            print('That letter is in the word!')
            letters_guessed.append(guess)

            #create a new variable that is True when all of the letters in the word have been guessed
            all_letters_guessed = True

            #go through each letter in the word and check if it has been guessed
            for letter in word:
                if letter not in letters_guessed:
                    all_letters_guessed = False

            #if all of the letters have been guessed, set player_won to True and set game_over to True
            if all_letters_guessed:
                player_won = True
                game_over = True

        #if the player guessed a letter not in the word, add it to the list of letters guessed and increment num_guesses
        else:
            print('That letter is not in the word!')
            letters_guessed.append(guess)
            num_guesses += 1

        #if num_guesses is 6 (the player has used all 6 chances), set game_over to True
        if num_guesses == 6:
            game_over = True

    #if the player won, print out a winning message. otherwise, print out a losing message.
    if player_won:
        print('Congratulations! You won!')
    else:
        print('Sorry, you lost. The word was', word)

    #ask if the player wants to play again and if they do, call main() again. otherwise, end the program. 
    play_again = input('Do you want to play again? (y/n) ')

    if play_again == 'y':
        main()

    else: 
        print('Thanks for playing!')

#display the current status of the game, including the number of chances the player has left and the letters that have been guessed
def display_hangman(num_guesses):
    if num_guesses == 0:
        print('''
            
            
            
            
            
            
        ''')
    elif num_guesses == 1:
        print('''
            
            
            
            
            
        +---+
        |   |
              |
              |
              |
              |
        =========''')
    elif num_guesses == 2:
        print('''
            
            
            
            
            
        +---+
        |   |
        O   |
              |
              |
              |
        =========''')
    elif num_guesses == 3:
        print('''
            
            
            
            
            
        +---+
        |   |
        O   |
        |   |
              |
              |
        =========''')

    elif num_guesses == 4: 
        print(''' 





                 +---+ 

                 |   | 

                 O   | 

                /|   | 

                     | 

                     | 

                 =========''') 

    elif num_guesses == 5: 

        print(''' 

                 +---+ 

                 |   | 

                 O   | 

                /|\  | 

                /    | 

                     | 

                 =========''') 

    else: 

        print(''' 

                 +---+ 

                 |   | 

                 O   | 

                /|\  | 

                / \  | 

                     | 

                 =========''') 


#run the program
main()