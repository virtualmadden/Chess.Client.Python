from engine.board import Board
from engine.player import Player
from datetime import datetime
import uuid


class Game(object):
    def __init__(self, move_time=5):
        # game identifier
        self.game_id = uuid.uuid4()

        # move history
        self.move_history = []

        # timing variables
        self.start_time = datetime.utcnow()
        self.end_time = self.start_time
        self.move_time_in_minutes = move_time

        # setup game board
        self.board = Board()

        # setup players
        self.whitePlayer = Player()
        self.blackPlayer = Player()
