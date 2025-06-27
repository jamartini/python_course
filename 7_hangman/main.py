# This is a game of hangman, in which we have 5 chances to guess the word or else we lose. The game uses a while loop
# to keep running while there are still letters to be guessed and chances left. It also displays the hangman, according
# to the number of wrong guesses taken.

# Isto é um jogo da forca, no qual temos 5 chances de acertar a palavra, caso contrário perdemos. O jogo usa um while
# loop pra continuar funcionando enquanto existirem letras a serem adivinhadas e chances restantes. Ele também mostra
# o boneco na forca de acordo com o número de palpites errados.

import hangman_arts
import hangman_words
import random

chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
word_split = [*chosen_word]

display = []
for i in range(word_length):
    display.append("_")

right_guesses = 0
wrong_guesses = 0

print(' '.join(display))
print(hangman_arts.logo)
print(hangman_arts.stages[0])

# The loop will end when all chances have been taken or if the word was guessed right.

# O loop vai se encerrar quando todas as chances forem gastas ou se a palavra tiver sido adivinhada.

while right_guesses < word_length and wrong_guesses < 6:
    guess = input("Guess a letter: ").lower()
    if guess == chosen_word:
        right_guesses = word_length
    elif word_split.count(guess) and not display.count(guess):
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
                right_guesses += 1
        print(' '.join(display))
    elif display.count(guess):
        print('You already guessed this letter, try again!')
    else:
        wrong_guesses += 1
        print(hangman_arts.stages[wrong_guesses])
        if (6 - wrong_guesses) > 0:
            print(f"You guessed wrong, try again! ({6 - wrong_guesses} guesses left).")
        else:
            print("0 guesses left. You lost.")
            print(f"The word was {chosen_word}")
if right_guesses >= word_length:
    print("You won!")
