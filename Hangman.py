import random

words = ["python", "computer", "programming", "developer", "keyboard"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

while wrong_guesses < max_attempts:

    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)
    print("Wrong guesses:", wrong_guesses)
    print("Attempts left:", max_attempts - wrong_guesses)

    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You won!")
        break

    guess = input("\nGuess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter!")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct guess!")
    else:
        print("Wrong guess!")
        wrong_guesses += 1

else:
    print("\nGame Over!")
    print("The correct word was:", word)

print("\nThanks for playing!")