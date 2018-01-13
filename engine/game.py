from engine.board import Board
from engine.player import Player
from datetime import datetime
import uuid


class Game(object):
    def end_game(self):
        self.end_time = datetime.utcnow()
        self.game_time = self.end_time - self.start_time

    def __init__(self, move_time=300000):
        # game identifier
        self.game_id = uuid.uuid4()

        # move history
        self.move_history = []

        # timing variables
        self.start_time = datetime.utcnow()
        self.end_time = None
        self.game_time = None
        self.max_move_time = move_time

        # setup game board
        self.board = Board()

        # setup players
        self.whitePlayer = Player("white")
        self.blackPlayer = Player("black")
