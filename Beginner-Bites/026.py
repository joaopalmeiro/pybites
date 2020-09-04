from json import dumps
from typing import Dict, Set

bites: Dict[int, str] = {
    6: "PyBites Die Hard",
    7: "Parsing dates from logs",
    9: "Palindromes",
    10: "Practice exceptions",
    11: "Enrich a class with dunder methods",
    12: "Write a user validation function",
    13: "Convert dict in namedtuple/json",
    14: "Generate a table of n sequences",
    15: "Enumerate 2 sequences",
    16: "Special PyBites date generator",
    17: "Form teams from a group of friends",
    18: "Find the most common word",
    19: "Write a simple property",
    20: "Write a context manager",
    21: "Query a nested data structure",
}
exclude_bites: Set[int] = {6, 10, 16, 18, 21}


def print_dict(d: dict) -> None:
    print(dumps(d, indent=4))


def filter_bites(
    bites: Dict[int, str] = bites, bites_done: Set[int] = exclude_bites
) -> Dict[int, str]:
    """return the bites dict with the exclude_bites filtered out"""
    return {k: v for (k, v) in bites.items() if k not in bites_done}


print_dict(filter_bites())
print(len(filter_bites()))