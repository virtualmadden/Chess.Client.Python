from engine.state import State

class Square(object):
    @staticmethod
    def on_board(row, col):
        if row in range(8):
            if col in range(8):
                return True
            else:
                return False
        else:
            return False

    @staticmethod
    def blocked(row, col):
        if State.turn == 'b':
            if boar
