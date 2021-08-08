"""This module plays the game Tic-Tac-Toe."""
from typing import Optional
import re
from tictactoe.board import Board
from tictactoe.player import Player
from tictactoe.minimax import minimax


def validate_response(response: str) -> Optional[str]:
    """Return an error message if the response in invalid."""
    pattern = re.compile('^[1-9q]$')
    if pattern.match(response) is None:
        return f'Invalid response: {response}'

def play(auto_A: bool = False, auto_B: bool = False):
    """Play a game with moves for each player either input or automatically generated."""
    board: Board = Board()
    player: Player = Player.A
    move_count: int = 1
    cell_number: int = 0
    print('Welcome to the Tic-Tac-Toe game!')
    while move_count <= 9:
        print(board.display())
        player_name: str = player.display()

        if player == Player.A and auto_A or player == Player.B and auto_B:
            cell_number = minimax(board, player)
            print(f'[{move_count}] Player {player_name} moved to {cell_number}.')
        else:
            response: str = input(f'[{move_count}] Player {player_name}, enter your move or q to exit): ')

            if response == 'q':
                print("Game exited.")
                break

            response_error: Optional[str] = validate_response(response)
            if response_error is not None:
                print(f'ERROR! {response_error}')
                continue

            cell_number = int(response)
            if not board.is_cell_empty(cell_number):
                print(f'ERROR! Cell number {cell_number} is not empty.')
                continue

        board = board.make_move(player, cell_number)
        if board.is_win(player):
            print(board.display())
            print(f'Congratulations, player {player_name}! You won in {move_count} moves.')
            break
        else:
            move_count += 1
            player = player.switch()
            if move_count > 9:
                print(board.display())
                print('This game has ended in a draw.')


if __name__ == '__main__':
    play()
