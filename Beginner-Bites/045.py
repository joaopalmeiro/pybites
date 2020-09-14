from collections import deque
from typing import Deque


def my_queue(n: int = 5) -> Deque[int]:  # or `Deque`
    return deque(maxlen=n)  # Empty deque


if __name__ == "__main__":
    mq = my_queue()
    for i in range(10):
        mq.append(i)
        print((i, list(mq)))
