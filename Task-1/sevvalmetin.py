import random

CARD_VALUES = {
    "A": 11, "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10
}

def deal_card():
    cards = list(CARD_VALUES.keys())
    return random.choice(cards)

def calculate_score(hand):
    score = 0
    count = 0

    for card in hand:
        value = CARD_VALUES[card]
        score += value
        if card == "A":
            count += 1

    while score > 21 and count > 0:
        score -= 10
        count -= 1
    return score

def get_bet(balance):
    while True:
        try:
            bet = int(input(f"Current Balance: {balance}$\nHow much would you like to bet? "))
            if 0 < bet <= balance:
                return bet
            else:
                print(f"Please enter an amount between 1 and {balance}.")
        except ValueError:
            print("Please enter a numeric value.")

def play_game(balance,name):
    print(f"BLACKJACK GAME - Player: {name}")

    bet_amount = get_bet(balance)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    while not is_game_over:
        user_score = calculate_score(user_cards)
        print(f"\n{name} cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 21 and len(user_cards) == 2:
            print(f"Blackjack! {name} got 21.")
            is_game_over = True
        elif user_score > 21:
            print(f"{name} went over 21! Game over.")
            is_game_over = True
        else:
            user_should_deal = input("Type 'h' to hit, type 's' to stand: ").lower()
            if user_should_deal == 'h':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score < 17 and user_score <= 21:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("\n" + "-" * 30)
    print(f"{name} final hand: {user_cards}, Score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, Score: {computer_score}")
    print("-" * 30)

    result = ""
    if user_score > 21:
        result = f"{name} lost! You went over 21"
        balance -= bet_amount
    elif computer_score > 21:
        result = f"{name} won! Computer went over 21"
        balance += bet_amount
    elif user_score > computer_score:
        result = f"{name} won!"
        balance += bet_amount
    elif computer_score > user_score:
        result = f"{name} lost!"
        balance -= bet_amount
    else:
        result = "Draw! Your money is returned"

    print(f"Result: {result}")
    return balance

def game():
    user_name = input("Enter your name: ")
    current_balance = int(input("Enter your balance:"))

    while True:
        if current_balance <= 0:
            print(f"\n{user_name} ran out of money! Game over.")
            break

        current_balance = play_game(current_balance,user_name)
        print(f"\n{user_name} balance after the game: {current_balance}$")

        if input("\nDo you want to play again? (y/n): ").lower() != "y":
            print("Game closed. Thank you!")
            break

game()