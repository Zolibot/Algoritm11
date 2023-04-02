from typing import Tuple


def get_(a: int, b: int, c: int) -> str:
    if a % 2 == b % 2 == c % 2:
        return "WIN"

    return "FAIL"


def read_input() -> Tuple[int, int, int]:
    a, b, c = map(int, input().split())
    return a, b, c


def print_result(result: int) -> None:
    print(result)


a, b, c = read_input()
print_result(calc_func(a, b, c))
