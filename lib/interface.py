from lib.card import Card
from lib.deck import Deck
from lib.round import Round
from lib.turn import Turn

class Interface:
  def __init__(self, deck):
    self.round = Round(deck)
    self.line_break = "-----------------------------------------------------------------"
    self.total_cards = len(self.round.deck.cards)

  def welcome(self):
    print(self.line_break)
    print(f"|             Welcome! You're playing with {self.total_cards} cards!             |")
    print(self.line_break)
    print(f"|                     This is card 1 out of {self.total_cards}.                  |")
    print(self.line_break)
    guess = input(self.round.current_card.question)
    self.check_answer(guess)

  def check_answer(self, guess):
    print(self.line_break)
    self.round.take_turn(guess)
    print(self.round.turns[-1].feedback())
    self.next_card()
  
  def next_card(self):
    if self.round.current_card == 'No More Cards':
      print(self.line_break)
      print(self.round.current_card)
      self.round_feedback()
    else:
      print(self.line_break)
      total = len(self.round.deck.cards)
      print(f"This is card {len(self.round.turns) + 1} out of {self.total_cards}")
      print(self.line_break)
      guess = input(self.round.current_card.question)
      self.check_answer(guess)

  def round_feedback(self):
    total = len(self.round.deck.cards)
    print(self.line_break)
    print("|                     ****** Game over! *******                  |")
    print(self.line_break)
    print(f"You had {self.round.number_correct()} correct guess out of {self.total_cards} for a total score of {self.round.percent_correct()}%.")
    self.round_category_feedback()

  def round_category_feedback(self):
    for category in self.round.deck.all_categories():
      print(f"{category} - {self.round.percent_correct_by_category(category)}% correct")
    print(self.line_break)
