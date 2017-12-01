from collections import namedtuple


class Piece(object):

    Location = namedtuple("Location", ["row", "column"])

    def __init__(self, name, value, row, column):
        self.name = name
        self.value = value
        self.Location(row, column)

    def move(self, row, column):
        self.Location(row, column)


class King(Piece):

    def __init__(self):
        Piece.__init__(self, "King", 10)


class Queen(Piece):

    def __init__(self):
        Piece.__init__(self, "Queen", 9)


class Rook(Piece):

    def __init__(self):
        Piece.__init__(self, "Rook", 5)


class Bishop(Piece):

    def __init__(self):
        Piece.__init__(self, "Bishop", 3)


class Knight(Piece):

    def __init__(self):
        Piece.__init__(self, "Knight", 3)


class Pawn(Piece):

    def __init__(self):
        Piece.__init__(self, "Pawn", 1)
