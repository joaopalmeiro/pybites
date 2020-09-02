from datetime import datetime, timedelta

NOW = datetime.now()


class Promo:
    def __init__(self, name: str, expires: datetime) -> None:
        self.name = name
        self.expires = expires

    @property
    def expired(self) -> bool:
        return NOW > self.expires


past_time = NOW - timedelta(seconds=3)
promo = Promo("promo", past_time)
print(promo.expired)
