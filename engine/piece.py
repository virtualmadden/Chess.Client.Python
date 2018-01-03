from collections import namedtuple


class Piece(object):
    Location = namedtuple("Location", ["row", "column"])

    def __init__(self, color, value, location):
        self.color = color
        self.value = value
        self.captured = False
        self.Square = self.Location(int(location[0]), int(location[1]))


class King(Piece):
    def __init__(self, color):
        self.name = "King"

        if color is "b":
            Piece.__init__(self, color, 10, [0, 4])
        else:
            Piece.__init__(self, color, 10, [7, 3])


class Queen(Piece):
    def __init__(self, color):
        self.name = "Queen"

        if color is "b":
            Piece.__init__(self, color, 9, [0, 3])
        else:
            Piece.__init__(self, color, 9, [7, 4])


class Rook(Piece):
    def __init__(self, color, location):
        self.name = "Rook"

        Piece.__init__(self, color, 5, location)


class Bishop(Piece):
    def __init__(self, color, location):
        self.name = "Bishop"

        Piece.__init__(self, color, 3, location)


class Knight(Piece):

    def __init__(self, color, location):
        self.name = "Knight"

        Piece.__init__(self, color, 3, location)


class Pawn(Piece):
    def __init__(self, color, location):
        self.name = "Pawn"

        Piece.__init__(self, color, 1, location)
