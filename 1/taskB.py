# 85057872
import re
from collections import Counter


def count_score(data: str, max_click: int) -> None:
    result: int = 0
    counts: Counter = Counter(data)
    for character, count in counts.most_common():
        if count <= max_click:
            result += 1
    print(result)


def load_data() -> None:
    punctuation: str = r'|\.||\n|'
    file = open('./input.txt', 'rt')
    max_click: int = int(file.read(1)) * 2
    data: str = re.sub(punctuation, '', file.read())
    count_score(data, max_click)


if __name__ == '__main__':
    load_data()
