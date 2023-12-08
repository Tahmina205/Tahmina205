import random

# here we create the word to display to the user. 
# If the guessed letter is in the word, we display the letter. Otherwise we display an underscore
def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def main():
    word_to_guess = "APPLE"
    max_chances = 10
    guessed_letters = []

    print("Try to guess the word. It has {} letters.".format(len(word_to_guess)))
    
    chances = 0
    while chances < max_chances:
        # here we display the word after passing the word and guessed letters to display_word defined above
        # we also display the guessed letters after joining them
        guess = input("\nGuess the word: {}\nSo far used letters: {}\nYour guess: "
                      .format(display_word(word_to_guess, guessed_letters), ', '.join(guessed_letters)))

        # here we check if the guess is a single character and a letter
        if len(guess) == 1 and guess.isalpha():
            # we first check if the guessed letter has been previously guessed
            # If not, we add the guess to the guessed_letters array
            if(guess.upper() in guessed_letters):
                print("Letter already guessed. Please choose another")
            else:
                guessed_letters.append(guess.upper())

            # here we check if all the letters have been guessed by matching all unique characters in guessed_letters with word_to_guess
            if set(guessed_letters) == set(word_to_guess):
                print("Congratulations! You guessed the word '{}' correctly in {} tries."
                      .format(word_to_guess, chances + 1))
                break

            chances += 1
        else:
            print("Invalid input. Please enter a single letter.")

    else:
        # when user runs out of guesses
        print("Sorry, you have lost. The correct word was '{}'.".format(word_to_guess))

if __name__ == "__main__":
    main()
