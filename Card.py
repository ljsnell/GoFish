class Card:
    def __init__(self, card_number, color):
        self.card_number = card_number
        self.color = color
        self.id = str(self.card_number) + ":" + self.color

    def __repr__(self):
        return str(self.card_number)
    
    def __eq__(self, other):
        return self.card_number == other.card_number

    def __hash__(self):
        return hash(self.card_number)
