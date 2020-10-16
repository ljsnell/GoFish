from collections import Counter

import Deck
import Utilities
deck = Deck.Deck()
utilities = Utilities.Utilities()

deck_list = deck.create_deck()

hand1 = []
hand2 = []

hand_size = 7

player1_pts = 0
player2_pts = 0

hand1, deck_list = deck.draw_cards(deck_list, hand1, hand_size)
hand2, deck_list = deck.draw_cards(deck_list, hand2, hand_size)

print(hand1)
print(hand2)

while 1 < 2:
    # P1 guess card
    current_player = 'Player 1'
    p1_guess = int(input("Guess a card: "))
    
    # Player 1 actions:
    guessing_hand, target_hand, index = utilities.is_card_in_hand(hand1, hand2, p1_guess, deck_list, deck, current_player)

    # Check if there's 4 in the hand
    counts = Counter(hand1)    
    print(counts)

    hand1, player1_pts = utilities.scoring_cycle(counts, hand1, "Player1's score: ", player1_pts)

    current_player = 'Player 2'

    # P2 guess card

    # Draw card if it doesn't match
