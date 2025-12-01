import pandas as pd

def load_movies(path="movies.csv"):
    df = pd.read_csv(path)
    movies = []

    for row in df.itertuples(index=False):
        movies.append({
            "title": row.title,
            "duration": int(row.duration),
            "rating": float(row.rating)
        })

    return movies

if __name__ == "__main__":
    movies = load_movies()
    print("Loaded", len(movies), "movies")
    print(movies[:3])
