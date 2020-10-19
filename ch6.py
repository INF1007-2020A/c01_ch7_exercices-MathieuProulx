from collections import Counter


def histogram(string: str) -> dict:
    return dict(Counter(string))
