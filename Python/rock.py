import random

choice_dict = {'r': '🪨', 'p': '📃', 's': '✂️'}
choices = ['r', 'p', 's']

while True:
    user_choice = input("Enter Rock, Paper or Scissors (r/p/s): ").lower()

    if user_choice not in choices:
        print("Invalid Choice. Please try again.")
        continue

    print("Your option is: " + choice_dict[user_choice])

    comp_choice = random.choice(choices)
    print("Computer's choice is: " + choice_dict[comp_choice])

    if (user_choice == "r" and comp_choice == "p") or (user_choice == "s" and comp_choice == "r") or (user_choice == "p" and comp_choice == "s"):
        print("Sorry, Computer Won It")
    elif (user_choice == "p" and comp_choice == "r") or (user_choice == "r" and comp_choice == "s") or (user_choice == "s" and comp_choice == "p"):
        print("Yes, You Have Won..")
    else:
        print("It's a draw..")

    while True:
        take = input("Do you want to play again? (y/n): ").lower()

        if take == "n":
            print("Thanks for playing....")
            break
        elif take == "y":
            break
        else:
            print("Invalid input. Please enter 'y' to play again or 'n' to quit.")

    if take == "n":
        break
