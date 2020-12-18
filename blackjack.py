## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
print("Welcome to Blackjack project\n")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    # 0 will present blackjack in our code
    return sum(cards)


def compare(user_score,cp_score):
    if user_score > 21 and cp_score > 21:
        return "You Lose"

    if user_score == cp_score:
        return "Draw"
    elif cp_score == 0:
        return "Lose, opponent has Blackjack "
    elif user_score == 0:
        return "Win with a Blackjack "
    elif user_score > 21:
        return "You lose"
    elif cp_score > 21:
        return "You win "
    elif user_score > cp_score:
        return "You win "
    else:
        return "You lose "


def play_game():
    user_card = []
    cp_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        cp_card.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_card)
        cp_score = calculate_score(cp_card)
        print(f"Your cards: {user_card}, current score: {sum(user_card)}")
        print(f"Computer's first card: {cp_card[0]}\n")

        if user_score == 0 or cp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while cp_score != 0 and cp_score < 17:
        cp_card.append(deal_card())
        cp_score = calculate_score(cp_card)

    print(f" Your final hand: {user_card}, final score: {user_score}")
    print(f" Computer's final hand: {cp_card}, final score: {cp_score}")
    print(compare(user_score, cp_score))


while input("Do you want to play a game Blsckjack? Type 'y' or 'n': ") == "y":
    play_game()
