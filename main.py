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
    START = int(input("The range of random number start from: "))
    END = int((input("To: ")))
    attempts = int(input("How many tries do you want? (10 or less is recommended): "))
    print(f"you have {attempts} tries to guess a number between {START} and {END}")
    number = random.randint(START, END)
    global tries
    tries = 0
    while tries < attempts:
        tries += 1
        tmp = INPUT()
        if tmp < number:
            print("Too small!")
        elif tmp > number:
            print("Too big!")
        else:
            print("congratulations! You guessed the right number!")
            playAgain = input("Would you like to play again? (Y/N): ").strip().lower()
            if playAgain != 'y':
                print("Program ending...")
                sys.exit(0)

    restart = input(f"The number was {number}. Would you like to play again? (Y/N): ").strip().lower()
    if restart != 'y':
        print("Program ending...")
        sys.exit(0)

while True:
    print("You MUST enter a integer for all inputs.")
    playGame()
