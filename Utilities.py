import os
from collections import Counter

class Utilities:

    def is_card_in_hand(self, guessing_hand, target_hand, guess, deck_list, deck, current_player, correct_guess):
        indices = [i for i, x in enumerate(target_hand) if x.card_number == guess]
        
        # Draw card if guess doesn't match
        if not indices:
            print('Go Fish!')
            hand, deck_list = deck.draw_cards(deck_list, guessing_hand, 1)
            correct_guess = False
        # Remove all matching cards from hand
        else:
            print('You guessed it!')
            for index in sorted(indices, reverse=True):
                guessing_hand.append(target_hand.pop(index))                            
                correct_guess = True

        return guessing_hand, target_hand, deck_list, correct_guess

    def scoring_cycle(self, hand, player_name, player_pts):
        counts = Counter(hand)
        match = False
        for ele in counts:
            if (counts[ele] == 4):
                print("Theres 4 of this card:")
                print(ele)
                # Remove element from hand and increment players score by 1.            
                hand.remove(ele)                
                print(player_name + str(player_pts))
                match = True
        if match:
            player_pts += 1
            
        return hand, player_pts

    
    def print_hand(self, hand, player_name):
        print(player_name + ":")
        hand.sort(key=lambda x: x.card_number)
        print(hand)        

    def end_player_cycle(self):
        input("Press enter when ready...")
        os.system('clear')
        input("Please pass the game to the next player...")
