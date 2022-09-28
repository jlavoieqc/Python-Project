import random


def main():
    characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                  "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!","@","#","$","%","^","&","*"]
    password = ""
    while True:
        length = int(input("Enter the length of your password: "))
        if length > 0:
            break
    for i in range(length):
        x = random.randrange(0, len(characters))
        password += characters[x]
    print("Your new password is:", password)


main()
