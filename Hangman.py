# Importing random so I can generate choose random things from a list.
# Globally declaring variables I will need later.
import random
check = 1
guesses = 1

def menu():
    old_guesses = []
    loop = 1
    print('__________***---^---***---^---***__________')
    while loop == 1:
        difficulty = input("Welcome to Hangman!\nWhat difficulty do you want to play?\nEasy (3-4 letter words)\nMedium (4-6 letter words)\nHard (5-7 letter words)\nInsane (7+ letter words)\nChoose (Easy/Medium/Hard/Insane): ").lower()
        word = difficulty_selection(difficulty)
        if word == 'baddie':
            continue
        else:
            loop = 0
    lives = life_setting(difficulty)
    while lives != 0:
        print("\n\n", (display(word, old_guesses)))
        print("\nYou have", lives, "lives left.")

        print("These are the words you have already guessed:", old_guesses)
        guess = input("Guess a letter: ").lower()
        check = input_check(guess, old_guesses)
        if check == 0:
            continue
        guesses = former_guesses(guess, word, lives, old_guesses)
        if guesses == 0:
            break

    if lives == 0:
        print("Sorry, you lost. The word was:", word)
def display(correct_word, already_guessed):
    answer = ""
    for char in correct_word:
        if char in already_guessed:
            answer += char
        else:
            answer += "_"
    return answer




WORDS_EASY = ("see", "fur", "oak", "cow", "hex", "ask", "hay", "fox", "hip", "eye", "raw", "lip", "god", "nut", "hot", "rest", "jail", "nail", "myth", "beer", "kill", "name", "edge", "drop", "home", "lamp", "maid", "desk", "leaf", "fear")
WORDS_MEDIUM = ("stun", "firm", "gold", "will", "hour", "lake", "phew", "sure", "thor", "ouch", "ouija", "azure", "rural", "blank", "right", "leash", "dress", "medal", "woman", "cable", "bother", "polish", "social", "spirit", "kidnap", "kettle", "sailor", "scheme", "column", "string")
WORDS_HARD = ("bullet", "layout", "coffee", "insure", "resign", "embryo", "middle", "virgin", "powder", "aspect", "equinox", "breathe", "diamond", "trouble", "popular", "harvest", "extract", "outline", "bracket", "century", "jelly", "staff", "blame", "proud", "chain", "tease", "arrow", "sense", "swell", "pupil")
WORDS_INSANE = ("uniform", "justice", "subject", "country", "context", "omission", "position", "nonsense", "creation", "merchant", "vertical", "mosquito", "suitcase", "retailer", "abortion", "condition", "exclusive", "permanent", "fabricate", "unanimous", "establish", "invisible", "perforate", "sacrifice", "landscape", "prosecute", "undermine", "sentiment", "orchestra", "transform")

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



def input_check(guess, old_guesses):
    if len(guess) != 1 or not guess.isalpha():  # .isalpha checks if the variable before the period is in the english alphabet.
        print("That guess in not correct, please try to input a single letter.")
        return 0
    elif guess in old_guesses:
        print("You have already guessed that letter.")
        return 0

def former_guesses(guess, hangman, lives, old_guesses):
    old_guesses.append(guess)
    if guess not in hangman:
        lives -= 1
        print("You have", lives, "lives left.")
    else:
        print("That letter is in the word")
    word_display = display(hangman, old_guesses)
    if "_" not in word_display:
        print("\n\nCongratulations! You guessed the word:", hangman)
        return 0

menu()
    # FUNCTIONS
    # MORE ANNOTATIONS
    # MAKE PRETTY
    # VIDEO IS FOR SHOWING THE CODE WORKS
    #Main function
    #Menu function