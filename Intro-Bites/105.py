from typing import List

text = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""


def slice_and_dice(text: str = text) -> List[str]:
    """Get a list of words from the passed in text.
       See the Bite description for step by step instructions"""
    results = []

    text_strip = text.strip()
    text_split = text_strip.split("\n")

    for l in text_split:
        line = l.lstrip()
        if line[0].islower():
            last_word = line.split()[-1]
            result_word = last_word.rstrip("!.")
            results.append(result_word)

    return results


# print(slice_and_dice(text))
