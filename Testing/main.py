import random
import urllib.request

def main():
   #here is the list of books that will be generated
   books_url = "https://raw.githubusercontent.com/jlavoieqc/Python-Project/main/Test%20Files%20Data/testing.txt"

   #random book
   book = random.choice(books_url)

   #print the book
   print(book)

    #ask if the player wants to play again and if they do, call main() again. otherwise, end the program. 
    play_again = input('Do you want to generate an other book? (y/n) ')

    if play_again == 'y':
        main()
main()