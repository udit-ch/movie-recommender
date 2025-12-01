from load_movies import load_movies
from dp_recommender import recommend_dp
from bruteforce_recommender import recommend_bruteforce
import time

movies = load_movies()

time_limits = [120, 180, 240, 300]

for limit in time_limits:
    print("\n======== TIME LIMIT:", limit, "minutes ========")

    # Test DP
    start = time.time()
    dp_result = recommend_dp(movies, limit)
    dp_time = time.time() - start

    # Test brute force
    start = time.time()
    bf_result = recommend_bruteforce(movies, limit)
    bf_time = time.time() - start

    print("Dynamic Programming:")
    print("  Total Rating:", dp_result["total_rating"])
    print("  Total Duration:", dp_result["total_duration"])
    print("  Time:", dp_time, "seconds")

    print("\nBrute Force:")
    print("  Total Rating:", bf_result["total_rating"])
    print("  Total Duration:", bf_result["total_duration"])
    print("  Time:", bf_time, "seconds")
