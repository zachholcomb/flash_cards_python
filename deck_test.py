import unittest

from lib.card import Card
from lib.turn import Turn
from lib.deck import Deck

class Test(unittest.TestCase):
  def setUp(self):
    self.card_1 = Card("Geography", "What is the capital of Alaska?", "Juneau")
    self.card_2 = Card("STEM", "The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet?", "Mars")
    self.card_3 = Card("STEM", "Describe in words the exact direction that is 697.5° clockwise from due north?", "North north west")
    self.deck = Deck([self.card_1, self.card_2, self.card_3])

  def test_it_has_attributes(self):
    self.assertEqual(self.deck.cards, [self.card_1, self.card_2, self.card_3])

if __name__ == '__main__':
  unittest.main()