import random

rock = 1
paper = 2
scissors = 3

user_score = 0
computer_score = 0

while True:
    user_choice = int(input("Enter your choice (1 - Rock, 2 - Paper, 3 - Scissors): "))
    computer_choice = random.randint(1, 3)
    
    if user_choice == rock and computer_choice == scissors:
        print("You win! Rock beats scissors.")
        user_score += 1
    elif user_choice == paper and computer_choice == rock:
        print("You win! Paper beats rock.")
        user_score += 1
    elif user_choice == scissors and computer_choice == paper:
        print("You win! Scissors beat paper.")
        user_score += 1
    elif user_choice == computer_choice:
        print("It's a tie!")
    else:
        print("You lose! Try again.")
        computer_score += 1
    
    print("User Score:", user_score)
    print("Computer Score:", computer_score)
    
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break
