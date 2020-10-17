from collections import Counter

class Utilities:

    def is_card_in_hand(self, guessing_hand, target_hand, guess, deck_list, deck, current_player):
        for index, card in enumerate(target_hand):
            if card.card_number == guess:
                guessing_hand.append(target_hand.pop(index))
                print('You guessed it!')
                print(guessing_hand)
                print(target_hand)
                break            
            else:
                index = -1
        if index == -1:
            print('Go Fish!')
            # Draw card if it doesn't match
            hand, deck_list = deck.draw_cards(deck_list, guessing_hand, 1)
            print(current_player + "'s hand is: ")
            print(hand)

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