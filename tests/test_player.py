import unittest
from engine.player import Player


class TestEngine(unittest.TestCase):
    def setUp(self):
        self.player = Player("b")

    def test_shouldReturnNewGame(self):
        self.assertTrue(self.player.player_id is not None)

    def test_shouldReturnPieces(self):
        self.assertEqual(len(self.player.pieces), 16)
