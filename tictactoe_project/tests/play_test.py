"""This module tests the play module."""
from tictactoe.play import validate_response

class TestValidateResponse:
    def test_q(self):
        message = validate_response('q')
        assert message is None

    def test_qq(self):
        message = validate_response('qq')
        assert message is not None

    def test_Q(self):
        message = validate_response('Q')
        assert message is not None

    def test_0(self):
        message = validate_response('0')
        assert message is not None

    def test_cell_number(self):
        for response in '123456789':
            message = validate_response(response)
            assert message is None
