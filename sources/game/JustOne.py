# Description: JustOne implementation


class JustOne:
    """Environment that manage the game

    Attributes
    ---
        - self.players (List[callable]): list of callable objects

    Methods
    ---

    """

    def __init__(self, players: list):
        """Initialisation of the game

        Params
        ---
            - players (list): list of players

        Raise
        ---
            -

        Usage
        ---
            >> game = JustOne([])
        """
        self.players: list = players
