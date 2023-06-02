import math
import random

def die_roll():
    return math.ceil(
        random.random() * 6
    )

if __name__ == "__main__":
    die_roll()
