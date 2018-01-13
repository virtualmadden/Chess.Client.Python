import uuid
import engine.piece


class Player(object):
    def __init__(self, color):
        self.player_id = uuid.uuid4()

        self.pieces = []

        if color is "b":
            self.pieces.append(engine.piece.King(color, [0, 4]))
            self.pieces.append(engine.piece.Queen(color, [0, 3]))
            self.pieces.append(engine.piece.Bishop(color, [0, 2]))
            self.pieces.append(engine.piece.Bishop(color, [0, 5]))
            self.pieces.append(engine.piece.Knight(color, [0, 1]))
            self.pieces.append(engine.piece.Knight(color, [0, 6]))
            self.pieces.append(engine.piece.Rook(color, [0, 0]))
            self.pieces.append(engine.piece.Rook(color, [0, 7]))

            for x in range(0, 8):
                self.pieces.append(engine.piece.Pawn(color, [1, x]))
        else:
            self.pieces.append(engine.piece.King(color, [7, 3]))
            self.pieces.append(engine.piece.Queen(color, [7, 4]))
            self.pieces.append(engine.piece.Bishop(color, [7, 2]))
            self.pieces.append(engine.piece.Bishop(color, [7, 5]))
            self.pieces.append(engine.piece.Knight(color, [7, 1]))
            self.pieces.append(engine.piece.Knight(color, [7, 6]))
            self.pieces.append(engine.piece.Rook(color, [7, 0]))
            self.pieces.append(engine.piece.Rook(color, [7, 7]))

            for x in range(0, 8):
                self.pieces.append(engine.piece.Pawn(color, [6, x]))
