from typing import List


def digit_fact(digit: int) -> list[int]:
    data: List[int] = []
    i = 2
    while i * i <= digit:
        while digit % i == 0:
            data.append(i)
            digit /= i
        i += 1
    if digit > 1:
        data.append(digit)
    return data


def load_data() -> None:
    digit = int(input())
    print(" ".join(map(str, digit_fact(digit))))


if __name__ == "__main__":
    load_data()
