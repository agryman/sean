# 3. An integer is multiplied by 2 and the result is then multiplied by 5. The final result could be
# (A) 64 (B) 32 (C) 12 (D) 25 (E) 30

answers = [64, 32, 12, 25, 30]

def is_divisible(x):
    return (x % 2 == 0) and (x % 5 == 0)

solution = [x for x in answers if is_divisible(x)]

print('The solution is', solution)