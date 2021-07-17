"""This module solves the knight move problem on a four by four board."""

n = 4
column_names = 'abcd'
column_numbers = list(range(n))
rows_numbers = list(range(n))


def new_board_dict():
    """Return a new empty game board as a dict."""
    return {(row, column): False for row in rows_numbers for column in column_numbers}


def new_board_list():
    """Return a new empty game board as a list of rows."""
    return [[False] * n] * n
