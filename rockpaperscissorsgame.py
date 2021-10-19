import random

print(f"Enter choice: 1 - Rock, 2 - Paper, 3 - Scissor")
choice = int(input(f"Enter your choice: "))
computer_choice = random.randint(1, 3)
print(f"Computer: {computer_choice}")

if choice == computer_choice:
    print("Draw")
elif choice == 1:  # Rock
    if computer_choice == 2:  # Paper
        print("you lose. Paper beats rock")
    else:
        print("You win. Rock beats Scissors")
elif choice == 2:  # Paper
    if computer_choice == 1:  # Rock
        print("You win. Paper beats rock")
    else:
        print("You lose.")
elif choice == 3:  # Scissors
    if computer_choice == 1:  # Rocgitk
        print("You lose. Rock beats Scissors")
    else:
        print("You win.")
else:
    print("Choose a number between 1, 2 or 3")
