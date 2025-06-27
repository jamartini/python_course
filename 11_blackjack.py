# This is a game of Blackjack, where you must have the closest sum to 21 (if not 21), but if your sum is more than 21
# you lose.

# Isto é um jogo de Blackjack, no qual você precisa ter a soma mais próxima de 21 (se não 21), mas se a sua soma for
# maior que 21 você perde.

from random import randint

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_card1 = cards[randint(0, len(cards) - 1)]
player_card2 = cards[randint(0, len(cards) - 1)]
if player_card1 == 11 and player_card2 == 11:
    player_card1 = 1
player_sum = player_card1 + player_card2
print(f"Player's cards: {player_card1}, {player_card2}; sum: {player_sum}.")

dealer_card1 = cards[randint(0, len(cards) - 1)]
dealer_card2 = cards[randint(0, len(cards) - 1)]
print(f"Dealer's first card: {dealer_card1}")

# The player may choose if they want another card or if they want to jump to the results.

# O jogador pode escolher se quer outra carta ou se quer ir direto aos resultados.

player_choice = input(
    "What will you do? Type 'hit' to take another card, or type 'stand' to end your turn and see the results.\n")
if player_choice == "hit":
    player_card3 = cards[randint(0, len(cards) - 1)]
    if player_card3 == 11 and player_sum > 10:
        player_card3 = 1
    player_sum += player_card3
    print(f"Player's third card: {player_card3}")

print(f"Sum of the player's cards: {player_sum}")
print(f"Dealer's second card: {dealer_card2}")
dealer_sum = dealer_card1 + dealer_card2

if dealer_sum < 17:
    dealer_card3 = cards[randint(0, len(cards) - 1)]
    print(f"Dealer's third card: {dealer_card3}")
    dealer_sum += dealer_card3
print(f"Dealer's sum: {dealer_sum}")

# If both the player and the dealer have the same sum, that's a draw.

# Se ambos jogador e dealer tiverem a mesma soma, é um empate.

if player_sum == 21:
    print("You win!")
elif dealer_sum > 21 > player_sum:
    print("You win!")
elif player_sum > 21:
    print("You lose!")
elif player_sum > dealer_sum:
    print("You win!")
elif player_sum < dealer_sum:
    print("You lose!")
elif player_sum == dealer_sum:
    print("That's a draw.")
