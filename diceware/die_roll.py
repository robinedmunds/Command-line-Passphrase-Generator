from random import choice


def die_roll():
    die_values = range(1, 7)
    return choice(die_values)


if __name__ == "__main__":
    die_roll()
