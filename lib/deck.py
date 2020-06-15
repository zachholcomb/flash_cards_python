class Deck:
  def __init__(self, cards):
    self.cards = cards

  def add_card(self, card):
    self.cards.append(card)

  def all_categories(self):
    card_categories = []
    for card in self.cards:
      card_categories.append(card.category)
    return list(set(card_categories))