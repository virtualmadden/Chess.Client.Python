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
        self.w_king = self.b_king = 1
        self.w_queen = self.b_queen = 1
        self.w_rook = self.b_rook = 2
        self.w_bishop = self.b_bishop = 2
        self.w_knight = self.b_knight = 2
        self.w_pawn = self.b_pawn = 8
