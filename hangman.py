# Import the random module, which is used to generate a random word from the list of words
import random

# Define the list of words, which contains 34 words related to computer science and programming
words = [
    'python', 'javascript', 'kotlin', 'ruby', 'swift', 'algorithm',
    'compiler', 'database', 'encryption', 'firewall', 'hardware',
    'internet', 'java', 'kernel', 'malware', 'network', 'object',
    'protocol', 'query', 'router', 'security', 'token', 'url',
    'virtual', 'wireless', 'xml', 'yaml', 'zip', 'abstract', 'binary',
    'cache', 'developer', 'ethernet', 'framework', 'gateway', 'hexadecimal',
    'iteration', 'juxtapose', 'keystroke', 'lambda', 'metadata', 'node'
]

# Define the Hangman stages, which are used to display the current state of the game
hangman_stages = [
    """
   +---+
   O   |
  /|\\  |
  / \\  |
      ===""", '''
   +---+
   O   |
  /|\\  |
  /    |
      ===''', '''
   +---+
   O   |
  /|\\  |
       |
      ===''', '''
   +---+
   O   |
  /|   |
       |
      ===''', '''
   +---+
   O   |
   |   |
       |
      ===''', '''
   +---+
   O   |
       |
       |
      ===''', '''
   +---+
       |
       |
       |
      ===''',]

# Choose a random word from the list of words
chosen_word = random.choice(words)
print(chosen_word)

# Initialize the word display with underscores for each letter in the chosen word
word_display = ["_" for _ in chosen_word]
print(word_display)

# Set the number of attempts to 6
attempts = 6

# Print a welcome message to the user
print("...Welcome to Hangman...")

# Define a function to display the current state of the game
def display_state():
    # Print the number of attempts remaining
    print(f"attempts = {attempts}")
    # Print the current Hangman stage
    print(hangman_stages[attempts])
    # Print the current word display
    print(" ".join(word_display))

# Define a function to display the final word
def display_word():
    # Print the final word display
    print(" ".join(word_display))

# Start the game loop
while attempts > 0 and " " in word_display:
    # Display the current state of the game
    display_state()
    # Ask the user to guess a letter
    guess = input("Guess a letter---> ").lower()
    # Check if the guessed letter is in the chosen word
    if guess in chosen_word:
        # Iterate over the word and update the word display
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                if word_display[index] == "_":
                    word_display[index] = guess
    else:
        # Decrement the number of attempts if the guess is incorrect
        print("Incorrect, Try again")
        attempts -= 1

    # Check if the user has won the game
    if "_" not in word_display:
        # Display the final word and congratulate the user
        display_word()
        print("You win!")
        break

# Check if the user has lost the game
if attempts == 0:
    # Display the final state of the game and reveal the correct answer
    display_state()
    print("Sorry, you lost, the word was--->", chosen_word)

# Display the final word
display_word()