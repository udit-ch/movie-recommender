# Brute-force approach: try every possible subset of movies.
# This is slow, but it guarantees the correct answer for small datasets.

from typing import List, Tuple
from movies_utils import Movie

def recommend_bruteforce(movies: List[Movie], max_time: int) -> Tuple[List[Movie], float, int]:
    n = len(movies)

    best_rating = -1.0
    best_subset = []
    best_duration = 0

    # Loop over all 2^n subsets using bitmasks
    for mask in range(1 << n):
        total_time = 0
        total_rating = 0.0
        subset = []

        # Check which movies are included in this subset
        for i in range(n):
            if mask & (1 << i):
                m = movies[i]
                total_time += m.duration
                total_rating += m.rating
                subset.append(m)

        # Only consider subsets that fit within the time limit
        if total_time <= max_time:
            # Prefer higher rating; if tied, prefer lower total duration
            if (total_rating > best_rating or
               (abs(total_rating - best_rating) < 1e-9 and total_time < best_duration)):
                best_rating = total_rating
                best_subset = subset
                best_duration = total_time

    return best_subset, best_rating, best_duration