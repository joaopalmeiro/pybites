from typing import Union


def fizzbuzz(num: int) -> Union[str, int]:
    return (
        "Fizz" * (num % 3 == 0)
        + " " * (num % 3 == 0 and num % 5 == 0)
        + "Buzz" * (num % 5 == 0)
        or num
    )


def fizzbuzz_with_f_string(num: int) -> Union[str, int]:
    fizz = "Fizz" if num % 3 == 0 else ""
    buzz = "Buzz" if num % 5 == 0 else ""
    space = " " if fizz and buzz else ""
    return f"{fizz}{space}{buzz}" or num


print(fizzbuzz(2))
print(fizzbuzz(3))
print(fizzbuzz(5))
print(fizzbuzz(15))

print("-" * 3)

print(fizzbuzz_with_f_string(2))
print(fizzbuzz_with_f_string(3))
print(fizzbuzz_with_f_string(5))
print(fizzbuzz_with_f_string(15))
