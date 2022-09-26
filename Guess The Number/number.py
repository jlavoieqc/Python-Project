import random

def main():
    print("This program generates a random number between 1 and 100.")
    print("If you guess the number, you will win the game.")
    print()

    # Set the initial values.
    the_number = random.randint(1, 100)
    guess = int(input("Take a guess: "))
    tries = 1

    # Guessing loop.
    while guess != the_number:
        if guess > the_number:
            print("Lower...")
        else:
            print("Higher...")

        guess = int(input("Take a guess: "))
        tries += 1

    print("You guessed it!  The number was", the_number)
    print("And it only took you", tries, "tries!\n")

    # see if the user wants to play again.
    answer = input("Would you like to play again? (y/n): ")

    while answer.lower() != "n" and answer.lower() != "y":
        answer = input("Would you like to play again? (y/n): ")

    if answer.lower() == "y":
        main()
    else:
        print("\nThanks for playing.  See you later.")


# Call the main function.
main()