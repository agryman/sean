"""This module solves Cayley 2021, problem 23."""

import math

def compute_all_turns():
    """Return a dict whose keys are the three rolls of the special die and
    whose values are score and relative probability."""

    return {(r1, r2, r3): (r1 + r2 + r3, r1 * r2 * r3)
            for r1 in range(1, 7)
            for r2 in range(1, 7)
            for r3 in range(1, 7)}


turns = compute_all_turns()

# Robbie scores 8 after the first 2 rolls
robbie_8 = [rolls for rolls in turns if rolls[0] + rolls[1] == 8]

# Francis scores 10 after the first 2 rolls
francine_10 = [rolls for rolls in turns if rolls[0] + rolls[1] == 10]

# All possible games where the score is 8 to 10 after the first 2 rolls of each player
games_8_10 = [(r, f) for r in robbie_8 for f in francine_10]

# The total relative probabilty of these games
total_relative_probability_8_10 = sum([turns[r][1] * turns[f][1] for (r, f) in games_8_10])

# The games that Robbie goes on to win
games_robbie_wins = [(r, f) for (r, f) in games_8_10 if turns[r][0] > turns[f][0]]

# The relative probability of the games Robbie wins
robbie_wins_relative_probability = sum([turns[r][1] * turns[f][1] for (r, f) in games_robbie_wins])

# The probability as a floating point number
robbie_wins_probability = robbie_wins_relative_probability / total_relative_probability_8_10

# Reduce this probability to a fraction in lower terms

# find the greatest common divisor of robbie_wins_relative_probability and total_relative_probability_8_10
gcd = math.gcd(robbie_wins_relative_probability, total_relative_probability_8_10)

r = robbie_wins_relative_probability // gcd

s_400 = total_relative_probability_8_10 // gcd

s = s_400 - 400

answer = r + s

