"""The modules represents a Tic-Tac-Toe game player."""
from enum import Enum, unique

@unique
class Player(Enum):
    """Tic tac toe is a 2-person game so define the two players. Player A moves first."""
    A = 0
    B = 1

    def display(self) -> str:
        """Return X for player A and O for player B."""
        return 'XO'[self.value]

    def switch(self) -> 'Player':
        """Return the other player."""
        return Player(1 - self.value)
