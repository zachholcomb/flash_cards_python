class Deck:
  def __init__(self, cards):
    self.cards = cards

  def add_card(self, card):
    self.cards.append(card)