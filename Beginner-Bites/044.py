import secrets
import string
from itertools import repeat

ALPHABET: str = string.ascii_uppercase + string.digits


def gen_key(parts: int = 4, chars_per_part: int = 8) -> str:
    # Double underscore: https://docs.python-guide.org/writing/style/#create-an-ignored-variable
    password = "-".join(
        "".join(secrets.choice(ALPHABET) for __ in range(chars_per_part))
        for __ in range(parts)
    )
    return password


def gen_key_with_repeat(parts: int = 4, chars_per_part: int = 8) -> str:
    password = "-".join(
        "".join(secrets.choice(ALPHABET) for __ in repeat(None, chars_per_part))
        for __ in repeat(None, parts)
    )
    return password


print(gen_key())
print(gen_key_with_repeat())
