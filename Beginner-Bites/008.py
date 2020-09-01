from collections import deque


def rotate(string: str, n: int) -> str:
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    characters = deque(string)
    characters.rotate(-n)

    return "".join(characters)


print(rotate("hello", 2))
print(rotate("hello", -2))
