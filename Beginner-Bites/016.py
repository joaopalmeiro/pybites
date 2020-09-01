from calendar import isleap
from datetime import datetime, timedelta
from itertools import islice
from pprint import pprint
from typing import Generator

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates() -> Generator[datetime, None, None]:
    one_hundred_days = 100
    one_year = 365

    while True:
        if one_hundred_days < one_year:
            yield PYBITES_BORN + timedelta(days=one_hundred_days)
            one_hundred_days += 100
        else:
            birthday = PYBITES_BORN + timedelta(days=one_year)
            yield birthday
            one_year += 366 if isleap(birthday.year + 1) else 365


dates = list(islice(gen_special_pybites_dates(), 20))
pprint(dates)
