from json import dumps
from typing import Any, List, NamedTuple

import feedparser

# cached version to have predictable results for testing
FEED_URL: str = "https://bites-data.s3.us-east-2.amazonaws.com/steam_gaming.xml"

Game = NamedTuple(
    "Game",
    [
        ("title", str),
        ("link", str),
    ],
)


def jprint(d: Any, indent: int = 4) -> None:
    print(dumps(d, indent=indent))


def get_games() -> List[Game]:
    """Parses Steam's RSS feed and returns a list of Game namedtuples"""
    # or `entries = feedparser.parse(FEED_URL)["entries"]`
    entries = feedparser.parse(FEED_URL).entries

    # or `return [Game(g["title"], g["link"]) for g in entries]`
    return [Game(g.title, g.link) for g in entries]


jprint(get_games())
print(len(get_games()))
