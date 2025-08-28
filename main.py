import random
import sys

def playGame():
    print("you have 10 tries to guess a number between 1 and 1000")
    number = random.randint(1, 1000)
    tries = 0
    while tries < 10:
        tries += 1
        tmp = int(input(f"This is guess number {tries}: "))
        if tmp < number:
            print("Too small!")
        if tmp > number:
            print("Too big!")
        if tmp == number:
            print("congratulations! You guessed the right number!")
            playAgain = input("Would you like to play again? (Y/N): ")
            if playAgain == 'Y':
                playGame()
            else:
                print("Program ending...")
                sys.exit(0)
    restart = input("That was your last try. Do you want to restart? (Y/N): ")
    if restart == 'Y':
        playGame()
    else:
        print("Program ending...")
        sys.exit(0)

playGame()