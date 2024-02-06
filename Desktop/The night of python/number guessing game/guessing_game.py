import random 
from art import welcome_message

def game():
    computer_number = random.randint(0, 100)
    valid_difficulties = ['easy', 'hard']

    diff = ""
    while diff not in valid_difficulties:
        diff = input("Choose difficulty 'easy' or 'hard': ").lower()

        if diff not in valid_difficulties:
            print("Invalid input. Please choose 'easy' or 'hard'.")

    print(f"I am thinking of a number between 0 and 100.")
    attempts = 0

    if diff == "easy":
        attempts = 10
    elif diff == "hard":
        attempts = 5   

    print(f"You have {attempts} attempts to guess the number.")
    
    end_of_game = False

    while not end_of_game:
        guess = int(input("Guess the number: "))
        attempts -= 1

        if guess == computer_number:
            print(f"{guess} is the correct answer.")
            end_of_game = True

        elif guess < computer_number:
            print(f"{guess} is too low. You have {attempts} attempts left.")
        else:
            print(f"{guess} is too high. You have {attempts} attempts left.")

        if attempts == 0:
            end_of_game = True
        elif not end_of_game:
            print("Guess again!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        game()

# Start the game
print(welcome_message)
game()
