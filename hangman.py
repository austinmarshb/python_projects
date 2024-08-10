import random
import hangman_art
import hangman_words

lives = 6

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
# print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for characters in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
incorrect_letters = []

while not game_over:

    print(f"****************************{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}!")

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        if guess in incorrect_letters:
            print(f"You've already guessed {guess}!")
        else:
            incorrect_letters.append(guess)
            lives -= 1
            print(f"Sorry, {guess} is not in the word!")
            print(hangman_art.stages[lives])

        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************")
            print(f"The word was {chosen_word}!")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
