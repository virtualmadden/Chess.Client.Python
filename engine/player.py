import uuid


class Player(object):
    def __init__(self):
        self.player_id = uuid.uuid4()
