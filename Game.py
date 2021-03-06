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

# Check if either player drew 4 of a kind right away.
hand1, player1_pts = utilities.scoring_cycle(hand1, "Player1's score: ", player1_pts)
hand2, player2_pts = utilities.scoring_cycle(hand2, "Player2's score: ", player2_pts)

while 1 < 2:
    # Check if deck's exhausted
    if(len(deck_list) == 0):
        print("Well played!")
        print("Player 1 Final score:" + str(player1_pts))
        print("Player 2 Final score:" + str(player2_pts))

    correct_guess = True
    while correct_guess == True:
        # P1 guess card
        current_player = 'Player 1'
        utilities.print_hand(hand1, current_player)

        p1_guess = int(input("Guess a card Player 1: "))

        # Player 1 actions:
        hand1, hand2, deck_list, correct_guess = utilities.is_card_in_hand(hand1, hand2, p1_guess, deck_list, deck, current_player, correct_guess)

        # Check if there's 4 in the hand
        hand1, player1_pts = utilities.scoring_cycle(hand1, "Player1's score: ", player1_pts)
        
        if(len(hand1) == 0):
            hand1, deck_list = deck.draw_cards(deck_list, hand1, 1)
        
        utilities.print_hand(hand1, current_player)
        
    utilities.end_player_cycle()
    correct_guess = True

    while correct_guess == True:
        # Repeat for next player
        current_player = 'Player 2'
        utilities.print_hand(hand2, current_player)

        p2_guess = int(input("Guess a card Player 2: "))

        # Player 2 actions:
        hand2, hand1, deck_list, correct_guess = utilities.is_card_in_hand(hand2, hand1, p2_guess, deck_list, deck, current_player, correct_guess)

        # Check if there's 4 in the hand        
        hand2, player2_pts = utilities.scoring_cycle(hand2, "Player2's score: ", player2_pts)
        if(len(hand2)== 0):
            hand2, deck_list = deck.draw_cards(deck_list, hand2, 1)

        utilities.print_hand(hand2, current_player)
    
    utilities.end_player_cycle()