from typing import List


def load_data() -> None:
    punctuation: str = r""" """
    file = open("./input.txt", "rt")
    file = file.read().strip().translate(str.maketrans('', '', punctuation))
    data: List[int] = [int(x) for x in file.split()]
    digit_len: int = data[0]
    result: int = data[1] + data[2]
    print(" ".join(str(result)))


if __name__ == "__main__":
    load_data()
