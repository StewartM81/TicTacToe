class Player:
    """A player object for a computerised game
    
       This class can be reused for different types of games that require
       one or more players. It stores basic identifying information
       such as the player's name and a symbol or marker.
    """

    def __init__(self, player_name, player_symbol):
        """Initialize a new player instance.

            playerName (str)     the name of the player
            symbol (str)         symbol to represent player on game board
        """
        self._player_name = player_name
        self._player_symbol = player_symbol

    def get_name(self):
        """Return the name of the player"""
        return self._player_name
    
    def get_symbol(self):
        """Return player symbol"""
        return self._player_symbol

