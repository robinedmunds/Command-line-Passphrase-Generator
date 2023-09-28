from math import ceil
import random


def die_roll(sides: int = 6) -> int:
    return ceil(
        random.random() * sides
    )


if __name__ == "__main__":
    die_roll()
