import random
import urllib.request

def main():
    #here is the list of books that will be generated
    books_url = "https://raw.githubusercontent.com/jlavoieqc/Python-Project/main/Test%20Files%20Data/testing.txt"
    response = urllib.request.urlopen(books_url)
    long_txt = response.read().decode()
    books_list = long_txt.splitlines()
    #random book
    book = random.choice(books_list)

    #print the book
    print(book)

    #ask if the player wants to play again and if they do, call main() again. otherwise, end the program. 
    play_again = input('Do you want to generate an other book? (y/n) ')

    if play_again == 'y':
        main()
main()