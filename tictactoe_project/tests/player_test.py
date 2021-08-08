"""This module tests the Player class."""
from tictactoe.player import Player

class TestSwitch:
    def test_switch_A(self):
        assert Player.A.switch() == Player.B

    def test_switch_B(self):
        assert Player.B.switch() == Player.A

class TestDisplay:
    def test_display_A(self):
        assert Player.A.display() == 'X'

    def test_display_B(self):
        assert Player.B.display() == 'O'
