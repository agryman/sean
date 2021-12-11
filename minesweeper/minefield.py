"""This module implements the minefield portion of the minesweeper game."""

from typing import ClassVar


class Cell:
    """A cell is a location in a minefield.
    A cell has row and column coordinates.
    A cell may or may not contain a mine.
    A cell contains a number that counts how many mines are adjacent to it.
    A cell may or may not have a flag on it.
    A cell may or may not be hidden.
    """

    row: int
    column: int
    has_mine: bool
    adjacent_mine_count: int
    has_flag: bool
    is_hidden: bool

    def __init__(self, row: int, column: int, has_mine: bool):
        self.row = row
        self.column = column
        self.has_mine = has_mine
        self.adjacent_mine_count = -1
        self.has_flag = False
        self.is_hidden = True


class Minefield:
    """A minefield is a rectangle that holds mines and flags.
    Each cell is either hidden or exposed.
    An exposed cell displays the number of mines adjacent to it.
    If the user exposes a cell that contains a mine, the game is over.
    The game ends when all the mines and only the mines are flagged,
    and all the empty cells are exposed.
    """

    width: int

    height: int

    MIN_WIDTH: ClassVar[int] = 10
    MAX_WIDTH: ClassVar[int] = 24

    MIN_HEIGHT: ClassVar[int] = 8
    MAX_HEIGHT: ClassVar[int] = 20

    rows: list[list[Cell]]

    def __init__(self, width: int = None, height: int = None):
        if width is None:
            width = self.MIN_WIDTH
        if height is None:
            height = self.MIN_HEIGHT

        if width < self.MIN_WIDTH:
            raise ValueError(f'width: {width} is below minimum: {self.MIN_WIDTH}')
        if width > self.MAX_WIDTH:
            raise ValueError(f'width: {width} is above maximum: {self.MAX_WIDTH}')

        if height < self.MIN_HEIGHT:
            raise ValueError(f'height: {height} is below minimum: {self.MIN_HEIGHT}')
        if height > self.MAX_HEIGHT:
            raise ValueError(f'height: {height} is below maximum: {self.MAX_HEIGHT}')

        self.width = width
        self.height = height

        self.rows = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                has_mine = False  # figure this our later
                cell = Cell(i, j, has_mine)
                row.append(cell)
            self.rows.append(row)
