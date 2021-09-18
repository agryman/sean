def solve():
    solutions = [(a, b, c, d)
                 for a in range(10)
                 for b in range(10)
                 for c in range(10)
                 for d in range(10)
                 if a < b < c < d and
                 (a + b + c + d) % 3 == 0]
    return len(solutions)


print(solve())
