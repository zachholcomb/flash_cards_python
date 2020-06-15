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
    if len(sorted_deck) >= 1:
      self.current_card = sorted_deck[0]
    else:
      self.current_card = 'No More Cards'

  def number_correct(self):
    count = 0
    for turn in self.turns:
      if turn.correct():
        count += 1
    return count

  def number_correct_by_category(self, category):
    count = 0
    for turn in self.turns:
      if turn.correct() and turn.card.category == category:
        count += 1
    return count

  def percent_correct(self):
    total_correct = self.number_correct()
    total_turns = len(self.turns)
    value = total_correct / total_turns * 100
    return round(value, 2)

  def turns_by_category(self, category):
    count = 0
    for turn in self.turns:
      if turn.card.category == category:
        count += 1
    return count

  def percent_correct_by_category(self, category):
    total_correct = self.number_correct_by_category(category)
    total_turns = self.turns_by_category(category)
    value = total_correct / total_turns * 100
    return round(value, 2)
    
