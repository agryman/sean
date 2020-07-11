# Cayley Contest
# 1997
# Question 21


def is_solution(a, b, c):
    if a * (a*b + a*c + b*c) == 11 * b * (b*c + a*b + a*c):
        return a + 2 * b + c <= 40
    else:
        False


def find_all_solutions():
    return [(a, b, c)
            for a in range(1, 40)
            for b in range(1, 40)
            for c in range(1, 40)
            if is_solution(a, b, c)]


solutions = find_all_solutions()

for s in solutions:
    print(s)

print('Number of solutions is', len(solutions))


