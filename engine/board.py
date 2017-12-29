from engine.state import State


class Board(object):
    def create_board(self):
        self.initialize_piece_counts()

    @staticmethod
    def initialize_piece_counts():
        State.reset_pieces()

