import unittest
from engine.board import Board


class TestEngine(unittest.TestCase):
    def setUp(self):
        self.board = Board()

    def test_isOnBoard(self):
        self.assertEquals(self.board.on_board([1, 1]), True)

    def test_isNotOnBoard(self):
        self.assertEquals(self.board.on_board([1, 9]), False)
