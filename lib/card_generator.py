import csv
from lib.card import Card

class CardGenerator:
  @classmethod
  def generate_cards(cls):
    cards = []
    with open('lib/cards.csv', 'r') as file:
      reader = csv.reader(file)
      for row in reader:
       cards.append(Card(row[2], row[0], row[1]))
    return cards
