MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    not_str = " " if age >= MIN_DRIVING_AGE else " not "
    print(f"{name} is{not_str}allowed to drive")


allowed_driving("tim", 17)
allowed_driving("bob", 18)
