from itertools import chain
from typing import Dict, List

cars: Dict[str, List[str]] = {
    "Ford": ["Falcon", "Focus", "Festiva", "Fairlane"],
    "Holden": ["Commodore", "Captiva", "Barina", "Trailblazer"],
    "Nissan": ["Maxima", "Pulsar", "350Z", "Navara"],
    "Honda": ["Civic", "Accord", "Odyssey", "Jazz"],
    "Jeep": ["Grand Cherokee", "Cherokee", "Trailhawk", "Trackhawk"],
}


def get_all_jeeps(cars: Dict[str, List[str]] = cars) -> str:
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    return ", ".join(cars["Jeep"])


def get_first_model_each_manufacturer(cars: Dict[str, List[str]] = cars) -> List[str]:
    """return a list of matching models (original ordering)"""
    return [manufacturer_cars[0] for manufacturer_cars in cars.values()]


def get_all_matching_models(
    cars: Dict[str, List[str]] = cars, grep: str = "trail"
) -> List[str]:
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    return sorted(
        [
            car
            for car in chain.from_iterable(cars.values())
            if grep.casefold() in car.casefold()
        ]
    )


def sort_car_models(cars: Dict[str, List[str]] = cars) -> Dict[str, List[str]]:
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    return {k: sorted(v) for (k, v) in cars.items()}


print(get_all_jeeps())
print(get_first_model_each_manufacturer())
print(get_all_matching_models())
print(get_all_matching_models(grep="CO"))
print(sort_car_models())

print(sum(cars.values(), []))  # Alternative to flatten a list of lists
