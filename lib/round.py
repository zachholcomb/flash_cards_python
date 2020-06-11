from .turn import Turn

class Round:
  def __init__(self, deck):
    self.deck = deck
    self.turns = []
    self.current_card = self.deck.cards[0]

  def take_turn(self, guess):
    new_turn = Turn(guess, self.current_card)
    self.turns.append(new_turn)
    sort_amount = len(self.turns)
    sorted_deck = self.deck.cards[sort_amount:]
    self.current_card = sorted_deck[0]

  def number_correct(self):
    count = 0
    list_size = len(self.turns)
    for turn in self.turns:
      if turn.correct():
        count += 1
    return count