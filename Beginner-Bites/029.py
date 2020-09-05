from itertools import filterfalse, tee
from string import ascii_letters, digits
from typing import Callable, Iterable, Iterator, List, Tuple, Union


def partition(
    predicate: Callable[..., bool], iterable: Iterable
) -> Tuple[Iterator, Iterator]:
    """Source: https://docs.python.org/3/library/itertools.html#itertools-recipes"""
    t1, t2 = tee(iterable)
    return filterfalse(predicate, t1), filter(predicate, t2)


def is_alphanumeric(char: str) -> bool:
    return char.isalnum()


def get_index_different_char(chars: List[Union[str, int]]) -> int:  # or `chars: list`
    chars = list(map(str, chars))
    non_alnum, alnum = map(list, partition(is_alphanumeric, chars))

    diff = non_alnum[0] if len(non_alnum) == 1 else alnum[0]

    return chars.index(str(diff))


alphanumeric_chars: List[str] = list(ascii_letters + digits)


def get_index_different_char_solution(
    chars: List[Union[str, int]]
) -> int:  # or `chars: list`
    matches, no_matches = [], []
    for idx, char in enumerate(chars):
        if str(char) in alphanumeric_chars:
            matches.append(idx)
        else:
            no_matches.append(idx)
    return matches[0] if len(matches) == 1 else no_matches[0]


print(get_index_different_char(["A", "f", ".", "Q", 2]))
print(get_index_different_char([".", "{", " ^", "%", "a"]))
print(get_index_different_char(["=", "=", "", "/", "/", 9, ":", ";", "?", "¡"]))

print("-" * 3)

print(get_index_different_char_solution(["A", "f", ".", "Q", 2]))
print(get_index_different_char_solution([".", "{", " ^", "%", "a"]))
print(
    get_index_different_char_solution(["=", "=", "", "/", "/", 9, ":", ";", "?", "¡"])
)
