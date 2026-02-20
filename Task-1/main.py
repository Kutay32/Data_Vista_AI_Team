import random


def deal_card():
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    return random.choice(cards)


def card_value(card, current_score):
    if card in ["J", "Q", "K"]:
        return 10
    elif card == "A":
        if current_score + 11 <= 21:
            return 11
        else:
            return 1
    else:
        return int(card)


def calculate_score(hand):
    score = 0
    aces = 0
    
    for card in hand:
        if card == "A":
            aces += 1
        else:
            score += card_value(card, score)
    
    for _ in range(aces):
        if score + 11 <= 21:
            score += 11
        else:
            score += 1
    
    return score


def blackjack_game():
    print("=== BLACKJACK GAME ===")
    
    player_name = input("Enter your name: ")
    
    while True:
        try:
            balance = int(input("Enter your starting balance ($): "))
            if balance > 0:
                break
            else:
                print("Balance must be greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    wins = 0
    losses = 0
    
    while True:
        if balance <= 0:
            print(f"\n{player_name}, you have no money left. Game over!")
            break
        
        print(f"\n--- NEW ROUND ---")
        print(f"Player: {player_name}")
        print(f"Balance: ${balance}")
        print(f"Wins: {wins} | Losses: {losses}")
        
        while True:
            try:
                bet = int(input(f"Enter your bet (max ${balance}): "))
                if 0 < bet <= balance:
                    break
                else:
                    print(f"Bet must be between $1 and ${balance}.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        player_hand = [deal_card(), deal_card()]
        dealer_hand = [deal_card(), deal_card()]
        
        game_over = False
        
        while not game_over:
            player_score = calculate_score(player_hand)
            print(f"\nYour cards: {player_hand} (Score: {player_score})")
            print(f"Dealer's visible card: {dealer_hand[0]}")
            
            if player_score == 21:
                print("Blackjack!")
                break
            elif player_score > 21:
                print("Bust! You exceeded 21.")
                game_over = True
                break
            
            action = input("Do you want to (h)it or (s)tand? ").lower()
            if action == "h":
                player_hand.append(deal_card())
            elif action == "s":
                break
            else:
                print("Invalid choice. Enter 'h' or 's'.")
        
        if not game_over:
            print("\n--- Dealer's Turn ---")
            dealer_score = calculate_score(dealer_hand)
            
            while dealer_score < 17:
                dealer_hand.append(deal_card())
                dealer_score = calculate_score(dealer_hand)
            
            print(f"Dealer's cards: {dealer_hand} (Score: {dealer_score})")
            
            player_score = calculate_score(player_hand)
            
            if dealer_score > 21:
                print(f"{player_name} wins! Dealer busted.")
                balance += bet
                wins += 1
            elif player_score > dealer_score:
                print(f"{player_name} wins!")
                balance += bet
                wins += 1
            elif player_score < dealer_score:
                print(f"{player_name} loses.")
                balance -= bet
                losses += 1
            else:
                print("It's a tie. Bet returned.")
        else:
            print(f"{player_name} loses.")
            balance -= bet
            losses += 1
        
        print(f"\nCurrent Balance: ${balance}")
        
        play_again = input("Play another round? (y/n): ").lower()
        if play_again != "y":
            print(f"\n=== GAME OVER ===")
            print(f"Player: {player_name}")
            print(f"Final Balance: ${balance}")
            print(f"Total Wins: {wins} | Total Losses: {losses}")
            break


if __name__ == "__main__":
    blackjack_game()
