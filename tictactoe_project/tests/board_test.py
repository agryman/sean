"""This module tests the board module."""
import pytest
from tictactoe.player import Player
from tictactoe.row import Row
from tictactoe.board import Board, cell_indices

class TestCellIndices:
    def test_fail(self):
        with pytest.raises(ValueError):
            cell_indices(0)
        with pytest.raises(ValueError):
            cell_indices(10)

    def test_ok(self):
        assert cell_indices(1) == (0, 0)
        assert cell_indices(2) == (0, 1)
        assert cell_indices(5) == (1, 1)
        assert cell_indices(7) == (2, 0)
        assert cell_indices(9) == (2, 2)

class TestPlayerCount:
    def test_empty(self):
        board: Board = Board()
        assert board.player_count(Player.A) == 0
        assert board.player_count(Player.B) == 0

    def test_ABA(self):
        board: Board = Board(Row(Player.A, Player.B, Player.A))
        assert board.player_count(Player.A) == 2
        assert board.player_count(Player.B) == 1

class TestWhoMoves:
    def test_empty(self):
        board: Board = Board()
        assert board.who_moves() == Player.A

    def test_A_1(self):
        row: Row = Row(Player.A)
        board: Board = Board(row)
        assert board.who_moves() == Player.B

    def test_BA_89(self):
        empty_row: Row = Row()
        row: Row = Row(None, Player.B, Player.A)
        board: Board = Board(empty_row, empty_row, row)
        assert board.who_moves() == Player.A
