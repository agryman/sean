"""This module represents a row of a Tic-Tac-Toe game board."""
from typing import NamedTuple
from tictactoe.player import Player
from tictactoe.cell import Cell, display_cell


class Row(NamedTuple):
    """A board contains rows. A Row is a named tuple of 3 cells arranged from left to right."""
    left: Cell = None
    centre: Cell = None
    right: Cell = None

    def display(self, n: tuple[int, int, int]) -> str:
        """Return a string that displays the row."""
        separator: str = '|'
        return separator.join([display_cell(self[i], n[i]) for i in range(3)])

    def override(self, c: int, v: Cell) -> 'Row':
        """Return a new row in which the contents of cell c is replaced by the value v."""
        return Row(*[v if i == c else self[i] for i in range(3)])

    def moves_by_player(self, player: Player) -> list['Row']:
        """Return the list of all rows that result from the player making one move in this row."""
        moves: list[Row] = []
        for c in range(3):
            if self[c] is None:
                moves.append(self.override(c, player))
        return moves
