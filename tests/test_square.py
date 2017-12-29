import unittest

from engine.square import Square


class TestEngine(unittest.TestCase):
    def setUp(self):
        self.square = Square()

    def test_isOnBoard(self):
        self.assertEquals(self.square.on_board(1, 1), True)

    def test_isNotOnBoard(self):
        self.assertEquals(self.square.on_board(1, 9), False)
