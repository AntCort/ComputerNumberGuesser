import random

class NumberGuesser:
    def __init__(self, low, high):
        # Initialize the guesser with a range and a random number within that range
        self.low = low
        self.high = high
        self.guesses = 0
        self.random_number = random.randint(self.low, self.high)

    def make_guess(self):
        # Increase the number of guesses made
        self.guesses += 1
        # Make a guess and ask the user for feedback
        print(f"My guess is {self.random_number}. Am I too low, too high, or am I correct?")
        answer = input("If too low, type 'low'. If too high, type 'high'. If correct, type 'correct': ").lower()

        if answer == "low":
            # If the guess was too low, adjust the lower bound for the next guess
            print("I will guess again.")
            self.low = self.random_number + 1
        elif answer == "high":
            # If the guess was too high, adjust the upper bound for the next guess
            print("I will guess again.")
            self.high = self.random_number - 1
        elif answer == "correct":
            # If the guess was correct, display the result and return True
            print(f"I guessed it correctly! Your number is {self.random_number}")
            print(f"It took me {self.guesses} guesses to get it right.")
            return True

        # Generate a new random number within the adjusted range for the next guess
        self.random_number = random.randint(self.low, self.high)
        return False

def main():
    # Define the range for guessing
    low = 0
    high = 100
    # Create an instance of NumberGuesser
    guesser = NumberGuesser(low, high)

    # Keep making guesses until the correct number is guessed
    while not guesser.make_guess():
        pass

if __name__ == "__main__":
    main()
