import unittest

from lib.card import Card
from lib.deck import Deck
from lib.round import Round
from lib.turn import Turn

class Test(unittest.TestCase):
  def setUp(self):
    self.card_1 = Card("Geography", "What is the capital of Alaska?", "Juneau")
    self.card_2 = Card("STEM", "The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars")
    self.card_3 = Card("STEM", "Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west")
    self.deck = Deck([self.card_1, self.card_2, self.card_3])
    self.round = Round(self.deck)

  def test_it_has_attributes(self):
    self.assertEqual(self.round.deck, self.deck)
    expected = "What is the capital of Alaska?"
    self.assertEqual(self.round.deck.cards, [self.card_1, self.card_2, self.card_3])
    self.assertEqual(self.round.deck.cards[0].question, expected)
    self.assertEqual(self.round.turns, [])

  def test_it_has_current_card(self):
    self.assertEqual(self.round.current_card, self.card_1)

  def test_it_can_take_turn(self):
    self.round.take_turn('Juneau')
    new_turn = self.round.turns[0]
    self.assertTrue(new_turn.correct())
    self.assertEqual(new_turn.feedback(), 'Correct')
    self.assertEqual(len(self.round.turns), 1)
    self.assertEqual(self.round.current_card, self.card_2)
    
    self.round.take_turn('Venus')
    new_turn2 = self.round.turns[1]
    self.assertFalse(new_turn2.correct())
    self.assertEqual(new_turn2.feedback(), 'Incorrect')
    self.assertEqual(len(self.round.turns), 2)
    self.assertEqual(self.round.current_card, self.card_3)

    self.round.take_turn('North north west')
    new_turn3 = self.round.turns[2]
    self.assertTrue(new_turn3.correct())
    self.assertEqual(new_turn3.feedback(), 'Correct')
    self.assertEqual(len(self.round.turns), 3)
    self.assertEqual(self.round.current_card, 'No More Cards')


  def test_it_can_calculate_number_correct(self):
    self.round.take_turn('Juneau')
    self.round.take_turn('Venus')
    self.assertEqual(self.round.number_correct(), 1)

  def test_it_can_calculate_number_correct_by_category(self):
    self.round.take_turn('Ohio')
    self.round.take_turn('Mars')
    self.round.take_turn('North north west')
    self.assertEqual(self.round.number_correct_by_category('STEM'), 2)
    self.assertEqual(self.round.number_correct_by_category('Geography'), 0)

  def test_it_can_calculate_percent_correct(self):
    self.round.take_turn('Ohio')
    self.round.take_turn('Mars')
    self.round.take_turn('North north west')
    self.assertEqual(self.round.percent_correct(), 66.67)

  def test_it_can_calculate_turns_by_category(self):
    self.round.take_turn('Ohio')
    self.round.take_turn('Mars')
    self.round.take_turn('North north west')
    self.assertEqual(self.round.turns_by_category('Geography'), 1)
    self.assertEqual(self.round.turns_by_category('STEM'), 2)

  def test_it_can_calculate_percent_correct_by_category(self):
    self.round.take_turn('Ohio')
    self.round.take_turn('Mars')
    self.round.take_turn('North north west')
    self.assertEqual(self.round.percent_correct_by_category('Geography'), 0.00)
    self.assertEqual(self.round.percent_correct_by_category('STEM'), 100.00)

if __name__ == '__main__':
  unittest.main()