import random
import sys

tries = 0

def INPUT():
    tmp = input(f"This is attempt number {tries}: ")
    if tmp.isdigit():
        return int(tmp)
    else:
        print("Please enter a number")
        return INPUT()

def playGame():
    print("you have 10 tries to guess a number between 1 and 1000")
    number = random.randint(1, 1000)
    global tries
    tries = 0
    while tries < 10:
        tries += 1
        tmp = INPUT()
        if tmp < number:
            print("Too small!")
        elif tmp > number:
            print("Too big!")
        else:
            print("congratulations! You guessed the right number!")
            playAgain = input("Would you like to play again? (Y/N): ").strip().lower()
            if playAgain == 'y':
                playGame()
            else:
                print("Program ending...")
                sys.exit(0)
    restart = input("That was your last try. Do you want to restart? (Y/N): ").strip().lower()
    if restart == 'y':
        playGame()
    else:
        print("Program ending...")
        sys.exit(0)

playGame()