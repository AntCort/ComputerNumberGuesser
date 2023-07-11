import random

# Creates the function
# Range between two numbers is created
def guess_number():
    low = 0
    high = 100
    print(f'Hello, please think of a number between {low} and {high}.')

    # First guess by the computer
    guesses = 1
    random_number = random.randint(low, high)
    print('My first guess is ' + str(random_number) + ". Am I too low, too high, or am I correct?")
    answer = input('''If too low, type 'low'. If too high, type 'high'. If correct, type 'correct.\n ''').lower()
    
    # While the answer isn't 'correct', the computer will
    # continue to guess
    while (answer.lower() != 'correct'):
        
        # If the answer is too low, the 'low' variable will be updated
        if (answer == "low"):
            print("I will guess again.")
            low = random_number + 1
            random_number = random.randint(low, high)
            print('Is ' + str(random_number) + " the number you guessed?")
            answer = input('''If too low, type 'low'. If too high, type 'high'. If correct, type 'correct.\n ''').lower()
            guesses = guesses + 1
            

        # If the answer is too high, the 'high' variable will be updated
        if (answer == "high"):
            print("I will guess again.")
            high = random_number - 1
            random_number = random.randint(low, high)
            print('Is ' + str(random_number) + " the number you guessed?")
            answer = input('''If too low, type 'low'. If too high, type 'high'. If correct, type 'correct.\n ''').lower()
            guesses = guesses + 1
            


    print(f"I guessed it correctly! Your number is {random_number}")
    print(f"It took me {guesses} guesses to get it right.")

guess_number()