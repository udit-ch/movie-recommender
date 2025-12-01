# Simple wrapper API for the full movie recommendation pipeline.
# This lets other team members call one function instead of dealing with
# DP/bruteforce imports directly.

from movies_utils import load_movies_from_csv
from bruteforce_recommender import recommend_bruteforce
from dp_recommender import recommend_dp

def get_best_movies(csv_path: str, max_time: int, method: str = "dp"):
    """
    Wrapper function to compute the best movie set.
    
    method = "dp" (default) or "bruteforce"
    """
    movies = load_movies_from_csv(csv_path)

    if method == "dp":
        return recommend_dp(movies, max_time)
    elif method == "bruteforce":
        return recommend_bruteforce(movies, max_time)
    else:
        raise ValueError("method must be 'dp' or 'bruteforce'")
