import unittest
import engine.piece


class TestEngine(unittest.TestCase):
    def test_shouldInitializeKing(self):
        self.black_king = engine.piece.King("b", [0, 4])

        self.assertEqual(self.black_king.color, "b")
        self.assertEqual(self.black_king.name, "King")
        self.assertEqual(self.black_king.value, 10)
        self.assertEqual(self.black_king.Square.row, 0)
        self.assertEqual(self.black_king.Square.column, 4)

        self.white_king = engine.piece.King("w", [7, 3])

        self.assertEqual(self.white_king.color, "w")
        self.assertEqual(self.white_king.name, "King")
        self.assertEqual(self.white_king.value, 10)
        self.assertEqual(self.white_king.Square.row, 7)
        self.assertEqual(self.white_king.Square.column, 3)

    def test_shouldInitializeQueen(self):
        self.black_queen = engine.piece.Queen("b", [0, 3])

        self.assertEqual(self.black_queen.color, "b")
        self.assertEqual(self.black_queen.name, "Queen")
        self.assertEqual(self.black_queen.value, 9)
        self.assertEqual(self.black_queen.Square.row, 0)
        self.assertEqual(self.black_queen.Square.column, 3)

        self.white_queen = engine.piece.Queen("w", [7, 4])

        self.assertEqual(self.white_queen.color, "w")
        self.assertEqual(self.white_queen.name, "Queen")
        self.assertEqual(self.white_queen.value, 9)
        self.assertEqual(self.white_queen.Square.row, 7)
        self.assertEqual(self.white_queen.Square.column, 4)

    def test_shouldInitializeRook(self):
        self.rook = engine.piece.Rook("b", [0, 0])

        self.assertEqual(self.rook.color, "b")
        self.assertEqual(self.rook.name, "Rook")
        self.assertEqual(self.rook.value, 5)
        self.assertEqual(self.rook.Square.row, 0)
        self.assertEqual(self.rook.Square.column, 0)

    def test_shouldInitializeBishop(self):
        self.bishop = engine.piece.Bishop("b", [0, 0])

        self.assertEqual(self.bishop.color, "b")
        self.assertEqual(self.bishop.name, "Bishop")
        self.assertEqual(self.bishop.value, 3)
        self.assertEqual(self.bishop.Square.row, 0)
        self.assertEqual(self.bishop.Square.column, 0)

    def test_shouldInitializeKnight(self):
        self.knight = engine.piece.Knight("b", [0, 0])

        self.assertEqual(self.knight.color, "b")
        self.assertEqual(self.knight.name, "Knight")
        self.assertEqual(self.knight.value, 3)
        self.assertEqual(self.knight.Square.row, 0)
        self.assertEqual(self.knight.Square.column, 0)

    def test_shouldInitializePawn(self):
        self.pawn = engine.piece.Pawn("b", [0, 0])

        self.assertEqual(self.pawn.color, "b")
        self.assertEqual(self.pawn.name, "Pawn")
        self.assertEqual(self.pawn.value, 1)
        self.assertEqual(self.pawn.Square.row, 0)
        self.assertEqual(self.pawn.Square.column, 0)
