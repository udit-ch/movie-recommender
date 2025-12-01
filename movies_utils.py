# Simple Movie object + CSV loader

from dataclasses import dataclass
from typing import List
import csv

# Basic container for each movie entry
@dataclass(frozen=True)
class Movie:
    title: str
    duration: int
    rating: float

# Read movies from a CSV file and return a list of Movie objects
def load_movies_from_csv(path: str) -> List[Movie]:
    movies = []
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies.append(Movie(
                title=row["title"].strip(),
                duration=int(row["duration"]),
                rating=float(row["rating"])
            ))
    return movies

import time

# Small helper to measure how long a function takes to run.
def measure_time(fn, *args):
    start = time.perf_counter()
    result = fn(*args)
    end = time.perf_counter()
    return result, end - start