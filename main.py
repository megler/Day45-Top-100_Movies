# topMovies.py
#
# Python Bootcamp Day 45 - Top 100 Movies
# Usage:
#      Using Beaufitul Soup, scrape Rotten Tomatoes and create text file with
# the top 100 movies to watch.
#
# Marceia Egler December 22, 2021

from bs4 import BeautifulSoup
import requests


r = requests.get("https://www.rottentomatoes.com/top/bestofrt/")
movies_webpage = r.text
soup = BeautifulSoup(movies_webpage, "html.parser")
table = soup.find("table", "table")
movies = table.findAll("a")

with open("movies.txt", "w") as f:
    for i, movie in enumerate(movies, 1):
        f.write(f"{i}) {movie.text.lstrip()}\n")
