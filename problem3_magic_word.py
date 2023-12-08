# Create the word to display to the user.
# If the guessed letter is in the word, display the letter. Otherwise, display an underscore
word_to_guess = "APPLE"
max_chances = 10
guessed_letters = []

print("Try to guess the word. It has {} letters.".format(len(word_to_guess)))

chances = 0
while chances < max_chances:
    # Display the word after checking if each letter in the word is in the guessed_letters array. Otherwise _
    # Display the guessed letters after joining them
    guess = input("\nGuess the word: {}\nSo far used letters: {}\nYour guess: "
                  .format(
                      ''.join([letter if letter in guessed_letters else '_' for letter in word_to_guess]),
                      ', '.join(guessed_letters)))

    # Check if the guess is a single character and a letter
    if len(guess) == 1 and guess.isalpha():
        # Check if the guessed letter has been previously guessed
        # If not, add the guess to the guessed_letters array
        if guess.upper() in guessed_letters:
            print("Letter already guessed. Please choose another")
        else:
            guessed_letters.append(guess.upper())

        # Check if all the letters have been guessed by matching all unique characters in guessed_letters with word_to_guess
        if set(guessed_letters) == set(word_to_guess):
            print("Congratulations! You guessed the word '{}' correctly in {} tries."
                  .format(word_to_guess, chances + 1))
            break

        chances += 1
    else:
        print("Invalid input. Please enter a single letter.")

else:
    # When the user runs out of guesses
    print("Sorry, you have lost. The correct word was '{}'.".format(word_to_guess))
