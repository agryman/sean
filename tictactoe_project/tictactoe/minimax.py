"""This module implements a minimax search for Tic-Tac-Toe."""
from typing import Optional
from tictactoe.player import Player
from tictactoe.board import Board

score_memo: dict[Board, int] = dict()

MAX_SCORE = 1
DRAW_SCORE = 0
MIN_SCORE = -1

def representative(board: Board) -> Board:
    """Return the representative of the orbit of board under the symmetry operations."""
    # TODO: Reduce the search space by exploiting the symmetry of the score function.
    # Select as representative the board with the smallest hash.
    # Apply all elements of the symmetry group to board, compute their hashes,
    # and select the board that has the smallest hash.
    return board

def score(board: Board) -> int:
    """Return the score of the board."""
    board = representative(board)
    if board in score_memo:
        return score_memo[board]

    if board.is_win(Player.A):
        score_memo[board] = MAX_SCORE
        return score_memo[board]

    if board.is_win(Player.B):
        score_memo[board] = MIN_SCORE
        return score_memo[board]

    player: Player = board.who_moves()
    moves: list[Board] = board.moves_by_player(player)
    if len(moves) == 0:
        score_memo[board] = DRAW_SCORE
        return score_memo[board]

    optimal_score: int = score(moves[0])
    for move in moves[1:]:
        if player == Player.A:
            if optimal_score == MAX_SCORE:
                break
            optimal_score = max(optimal_score, score(move))
        else:
            if optimal_score == MIN_SCORE:
                break
            optimal_score = min(optimal_score, score(move))

    score_memo[board] = optimal_score
    return score_memo[board]

def minimax(start: Board, player: Player) -> int:
    """Return the cell number of an automatically generated move."""
    moves: list[Board] = start.moves_by_player(player)
    assert len(moves) > 0

    optimal_move: Optional[Board] = None
    for move in moves:
        if score(move) == score(start):
            optimal_move = move
            break
    assert optimal_move is not None
    assert score(optimal_move) == score(start)

    cell_number: int = start.cell_number_of_move(move)
    assert move.value_at_cell_number(cell_number) == player

    return cell_number
