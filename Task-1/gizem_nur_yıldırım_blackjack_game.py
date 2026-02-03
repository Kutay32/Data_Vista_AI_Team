import random


def deal_card():
    """Rastgele bir kart secmeliyiz."""
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    return random.choice(cards)


def card_value(card, current_score):
    """Kartin sayisal degerini hesaplamaliyiz."""
    if card in ["J", "Q", "K"]:
        return 10
    else:
        return int(card)


def calculate_score(hand):
    """Eldeki kartlarin toplam puanini hesaplamaliyiz."""
    score = 0
    ace = 0
    for card in hand:
        if card != "A":
            score += card_value(card, score)
        else:
            ace += 1

    for i in range(ace):
        if score + 11 <= 21:
            score += 11
        else:
            score += 1
    return score


# OYUN MANTIGI

def blackjack_game():
    print("--- WELCOME TO THE GAME OF BLACKJACK 🤗🎰 ---")
    player_name = input("Please enter your name: ")
    # bakiyeyi kullanicidan istiyoruz
    while True:
        try:
            balance = int(input("Enter your balance to start the game ($): "))
            if balance > 0:
                break
            else:
                print("Please enter an amount greater than 0.")
        except ValueError:
            print("Invalid input! Please enter a numerical value.")

    wins = 0
    losses = 0

    while True:
        if balance <= 0:
            print(f"\n Sorry {player_name}, your balance is zero ($0)! Game over.")
            break

        print(f"\n --- NEW HAND ---")
        print(f"Current Balance: ${balance}")
        print(f"Your Score -> Wins: {wins} | Losses: {losses}")

        # bahis sistemi
        while True:
            try:
                bet = int(input(f"Enter bet amount (Maximum ${balance}): "))
                if 0 < bet <= balance:
                    break
                else:
                    print("Invalid amount! You can't bet more than your balance or 0.")
            except ValueError:
                print("Please enter a numeric value.")

        # kart dagilimi
        player_hand = [deal_card(), deal_card()]
        dealer_hand = [deal_card(), deal_card()]

        game_over = False

        # oyuncu sirasi
        while not game_over:
            player_score = calculate_score(player_hand)
            print(f"\nYour Hand: {player_hand} | Total Score: {player_score}")
            print(f"Dealer's First Card: {dealer_hand[0]}")

            if player_score == 21:
                print("Blackjack! You hit 21! 🔥")
                break
            elif player_score > 21:
                print("Busted! (You went over 21).☹️")
                game_over = True
                break

            choice = input("Press 'h' to hit, 's' to stand: ").lower()
            if choice == "h":
                player_hand.append(deal_card())
            elif choice == "s":
                break
            else:
                print("Invalid key, please try again.")

        # dealer sirasi
        if not game_over:
            print("\n--- Dealer is playing ---")
            dealer_score = calculate_score(dealer_hand)

            # Dealer'in 17den az olma durumu
            while dealer_score < 17:
                print(f"Dealer hits... (Current hand: {dealer_hand})")
                dealer_hand.append(deal_card())
                dealer_score = calculate_score(dealer_hand)

            print(f"Dealer's Hand: {dealer_hand} | Total Score: {dealer_score}")

            # sonuclari karsilastirma
            if dealer_score > 21:
                print("Dealer busted! YOU WIN! 🎉")
                balance += bet
                wins += 1
            elif player_score > dealer_score:
                print(f"Congratulations {player_name}! YOU WIN! 🎉")
                balance += bet
                wins += 1
            elif player_score < dealer_score:
                print("Dealer's hand is better. YOU LOSE. 😔")
                balance -= bet
                losses += 1
            else:
                print("It's a tie. Bet returned.")
        else:
            # player > 21
            print("YOU LOSE. 😔")
            balance -= bet
            losses += 1

        # tekrar oynama istegini sorma
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            print(f"\nGame over! Final Balance: ${balance}. See you later {player_name}!")
            break


# oyunu baslatma
blackjack_game()
