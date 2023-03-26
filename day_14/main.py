import art
import game_data
import random

print(art.logo)


def get_a_index():
    a_index = random.randint(0, len(game_data.data) - 1)
    return a_index


index_a = get_a_index()


def get_b_index():
    b_index = random.randint(0, len(game_data.data) - 1)
    return b_index


index_b = get_b_index()
while index_a == index_b:
    index_b = get_b_index()


def game(a, b):
    print(
        f"Compare A: {game_data.data[a]['name']}, a {game_data.data[a]['description']}, "
        f"from {game_data.data[a]['country']}.")
    print(art.vs)
    print(
        f"Against B: {game_data.data[b]['name']}, a {game_data.data[b]['description']}, "
        f"from {game_data.data[b]['country']}.")


def answer_verifier(a, b, answer):
    if answer == "A":
        if game_data.data[a]['follower_count'] > game_data.data[b]['follower_count']:
            return True
        else:
            return False
    elif answer == "B":
        if game_data.data[b]['follower_count'] > game_data.data[a]['follower_count']:
            return True
        else:
            return False


game(index_a, index_b)
answer_input = input("Who has more followers? Type 'A' or 'B': ").upper()
is_correct = answer_verifier(index_a, index_b, answer_input)
score = 0

while is_correct:
    score += 1
    index_a = index_b
    index_b = get_b_index()
    while index_a == index_b:
        index_b = get_b_index()
    print(art.logo)
    print(f"You're right! Current score: {score}")
    game(index_a, index_b)
    answer_input = input("Who has more followers? Type 'A' or 'B': ").upper()
    is_correct = answer_verifier(index_a, index_b, answer_input)

print(art.logo)
print(f"Sorry, that's wrong. Final score: {score}")
