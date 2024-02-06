import random  # Import the random module to generate random numbers
from art import welcome_message  # Import the welcome_message from the art module

def game():  # Define a function named game
    computer_number = random.randint(0, 100)  # Generate a random number between 0 and 100
    valid_difficulties = ['easy', 'hard']  # Define a list of valid difficulty levels

    diff = ""  # Initialize the variable diff
    while diff not in valid_difficulties:  # Continue loop until valid difficulty is chosen
        diff = input("Choose difficulty 'easy' or 'hard': ").lower()  # Prompt user for difficulty choice

        if diff not in valid_difficulties:  # If input is not valid, Print error message
            print("Invalid input. Please choose 'easy' or 'hard'.")   

    print(f"I am thinking of a number between 0 and 100.")  # Print message indicating the range of guess
    attempts = 0  # Initialize variable to store number of attempts

    if diff == "easy":  # If difficulty is easy Set attempts to 10.
        attempts = 10   
    elif diff == "hard":  # If difficulty is hard Set attempts to 5.
        attempts = 5     

    print(f"You have {attempts} attempts to guess the number.")  # Print number of attempts available
    
    end_of_game = False  # Initialize variable to control game loop

    while not end_of_game:  # Start the game loop
        guess = int(input("Guess the number: "))  # Prompt user to input their guess and convert to integer
        attempts -= 1  # Decrement the number of attempts remaining

        if guess == computer_number:  # If the guess is correct
            print(f"{guess} is the correct answer.")  # Print a message indicating the correct guess
            end_of_game = True  # Set end_of_game flag to True to end the game

        elif guess < computer_number:  # If the guess is too low
            print(f"{guess} is too low. You have {attempts} attempts left.")  # Print a message indicating the guess is too low
        else:  # If the guess is too high
            print(f"{guess} is too high. You have {attempts} attempts left.")  # Print a message indicating the guess is too high

        if attempts == 0:  # If there are no attempts left
            end_of_game = True  # Set end_of_game flag to True to end the game
        elif not end_of_game:  # If the game is not over yet
            print("Guess again!")  # Prompt the user to guess again

    play_again = input("Do you want to play again? (yes/no): ").lower()  # Ask user if they want to play again
    if play_again == "yes":  # If user wants to play again
        game()  # Call the game function recursively to start a new game

# Start the game
print(welcome_message)  # Print the welcome message
game()  # Call the game function to start the game
