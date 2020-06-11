import unittest

from lib.card import Card
from lib.turn import Turn

class Test(unittest.TestCase):
  def setUp(self):
    self.card = Card("Geography", "What is it?", "I don't know!")
    self.turn = Turn("I know!", self.card)
    self.turn2 = Turn("I don't know!", self.card)
  
  def test_it_has_attributes(self):
    self.assertEqual(self.turn.guess, "I know!")
    self.assertEqual(self.turn2.guess, "I don't know!")
    self.assertEqual(self.turn.card.category, 'Geography')
    self.assertEqual(self.turn.card.question, "What is it?")
    self.assertEqual(self.turn.card.answer, "I don't know!")

  def test_correct(self):
    self.assertFalse(self.turn.correct())
    self.assertTrue(self.turn2.correct())

  def test_feedback(self):
    self.assertEqual(self.turn.feedback(), 'Incorrect')
    self.assertEqual(self.turn2.feedback(), 'Correct')

if __name__ == '__main__':
  unittest.main()
    