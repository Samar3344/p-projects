import random

def hangman():
    """
    Plays a game of hangman.
    """

    words = ['python', 'hangman', 'programming', 'computer', 'science']
    word = random.choice(words)
    word_length = len(word)

    guessed_letters = []
    tries = 6

    print("Welcome to Hangman!")
    print("The word has", word_length, "letters.")

    while tries > 0:
        guess = input("Guess a letter: ")

        if len(guess) != 1 or not guess.isalpha() :
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters+=(guess)

        if guess in word:
            print("Correct!")
        else:
            tries -= 1
            print("Incorrect. You have", tries, "tries left.")

        word_display = ""
        for letter in word:
            if letter in guessed_letters:
                word_display += letter
            else:
                word_display += "_"
        print(word_display)

        if word_display == word:
            print("Congratulations, you win!")
            break

    if tries == 0:
        print("You lose. The word was", word)

if __name__ == "__main__":
    hangman()
     