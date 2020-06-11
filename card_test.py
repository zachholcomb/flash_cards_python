import unittest

from lib.card import Card

class Test(unittest.TestCase):
  def setUp(self):
      self.card = Card("Geography", "What is it?", "I don't know!")

  def test_attributes(self):
      self.assertEqual(self.card.category, 'Geography')
      self.assertEqual(self.card.question, "What is it?")
      self.assertEqual(self.card.answer, "I don't know!")


if __name__ == '__main__':
  unittest.main()