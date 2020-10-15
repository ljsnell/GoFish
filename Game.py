from collections import Counter

import Deck
deck = Deck.Deck()

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
    for index, card in enumerate(hand2):
        if card.card_number == p1_guess:
            hand1.append(hand2.pop(index))
            print('You guessed it!')
            print(hand1)
            print(hand2)
        else:
            index = -1

    if index == -1:
        print('Go Fish!')
        # Draw card if it doesn't match
        hand1, deck_list = deck.draw_cards(deck_list, hand1, 1)
        print(current_player + "'s hand is: ")
        print(hand1)

    # Check if there's 4 in the hand
    counts = Counter(hand1)    
    print(counts)
    for ele in counts:
        if (counts[ele] == 4):
            print("Theres 4 of this card:")
            print(ele)

    current_player = 'Player 2'
    # if myItem in list:
    # https://stackoverflow.com/questions/9371114/check-if-list-of-objects-contain-an-object-with-a-certain-attribute-value

    

    # P2 guess card

    # Draw card if it doesn't match
