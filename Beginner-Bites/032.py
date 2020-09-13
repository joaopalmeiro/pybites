from copy import deepcopy
from typing import List, TypedDict

Item = TypedDict("Item", {"id": int, "name": str, "value": int})


# or `List[Dict[str, Union[int, str]]]`
items: List[Item] = [
    {"id": 1, "name": "laptop", "value": 1000},
    {"id": 2, "name": "chair", "value": 300},
    {"id": 3, "name": "book", "value": 20},
]


def duplicate_items(items):
    return deepcopy(items)  # `items[:]` makes a shallow copy


print(duplicate_items(items))
