import unittest

from engine.state import State


class TestEngine(unittest.TestCase):
    def setUp(self):
        self.state = State()

    def test_pieceCountsAreReset(self):
        self.state.reset_pieces()

        self.assertEquals(self.state.b_king, 1)
        self.assertEquals(self.state.b_queen, 1)
        self.assertEquals(self.state.b_knight, 2)
        self.assertEquals(self.state.b_bishop, 2)
        self.assertEquals(self.state.b_rook, 2)
        self.assertEquals(self.state.b_pawn, 8)

        self.assertEquals(self.state.w_king, 1)
        self.assertEquals(self.state.w_queen, 1)
        self.assertEquals(self.state.w_knight, 2)
        self.assertEquals(self.state.w_bishop, 2)
        self.assertEquals(self.state.w_rook, 2)
        self.assertEquals(self.state.w_pawn, 8)
