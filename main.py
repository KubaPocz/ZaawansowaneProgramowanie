from fastapi import FastAPI
import csv
from Models.Link import Link
from Models.Movie import Movie
from Models.Rating import Rating
from Models.Tag import Tag
import json

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/links")
def load_links():
    links = []

    with open("data/links.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",")

        for row in reader:
            link = Link(
                movieId=int(row["movieId"]),
                imdbId=row["imdbId"],
                tmdbId=row["tmdbId"]
            )

            links.append(link.__dict__)

    return links

@app.get("/movies")
def load_movies():
    movies = []

    with open("data/movies.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",")

        for row in reader:
            movie = Movie(
                id=int(row["movieId"]),
                title=row["title"],
                genres=row["genres"].split("|")
            )

            movies.append(movie.__dict__)

    return movies

@app.get("/ratings")
def load_ratings():
    ratings = []

    with open("data/ratings.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",")

        for row in reader:
            rating = Rating(
                userId=int(row["userId"]),
                movieId=int(row["movieId"]),
                rating=row["rating"],
                timestamp=row["timestamp"]
            )

            ratings.append(rating.__dict__)

    return ratings

@app.get("/tags")
def load_tags():
    tags = []

    with open("data/tags.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",")

        for row in reader:
            tag = Tag(
                userId=int(row["userId"]),
                movieId=int(row["movieId"]),
                tag=row["tag"],
                timestamp=row["timestamp"]
            )

            tags.append(tag.__dict__)

    return tags