import Card
import random

class Deck:

    def create_deck(self):
        colors = ['♥', '♦', '♠', '♣']

        deck = [Card.Card(value, color) for value in range(1, 14) for color in colors]

        random.shuffle(deck)

        return deck

    def draw_cards(self, deck, hand, card_number):

        for i in range(card_number):
            hand.append(deck.pop(0))

        return hand, deck
