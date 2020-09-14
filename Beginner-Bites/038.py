import xml.etree.ElementTree as ET
from typing import Iterator

# from OMDB (https://www.omdbapi.com/)
xmlstring = """<?xml version="1.0" encoding="UTF-8"?>
<root response="True">
  <movie title="The Prestige" year="2006" rated="PG-13" released="20 Oct 2006" runtime="130 min" genre="Drama, Mystery, Sci-Fi" director="Christopher Nolan" />
  <movie title="The Dark Knight" year="2008" rated="PG-13" released="18 Jul 2008" runtime="152 min" genre="Action, Crime, Drama" director="Christopher Nolan" />
  <movie title="The Dark Knight Rises" year="2012" rated="PG-13" released="20 Jul 2012" runtime="164 min" genre="Action, Thriller" director="Christopher Nolan" />
  <movie title="Dunkirk" year="2017" rated="PG-13" released="21 Jul 2017" runtime="106 min" genre="Action, Drama, History" director="Christopher Nolan" />
  <movie title="Interstellar" year="2014" rated="PG-13" released="07 Nov 2014" runtime="169 min" genre="Adventure, Drama, Sci-Fi" director="Christopher Nolan"/>
</root>"""


def get_tree() -> ET.Element:  # or `ET.ElementTree`
    """You probably want to use ET.fromstring"""
    return ET.fromstring(
        xmlstring
    )  # or `return ET.ElementTree(ET.fromstring(xmlstring))`


def get_movies() -> Iterator[str]:
    """Call get_tree and retrieve all movie titles, return a list or generator"""
    for movie in get_tree().iter(tag="movie"):
        yield movie.attrib["title"]


def _get_runtime(m: ET.Element) -> int:
    return int(m.attrib["runtime"].rstrip(" min"))


def get_movie_longest_runtime() -> str:
    """Call get_tree again and return the movie title for the movie with the longest
    runtime in minutes, for latter consider adding a _get_runtime helper"""
    movies = get_tree().iter(tag="movie")
    return max(movies, key=_get_runtime).attrib["title"]


print(get_tree())
print(type(get_tree()))
print(len(list(get_tree().iter(tag="movie"))))

print("-" * 3)

print(list(get_movies()))

print("-" * 3)

print(get_movie_longest_runtime())
