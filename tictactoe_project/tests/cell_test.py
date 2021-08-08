"""This module tests the cell module."""
from tictactoe.player import Player
from tictactoe.cell import Cell, display_cell

class TestDisplayCell:
    def test_display_A_1(self):
        assert display_cell(Player.A, 1) == ' X '

    def test_display_B_2(self):
        assert display_cell(Player.B, 2) == ' O '

    def test_display_empty_3(self):
        assert display_cell(None, 3) == ' 3 '
