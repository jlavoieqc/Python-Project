import random

def lotto_generator():
    """
    Generates a random lotto number
    """
    lotto_number = []
    for i in range(6):
        lotto_number.append(random.randint(1, 45))

    return lotto_number


def main():
    """
    Runs the program
    """
    print(lotto_generator())


if __name__ == '__main__':
    main()