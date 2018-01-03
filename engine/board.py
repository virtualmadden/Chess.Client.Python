from engine.piece import Piece


class Board(object):
    def on_board(self, new_location):
        if new_location[0] in range(self.number_of_rows):
            if new_location[1] in range(self.number_of_columns):
                return True
            else:
                return False
        else:
            return False

    def blocked(self, turn, new_location):
        if self.game_board[new_location] is type(Piece) and new_location.color is turn:
            return True

        return False

    def __init__(self, number_of_rows=8, number_of_columns=8):
        self.number_of_rows = number_of_rows
        self.number_of_columns = number_of_columns

        self.game_board = [x[:] for x in [["x"] * number_of_columns] * number_of_rows]
