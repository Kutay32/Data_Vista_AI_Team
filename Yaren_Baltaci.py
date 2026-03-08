import random

kartlar = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def kart_cek():
    return random.choice(kartlar)

def el_toplami(el):
    toplam = 0
    as_sayisi = 0

    for kart in el:
        if kart == "J" or kart == "Q" or kart == "K":
            toplam += 10
        elif kart == "A":
            toplam += 11
            as_sayisi += 1
        else:
            toplam += int(kart)

    while toplam > 21 and as_sayisi > 0:
        toplam -= 10
        as_sayisi -= 1

    return toplam

print("=== BLACKJACK OYUNU ===")

isim = input("Adınızı girin: ")
bakiye = 1000
kazanma = 0
kaybetme = 0

devam = "e"

while devam == "e" and bakiye > 0:
    print("\nBakiyeniz:", bakiye, "TL")

    bahis = int(input("Bahis miktarını girin: "))

    while bahis > bakiye or bahis <= 0:
        print("Hatalı bahis girdiniz.")
        bahis = int(input("Tekrar bahis girin: "))

    oyuncu = []
    krupiye = []

    oyuncu.append(kart_cek())
    oyuncu.append(kart_cek())

    krupiye.append(kart_cek())
    krupiye.append(kart_cek())

    print("\nKrupiyenin ilk kartı:", krupiye[0])
    print(isim, "kartların:", oyuncu)
    print("Toplam puanın:", el_toplami(oyuncu))

    # Oyuncunun sırası
    while el_toplami(oyuncu) < 21:
        secim = input("Kart çekmek için h, durmak için s: ")

        if secim == "h":
            yeni_kart = kart_cek()
            oyuncu.append(yeni_kart)
            print("Yeni kartın:", yeni_kart)
            print("Kartların:", oyuncu)
            print("Toplam puanın:", el_toplami(oyuncu))
        elif secim == "s":
            break
        else:
            print("Yanlış giriş yaptın.")

    oyuncu_toplam = el_toplami(oyuncu)

    # Oyuncu 21'i geçtiyse direkt kaybeder
    if oyuncu_toplam > 21:
        print("\n21'i geçtin, kaybettin.")
        bakiye -= bahis
        kaybetme += 1

    else:
        # Krupiyenin sırası
        print("\nKrupiyenin kartları:", krupiye)
        print("Krupiye puanı:", el_toplami(krupiye))

        while el_toplami(krupiye) < 17:
            yeni_kart = kart_cek()
            krupiye.append(yeni_kart)
            print("Krupiye kart çekti:", yeni_kart)
            print("Krupiyenin kartları:", krupiye)
            print("Krupiye puanı:", el_toplami(krupiye))

        krupiye_toplam = el_toplami(krupiye)

        print("\n--- SONUÇ ---")
        print(isim, "kartların:", oyuncu, "Toplam:", oyuncu_toplam)
        print("Krupiye kartları:", krupiye, "Toplam:", krupiye_toplam)

        if krupiye_toplam > 21:
            print("Krupiye 21'i geçti, kazandın.")
            bakiye += bahis
            kazanma += 1
        elif oyuncu_toplam > krupiye_toplam:
            print("Kazandın.")
            bakiye += bahis
            kazanma += 1
        elif oyuncu_toplam < krupiye_toplam:
            print("Kaybettin.")
            bakiye -= bahis
            kaybetme += 1
        else:
            print("Berabere.")

    print("Yeni bakiyen:", bakiye, "TL")
    print("Kazanma:", kazanma, "Kaybetme:", kaybetme)

    if bakiye <= 0:
        print("Paran bitti. Oyun sona erdi.")
        break

    devam = input("\nTekrar oynamak ister misin? (e/h): ")

print("\nOyun bitti.")
print("Oyuncu:", isim)
print("Son bakiye:", bakiye)
print("Toplam kazanma:", kazanma)
print("Toplam kaybetme:", kaybetme)
