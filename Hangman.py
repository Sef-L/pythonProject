# Importing random so I can generate choose random things from a list.
import random

# Function called 'display_word'.
def display(correct_word, already_guessed):
    # Create a variable (answer)
    answer = ""
    # for every 'char' in the variable 'correct_word'.
    # if 'char' is in the list 'already_guessed' then print 'char' else print a blank.
    # return the answer
    for char in correct_word:
        if char in already_guessed:
            answer += char
        else:
            answer += "_"
    return answer
# Create a list called 'old_guesses'
old_guesses = []

# Allow the user to choose a difficulty and what ever their answer is put into lowercase
difficulty = input("Welcome to Hangman!\nWhat difficulty do you want to play?\nEasy (3-4 letter words)\nMedium (4-6 letter words)\nHard (5-7 letter words)\nInsane (7+ letter words)\nChoose Easy/Medium/Hard/Insane: ").lower()

# The possible letters based on the difficulty
WORDS_EASY = ("see", "fur", "oak", "cow", "hex", "ask", "hay", "fox", "hip", "eye", "raw", "lip", "god", "nut", "hot", "rest", "jail", "nail", "myth", "beer", "kill", "name", "edge", "drop", "home", "lamp", "maid", "desk", "leaf", "fear")
WORDS_MEDIUM = ("stun", "firm", "gold", "will", "hour", "lake", "phew", "sure", "thor", "ouch", "ouija", "azure", "rural", "blank", "right", "leash", "dress", "medal", "woman", "cable", "bother", "polish", "social", "spirit", "kidnap", "kettle", "sailor", "scheme", "column", "string")
WORDS_HARD = ("bullet", "layout", "coffee", "insure", "resign", "embryo", "middle", "virgin", "powder", "aspect", "equinox", "breathe", "diamond", "trouble", "popular", "harvest", "extract", "outline", "bracket", "century", "jelly", "staff", "blame", "proud", "chain", "tease", "arrow", "sense", "swell", "pupil")
WORDS_INSANE = ("uniform", "justice", "subject", "country", "context", "omission", "position", "nonsense", "creation", "merchant", "vertical", "mosquito", "suitcase", "retailer", "abortion", "condition", "exclusive", "permanent", "fabricate", "unanimous", "establish", "invisible", "perforate", "sacrifice", "landscape", "prosecute", "undermine", "sentiment", "orchestra", "transform")

# Depending on the difficulty previously randomly choose a word from the corresponding list and set up their live count.
def difficulty_selection(difficulty):
    if difficulty == "easy":
        print("You have chosen easy mode.")
        word = random.choice(WORDS_EASY)
    elif difficulty == "medium":
        print("You have chosen medium mode.")
        word = random.choice(WORDS_MEDIUM)
    elif difficulty == "hard":
        print("You have chosen hard mode.")
        word = random.choice(WORDS_HARD)
    elif difficulty == "insane":
        print("You have chosen insane mode.")
        word = random.choice(WORDS_INSANE)
    else:
        print("That is not a valid difficulty.")
        word = "baddie"
    return word

hangman = difficulty_selection(difficulty)

def life_setting(difficulty):
    if difficulty == "easy":
        life_count = 10
    elif difficulty == "medium":
        life_count = 8
    elif difficulty == "hard":
        life_count = 7
    elif difficulty == "insane":
        life_count = 5
    return life_count

lives = life_setting(difficulty)

# While lives are not 0 use the display_word word function.
# With the randomly selected word and the 'old_guesses' list.
# Display the amount of lives remaining.
while lives != 0:
    print("\n\n", (display(hangman, old_guesses)))
    print("\nYou have", lives, "lives left.")

    # Display the list of letters already guessed.
    # Have the user input a guess and make it lowercase.
    print("These are the words you have already guessed:", old_guesses)
    guess = input("Guess a letter: ").lower()

    # Check if that guess is 1 letter long, is in the english alphabet and isn't in the 'old_guesses' list.
    # if not restart the loop and tell them what they did wrong.
    if len(guess) != 1 or not guess.isalpha():  # .isalpha checks if the variable before the period is in the english alphabet.
        print("That guess in not correct, please try to input a single letter.")
        continue
    elif guess in old_guesses:
        print("You have already guessed that letter.")
        continue

    old_guesses.append(guess)
    if guess not in hangman:
        lives -= 1
        print("You have", lives, "lives left.")
    else:
        print("That letter is in the word")
    word_display = display(hangman, old_guesses)
    if "_" not in word_display:
        print("\n\nCongratulations! You guessed the word:", hangman)
        break
if lives == 0:
    print("Sorry, you lost. The word was:", hangman)


    # FUNCTIONS
    # MORE ANNOTATIONS
    # MAKE PRETTY
    # VIDEO IS FOR SHOWING THE CODE WORKS