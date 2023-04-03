import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
 
    def setUp(self):
        self.card1 = Card("Hearts",1)
        self.card2 = Card("Diamonds",4) 
        self.card_game = CardGame()

    def test_get_value(self):
        self.assertEqual(1, self.card1.value)

    def test_get_suit(self):
        self.assertEqual("Hearts", self.card1.suit)

    def test_check_for_ace(self):
        result = self.card_game.check_for_ace(self.card1)
        self.assertEqual(True, result)

    def test_highest_card(self):
        result = self.card_game.highest_card(self.card1, self.card2)
        self.assertEqual(self.card2, result)

    def test_cards_total(self):
        cards = [self.card1, self.card2]
        result = self.card_game.cards_total(cards)
        self.assertEqual("You have a total of 5", result)