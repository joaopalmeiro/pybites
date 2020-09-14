def get_profile(*, name: str = "julian", profession: str = "programmer") -> str:
    """
    The bare variable argument parameter `*` indicates
    that there aren’t any more positional parameters.
    """
    return f"{name} is a {profession}"
