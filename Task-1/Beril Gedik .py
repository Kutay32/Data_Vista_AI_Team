import random

def create_deck():
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = cards * 4
    return deck

# Puan hesapla 
def calculate_score(hand):
    score = 0
    ace_count = 0

    for card in hand:
        if card in ["J", "Q", "K"]:
            score += 10
        elif card == "A":
            score += 11
            ace_count += 1
        else:
            score += int(card)

    # Toplam 21’i geçiyorsa As’ları 11 yerine 1 sayıyoruz  
    while total >21 and ace_count >0:
        score -= 10
        ace_count -= 1

    return score

# El açılıyor 
def deal_card(deck):
    return deck.pop()


# Game start
player_name = input("İsminizi giriniz: ")
balance = 1000
wins = 0
losses = 0

print(f"\nHoş geldiniz {player_name}! Başlangıç bakiyeniz: {balance} TL")

while balance > 0:

    print(f"\nMevcut bakiyeniz: {balance} TL")
    bet = int(input("Bahis miktarını giriniz: "))

    if bet > balance or bet <= 0:
        print("Geçersiz bahis miktarı!")
        continue

    deck = create_deck()

    player_hand = [deal_card(deck), deal_card(deck)]
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # Player turn
    while True:
        player_score = calculate_score(player_hand)
        print(f"\nKartlarınız: {player_hand} | Skorunuz: {player_score}")
        print(f"Krupiyenin açık kartı: {dealer_hand[0]}")

        if player_score > 21:
            print("21'i geçtiniz! Kaybettiniz.")
            balance -= bet
            losses += 1
            break

        choice = input("Kart çekmek için 'c', durmak için 'd' giriniz: ")

        if choice.lower() == "c":
            player_hand.append(deal_card(deck))
        elif choice.lower() == "d":
            break
        else:
            print("Geçersiz seçim!")

    # Dealer turn
    if player_score <= 21:
        print(f"\nKrupiyenin kartları: {dealer_hand}")
        while calculate_score(dealer_hand) < 17:
            dealer_hand.append(deal_card(deck))

        dealer_score = calculate_score(dealer_hand)

        print(f"Krupiyenin son kartları: {dealer_hand} | Skoru: {dealer_score}")

        if dealer_score > 21 or player_score > dealer_score:
            print("Tebrikler! Kazandınız.")
            balance += bet
            wins += 1
        elif player_score < dealer_score:
            print("Kaybettiniz.")
            balance -= bet
            losses += 1
        else:
            print("Berabere!")

    print(f"Güncel bakiyeniz: {balance} TL")
    print(f"Toplam Kazanma: {wins} | Toplam Kaybetme: {losses}")

    again = input("\nTekrar oynamak ister misiniz? (e/h): ")
    if again.lower() != "e":
        break

print("\nOyun sona erdi.")
print(f"Final bakiyeniz: {balance} TL")
print(f"Toplam Kazanma: {wins} | Toplam Kaybetme: {losses}")
