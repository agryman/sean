"""The module represents a cell in a Tic-Tac-Toe game board."""
from typing import Optional
from tictactoe.player import Player

# A cell is either empty or contains a player.
Cell = Optional[Player]


def display_cell(c: Cell, cell_number: int) -> str:
    """Return a string that displays the cell contents."""
    symbol: str = str(cell_number) if c is None else c.display()
    return f' {symbol} '


