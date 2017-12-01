class State(object):
    start_time = 0
    end_time = 0
    total_time = 5

    move_hist = []

    moves = 0
    turn = ''

    w_king = 0
    w_queen = 0
    w_rook = 0
    w_bishop = 0
    w_knight = 0
    w_pawn = 0

    b_king = 0
    b_queen = 0
    b_rook = 0
    b_bishop = 0
    b_knight = 0
    b_pawn = 0

    def reset_pieces(self):
        self.w_king = 1
        self.
