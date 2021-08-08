"""This module tests the row module."""
from tictactoe.player import Player
from tictactoe.row import Row

class TestOverride:
    def test_empty_0_A(self):
        row: Row = Row()
        new_row: Row = row.override(0, Player.A)
        assert new_row == Row(Player.A, None, None)

    def test_AAA_1_B(self):
        row: Row = Row(Player.A, Player.A, Player.A)
        new_row: Row = row.override(1, Player.B)
        assert new_row == Row(Player.A, Player.B, Player.A)

class TestMovesByPlayer:
    def test_empty_A(self):
        row: Row = Row()
        moves: list[Row] = row.moves_by_player(Player.A)
        assert len(moves) == 3
        assert Row(Player.A, None, None) in moves
        assert Row(None, Player.A, None) in moves
        assert Row(None, None, Player.A) in moves

    def test_AAA_A(self):
        row: Row = Row(Player.A, Player.A, Player.A)
        moves: list[Row] = row.moves_by_player(Player.A)
        assert len(moves) == 0

    def test_A_B(self):
        row: Row = Row(Player.A, None, None)
        moves: list[Row] = row.moves_by_player(Player.B)
        assert len(moves) == 2
        assert Row(Player.A, Player.B, None) in moves
        assert Row(Player.A, None, Player.B) in moves
