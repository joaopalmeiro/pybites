def countdown_for(start: int = 10) -> None:
    for i in reversed(range(1, start + 1)):
        print(i)
    print("time is up")


def countdown_recursive(start: int = 10) -> None:
    if start == 0:
        print("time is up")
    else:
        print(start)
        countdown_recursive(start - 1)


def countdown_recursive_solution(start: int = 10) -> None:
    print(start)
    if start == 1:
        print("time is up")
    else:
        return countdown_recursive(start - 1)


countdown_for()
print("-" * 3)
countdown_recursive()
print("-" * 3)
countdown_recursive_solution()
