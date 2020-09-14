import textwrap
from pprint import pprint

INDENTS: int = 4

# part of William Shakespeare's play Hamlet
shakespeare_unformatted: str = """
                          To be, or not to be, that is the question:
                          Whether 'tis nobler in the mind to suffer

                          The slings and arrows of outrageous fortune,
                          Or to take Arms against a Sea of troubles,
                          """

# part of Remember, by Christina Rosetti
rosetti_unformatted: str = """
                      Remember me when I am gone away,
                      Gone far away into the silent land;
                      When you can no more hold me by the hand,

                      Nor I half turn to go yet turning stay.

                      Remember me when no more day by day
                      You tell me of our future that you planned:
                      Only remember me; you understand
                      """


def print_hanging_indents(poem: str) -> None:
    for part in poem.split("\n\n"):
        lines = [textwrap.dedent(line) for line in part.splitlines() if line.strip()]

        for idx, line in enumerate(lines):
            print(textwrap.indent(line, " " * INDENTS * (idx > 0)))


def print_hanging_indents_solution(poem: str) -> None:
    for part in poem.split("\n\n"):
        lines = [line.strip() for line in part.splitlines() if line.strip()]

        print(lines[0])

        for line in lines[1:]:
            print(" " * INDENTS + line)


pprint(shakespeare_unformatted.splitlines(True))
pprint(textwrap.dedent(shakespeare_unformatted).splitlines(True))
pprint(list(map(textwrap.dedent, shakespeare_unformatted.splitlines())))

print("-" * 3)

print_hanging_indents_solution(shakespeare_unformatted)
print("-" * 1)
print_hanging_indents_solution(rosetti_unformatted)

print("-" * 3)

print_hanging_indents(shakespeare_unformatted)
print("-" * 1)
print_hanging_indents(rosetti_unformatted)
