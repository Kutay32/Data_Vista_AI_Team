import random


def create_deck():
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    return cards

def draw_card(deck):
    return random.choice(deck)

# PUAN HESAPLAMA
def calculate_score(hand):
    total = 0
    ace_count = 0

    for card in hand:
        if card in ["J", "Q", "K"]:
            total += 10
        elif card == "A":
            total += 11
            ace_count += 1
        else:
            total += int(card)

    # Toplam 21'i geçiyorsa As'ları 11 yerine 1 sayIYORUZ
    while total > 21 and ace_count > 0:
        total -= 10
        ace_count -= 1

    return total

# EL AÇILIYOR
def show_hand(name, hand):
    print(name + "'s hand: " + ' | '.join(hand) + "  -->  Score: " + str(calculate_score(hand)))


def play_game(player_name, balance):
    deck = create_deck()

    print("\n" + "="*15)
    print("  Welcome, " + player_name + "! Balance: $" + str(balance))
    print("="*45)

    # KULLANICIDAN BAHİSİNİ İSTİYORUM
    while True:
        try:
            bet = int(input("Enter your bet (Max: $" + str(balance) + "): "))
            if bet <= 0:
                print("Bet must be greater than 0.")
            elif bet > balance:
                print("Insufficient balance!")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")


    player_hand = [draw_card(deck), draw_card(deck)]
    dealer_hand = [draw_card(deck), draw_card(deck)]

    print("\n--- Cards Dealt ---")
    show_hand(player_name, player_hand)
    show_hand("Dealer", dealer_hand)

    #OYUNCU OYNUYOR BURADA
    while True:
        player_score = calculate_score(player_hand)

        if player_score == 21:
            print("\n🎉 Blackjack! " + player_name + " got 21!")
            break
        elif player_score > 21:
            print("\n💥 " + player_name + " busted! (" + str(player_score) + " points)")
            break

        choice = input("\nWhat would you like to do? [h] Hit / [s] Stand: ").lower()

        if choice == "h":
            new_card = draw_card(deck)
            player_hand.append(new_card)
            print("\n" + player_name + " drew a card: " + new_card)
            show_hand(player_name, player_hand)
        elif choice == "s":
            print("\n" + player_name + " stands. (" + str(calculate_score(player_hand)) + " points)")
            break
        else:
            print("Invalid choice. Enter 'h' or 's'.")

    player_score = calculate_score(player_hand)

    #KRUPİYER OYNUYOR
    print("\n--- Dealer's Turn ---")
    show_hand("Dealer", dealer_hand)

    while calculate_score(dealer_hand) < 17:
        new_card = draw_card(deck)
        dealer_hand.append(new_card)
        print("Dealer drew a card: " + new_card)
        show_hand("Dealer", dealer_hand)

    dealer_score = calculate_score(dealer_hand)

    # OYUNUN SONUCU
    print("\n" + "="*45)
    print("            RESULT")
    print("="*45)
    show_hand(player_name, player_hand)
    show_hand("Dealer", dealer_hand)
    print()

    if player_score > 21:
        print("❌ " + player_name + " loses! -$" + str(bet))
        balance -= bet
    elif dealer_score > 21:
        print("✅ Dealer busted! " + player_name + " wins! +$" + str(bet))
        balance += bet
    elif player_score > dealer_score:
        print("✅ " + player_name + " wins! +$" + str(bet))
        balance += bet
    elif player_score < dealer_score:
        print("❌ " + player_name + " loses! -$" + str(bet))
        balance -= bet
    else:
        print("🤝 Push! Bet returned.")

    print("\n💰 Current Balance: $" + str(balance))
    return balance


def main():
    print("="*45)
    print("        WELCOME TO BLACKJACK")
    print("="*45)

    player_name = input("Your Name: ").strip()
    if not player_name:
        player_name = "Player"

    while True:
        try:
            balance = int(input("Starting balance ($): "))
            if balance > 0:
                break
            else:
                print("Balance must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

    wins = 0
    losses = 0
    games_played = 0

    while True:
        if balance <= 0:
            print("\nYou are out of balance. Game over.")
            break

        old_balance = balance
        balance = play_game(player_name, balance)
        games_played += 1

        if balance > old_balance:
            wins += 1
        elif balance < old_balance:
            losses += 1

        play_again = input("\nDo you want to play again? [y/n]: ").lower()
        if play_again != "y":
            break

    # ÖZET
    print("\n" + "="*45)
    print("  Game Summary - " + player_name)
    print("="*45)
    print("  Total Games : " + str(games_played))
    print("  Wins        : " + str(wins))
    print("  Losses      : " + str(losses))
    print("  Final Balance: $" + str(balance))
    print("="*45)
    print("  Have a good day!")

if __name__ == "__main__":
    main()