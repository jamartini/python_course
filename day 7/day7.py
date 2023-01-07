import hangman_arts
import hangman_words
import random


chosen_word = random.choice(hangman_words.word_list)
word_length = len(chosen_word)
word_splitted = [*chosen_word]

display = []
for i in range(word_length):
    display.append("_")

right_guesses = 0
wrong_guesses = 0

print(' '.join(display))
print(hangman_arts.logo)
print(hangman_arts.stages[0])

while right_guesses < word_length and wrong_guesses < 6:
  guess = input("Guess a letter: ").lower()
  if word_splitted.count(guess) and not display.count(guess):
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
if right_guesses >= word_length:
  print("You won!")