import unittest
from engine.game import Game


class TestEngine(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_shouldReturnNewGame(self):
        self.assertTrue(self.game.game_id is not None)
