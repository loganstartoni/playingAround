import math
from typing import Union

debug = False


def pythagorean_theorem(
        a: Union[int, float] = None, b: Union[int, float] = None, c: Union[int, float] = None
) -> tuple[Union[int, float], Union[int, float], Union[int, float]]:
    if debug:
        print(f"debug: a={a} b={b} c={c}")
    if a and b and not c:
        if debug:
            print(f"debug: a^2={a ** 2} b^2={b ** 2}")
        return a, b, math.sqrt(a ** 2 + b ** 2)
    if a and not b and c:
        if debug:
            print(f"debug: a^2={a ** 2} c^2={c ** 2}")
        return a, math.sqrt(c ** 2 - a ** 2), c
    if not a and b and c:
        if debug:
            print(f"debug: c^2={c ** 2} b^2={b ** 2}")
        return math.sqrt(c ** 2 - b ** 2), b, c
    raise ValueError("Two Values must be present.")


if __name__ == '__main__':
    # print(pythagorean_theorem(a=3, b=4))
    # print(pythagorean_theorem(a=3, c=5))
    # print(pythagorean_theorem(b=4, c=5))
    print(pythagorean_theorem(b=10, a=15))
    print(pythagorean_theorem(a=8, b=15))
    print(pythagorean_theorem(a=5, b=12))
    print(pythagorean_theorem(a=4, b=5))

