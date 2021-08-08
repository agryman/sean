"""This module represents a Tic-Tac-Toe board."""
from typing import NamedTuple
from tictactoe.cell import Cell
from tictactoe.row import Row
from tictactoe.player import Player


# A triple of cell numbers.
Triple = tuple[int, int, int]

# The list of triples that correspond to cell numbers in each row of a board.
cell_numbers: list[Triple] = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9)
    ]

# The list of triples that correspond to the cell numbers of each winning cell combination in a board.
wins: list[Triple] = [
        (1, 2, 3),
        (4, 5, 6),
        (7, 8, 9),
        (1, 4, 7),
        (2, 5, 8),
        (3, 6, 9),
        (1, 5, 9),
        (3, 5, 7)
    ]


def cell_indices(cell_number: int) -> tuple[int, int]:
    """Return the row and column index tuple (i, j) corresponding to a cell number."""
    if cell_number < 1 or cell_number > 9:
        raise ValueError(f'cell number must be between 1 and 9: {cell_number}')

    i: int = (cell_number - 1) // 3
    j: int = (cell_number - 1) % 3

    return i, j


class Board(NamedTuple):
    """A Board is a named tuple of 3 rows arranged from top to bottom."""
    top: Row = Row()
    middle: Row = Row()
    bottom: Row = Row()

    def display(self) -> str:
        """Return a string that displays the board."""
        separator: str = '\n---+---+---\n'
        return separator.join([self[i].display(cell_numbers[i]) for i in range(3)])

    def override(self, r: int, v: Row) -> 'Board':
        """Return a new board in which row r is replaced by the value v."""
        return Board(*[v if i == r else self[i] for i in range(3)])

    def moves_by_player(self, player: Player) -> list['Board']:
        """Return the list of all boards that result from the player making one move in this board."""
        return [self.override(i, row)
                for i in range(3)
                for row in self[i].moves_by_player(player)]

    def value_at_cell_number(self, cell_number: int) -> Cell:
        """Return the value of the board at the cell number."""
        i, j = cell_indices(cell_number)
        return self[i][j]

    def is_cell_empty(self, cell_number: int) -> bool:
        """Return True if and only if the cell is empty."""
        return self.value_at_cell_number(cell_number) is None

    def is_win(self, player: Player) -> bool:
        """Return True if and only if the player has won the game."""
        for win in wins:
            if all([player == self.value_at_cell_number(cell_number) for cell_number in win]):
                return True
        return False

    def make_move(self, player: Player, cell_number: int) -> 'Board':
        """Return the new board that results when the player moves to the cell."""
        i, j = cell_indices(cell_number)
        row: Row = self[i].override(j, player)
        return self.override(i, row)

    def player_count(self, player: Player) -> int:
        """Return the number of cells occupied by the player."""
        return sum([cell == player for row in self for cell in row ])

    def who_moves(self) -> Player:
        """Return the player who moves from this position."""
        return Player.A if self.player_count(Player.A) <= self.player_count(Player.B) else Player.B

    def cell_number_of_move(self, move: 'Board') -> int:
        """Return the cell number of the cell where move differs from the board."""
        for cell_number in range(1, 10):
            if self.value_at_cell_number(cell_number) != move.value_at_cell_number(cell_number):
                return cell_number
        assert False
