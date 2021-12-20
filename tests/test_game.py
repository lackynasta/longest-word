import unittest
import string
from game import Game
from nose.tools import eq_

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_empty_word_is_invalid(self):
        new_game = Game()
        self.assertIs(new_game.is_valid(''), False)

    def test_is_invalid(self):
        new_game = Game()
        new_game.grid = list('ARWKNOCGS')
        result = new_game.is_valid('WAGON')
        eq_(True, result)
        self.assertEqual(new_game.grid, list('ARWKNOCGS'))

    def test_is_invalid(self):
        new_game = Game()
        new_game.grid = list('ARWKNOCGS')
        result = new_game.is_valid('LEARN')
        eq_(False, result)
        self.assertEqual(new_game.grid, list('ARWKNOCGS'))

    def test_unknown_word_is_invalid(self):
      new_game = Game()
      new_game.grid = list('ARWKNOCGS') # Forcer la grille à un scénario de test :
      self.assertIs(new_game.is_valid('WONA'), False)

