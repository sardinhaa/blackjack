import random

cards_list = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']

def card_value(card):
    if card in ['Jack', 'Queen', 'King']:
        return 10
    elif card == 'Ace':
        return 11
    else:
        return int(card)
player_wins = 0
dealer_wins = 0
ties = 0
while True:
    deck = cards_list * 4
    random.shuffle(deck)
    player_card = [deck.pop(), deck.pop()]
    dealer_card = [deck.pop(), deck.pop()]
    while True:
        player_score = sum(card_value(card) for card in player_card)
        print("\nCards Player Has:", player_card)
        print("Score Of The Player:", player_score)
        if player_score > 21:
            print("You lost! (Your score exceeded 21)")
            dealer_wins += 1
            break
        if player_score == 21:
            print("You hit 21! Standing automatically.")
            break 
        choice = input('What do you want? ["1" to hit, "2" to stand, "q" to quit]: ').lower()
        if choice == "1":
            new_card = deck.pop()
            player_card.append(new_card)
        elif choice == "2":
            break
        elif choice == "q":
            print(f"\nFinal Score: You {player_wins} - Dealer {dealer_wins} (Ties: {ties})")
            print("Thanks for playing!")
            exit()
        else:
            print("Invalid choice. Please try again.")
    player_score = sum(card_value(card) for card in player_card)
    if player_score <= 21:
        dealer_score = sum(card_value(card) for card in dealer_card)
        while dealer_score < 17:
            new_card = deck.pop()
            dealer_card.append(new_card)
            dealer_score += card_value(new_card)
        print("\nCards Dealer Has:", dealer_card)
        print("Score Of The Dealer:", dealer_score)
        if dealer_score > 21:
            print("Dealer busts! You win!")
            player_wins += 1
        elif player_score > dealer_score:
            print("You win! (Higher score than dealer)")
            player_wins += 1
        elif dealer_score > player_score:
            print("Dealer wins! (Higher score than you)")
            dealer_wins += 1
        else:
            print("It's a tie!")
            ties += 1
    again = input("\nPlay again? (y/n): ").lower()
    if again != "1":
        print(f"\nFinal Score: You {player_wins} - Dealer {dealer_wins} (Ties: {ties})")
        print("Thanks for playing!")
        break
