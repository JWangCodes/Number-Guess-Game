import random

# generates a random number from 1-100 that the user must guess
def number_generator():
    number = random.randint(1 , 100)
    return number

print("")
print("Welcome to the number guessing game!")
print("You are giving 5 tries to guess the computer's number from 1 to 100")
print("")

def start_game():
    answer = number_generator()
    for i in range(5):
        guess = int(input("Enter a number: "))
        if guess != answer:
            if guess > answer:
                if i == 4:
                    print("")
                    print("You lost")
                    print("The number was " + str(answer))
                else:
                    print("Try again")
                    print("The number is lower")
                    print("")
            else:
                
                if i == 4:
                    print("")
                    print("You lost")
                    print("The number was " + str(answer))
                else:
                    print("Try again")
                    print("The number is higher")
                    print("")
        else:
            print("")
            print("That's correct")
            print("You guessed the right number")
            break

while True:
    start_game()
    option = str(input("Want to play again? (Yes/No) ")).lower()
    if option == "yes":
        print("")
        continue
    else:
        break