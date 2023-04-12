import random

def play_game(user_choice):
    computer_choice = random.choice(["snake", "water", "gun"])

    if user_choice == computer_choice:
        return "It's a tie!"

    if user_choice == "snake":
        if computer_choice == "water":
            return "You win! Snake drinks water."
        else:
            return "You lose! Gun kills snake."

    if user_choice == "water":
        if computer_choice == "gun":
            return "You win! Gun gets wet."
        else:
            return "You lose! Snake drinks water."

    if user_choice == "gun":
        if computer_choice == "snake":
            return "You win! Gun kills snake."
        else:
            return "You lose! Gun gets wet."

user_choice = input("Enter snake, water, or gun: ")
result = play_game(user_choice)
print(result)


play_again = "y"
while play_again == "y":
    user_choice = input("Enter snake, water, or gun: ")
    result = play_game(user_choice)
    print(result)
    play_again = input("Play again? (y/n): ")


