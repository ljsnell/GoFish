from collections import Counter

class Utilities:

    def is_card_in_hand(self, guessing_hand, target_hand, guess, deck_list, deck, current_player):
        indices = [i for i, x in enumerate(target_hand) if x.card_number == guess]
        
        # Draw card if guess doesn't match
        if not indices:
            print('Go Fish!')
            hand, deck_list = deck.draw_cards(deck_list, guessing_hand, 1)            
        else:
            # Remove all matching cards from hand
            for index in sorted(indices, reverse=True):
                guessing_hand.append(target_hand.pop(index))            
                print('You guessed it!')

        return guessing_hand, target_hand, deck_list   

    def scoring_cycle(self, hand, player_name, player_pts):
        counts = Counter(hand)        
        for ele in counts:
            if (counts[ele] == 4):
                print("Theres 4 of this card:")
                print(ele)
                # Remove element from hand and increment players score by 1.            
                hand.remove(ele)
                player_pts += 1
                print(player_name + str(player_pts))

        return hand, player_pts

    
    def print_hands(self, hand1, hand2):
        print("Player 1:")
        hand1.sort(key=lambda x: x.card_number)
        print(hand1)
        print("Player 2:")
        hand2.sort(key=lambda x: x.card_number)
        print(hand2)
