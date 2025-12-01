# Dynamic programming version using the 0/1 knapsack idea.
# Much faster than brute force for larger datasets.

from typing import List, Tuple
from movies_utils import Movie

def recommend_dp(movies: List[Movie], max_time: int) -> Tuple[List[Movie], float, int]:
    n = len(movies)

    # dp[i][t] = best rating using first i movies with time limit t
    dp = [[0.0] * (max_time + 1) for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        movie = movies[i - 1]
        dur = movie.duration
        rate = movie.rating

        for t in range(max_time + 1):
            # Skip the movie
            best = dp[i - 1][t]

            # Take the movie if it fits
            if dur <= t:
                candidate = dp[i - 1][t - dur] + rate
                if candidate > best:
                    best = candidate

            dp[i][t] = best

    # Backtrack to find which movies were chosen
    chosen = []
    t = max_time

    for i in range(n, 0, -1):
        # If value changed, the movie was taken
        if dp[i][t] != dp[i - 1][t]:
            movie = movies[i - 1]
            chosen.append(movie)
            t -= movie.duration

    chosen.reverse()

    total_duration = sum(m.duration for m in chosen)
    total_rating = sum(m.rating for m in chosen)

    return chosen, total_rating, total_duration