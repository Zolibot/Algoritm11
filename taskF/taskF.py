def is_palindrome(words: str) -> bool:
    return words == words[::-1]


def load_data() -> None:
    punctuation: str = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """
    file = open("/run/media/greger/Disk_E/GRENOW/Dev/sprints/Algoritms/taskF/input.txt", "rt")
    data: str = file.read()
    data = data.strip().translate(str.maketrans('', '', punctuation)).lower()
    print(data)
    print(is_palindrome(data))


import timeit

print(timeit.timeit("load_data()", number=1000, setup="from taskF import load_data"))


if __name__ == '__main__':
    load_data()

