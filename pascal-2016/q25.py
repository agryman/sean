"""
2016 Pascal Contest
Question 25
"""
rows = [(x,y,z) for x in [0, 1] for y in [0, 1] for z in [0, 1]]

def is_good_row(row):
    return 0 in row and 1 in row

good_rows = [r for r in rows if is_good_row(r)]

boards = [(r1,r2,r3) for r1 in good_rows for r2 in good_rows for r3 in good_rows]

def is_good_board(board):
    r1 = board[0]
    r2 = board[1]
    r3 = board[2]
    c1 = (r1[0], r2[0], r3[0])
    c2 = (r1[1], r2[1], r3[1])
    c3 = (r1[2], r2[2], r3[2])
    return is_good_row(c1) and is_good_row(c2) and is_good_row(c3)

good_boards = [b for b in boards if is_good_board(b)]

print(len(good_boards))