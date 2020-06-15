from lib.card import Card
from lib.deck import Deck
from lib.round import Round
from lib.turn import Turn
from lib.interface import Interface

card1 = Card("Geography", "What is the capital of Alaska? ", "Juneau")
card2 = Card("STEM", "The Viking spacecraft sent back to Earth photographs and reports about the surface of which planet? ", "Mars")
card3 = Card("STEM", "Describe in words the exact direction that is 697.5° clockwise from due north? ", "North north west")
deck = Deck([card1, card2, card3])
interface = Interface(deck)
interface.welcome()