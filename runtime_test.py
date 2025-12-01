# Runtime comparison script.
# Run with: python3 runtime_test.py
# Outputs execution time of brute-force vs DP + correctness check.
# Quick script to compare brute force vs DP runtimes.
# Also checks that both methods agree on the best rating.

from time import perf_counter
from movies_utils import load_movies_from_csv
from bruteforce_recommender import recommend_bruteforce
from dp_recommender import recommend_dp

# Helper to measure how long a function takes
def time_function(fn, *args):
    start = perf_counter()
    result = fn(*args)
    end = perf_counter()
    return result, end - start

def main():
    movies = load_movies_from_csv("datasets/movies_small.csv")
    max_time = 300  # example: 5 hours

    (bf_result, bf_t) = time_function(recommend_bruteforce, movies, max_time)
    (dp_result, dp_t) = time_function(recommend_dp, movies, max_time)

    print("Brute-force time:", bf_t, "seconds")
    print("DP time:        ", dp_t, "seconds")

    bf_movies, bf_rating, bf_duration = bf_result
    dp_movies, dp_rating, dp_duration = dp_result

    print("\nBrute-force rating:", bf_rating)
    print("DP rating:         ", dp_rating)

    # Quick correctness check
    if abs(bf_rating - dp_rating) < 1e-6:
        print("\n✓ DP matches brute force (good).")
    else:
        print("\n⚠ DP does NOT match brute force (problem).")

if __name__ == "__main__":
    main()