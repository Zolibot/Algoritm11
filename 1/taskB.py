# 84981423
import re
from collections import Counter


def load_data() -> None:
    punctuation: str = '|\.||\n|'
    file = open('./input.txt', 'rt')
    max_click: int = int(file.read(1)) * 2
    data: str = re.sub(punctuation, '', file.read())
    result: int = 0
    counts: Counter = Counter(data)
    for character, count in counts.most_common():
        if count <= max_click:
            result += 1
    print(result)


if __name__ == '__main__':
    load_data()
