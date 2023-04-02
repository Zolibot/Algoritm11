def is_palindrome(words):
    max_index = len(words) - 1
    for i in range(len(words)):
        if words[i] == words[max_index]:
            if i == max_index or i > max_index:
                return True
            max_index -= 1
        else:
            return False


def load_data() -> None:
    punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ """
    file = open("/run/media/greger/Disk_E/GRENOW/Dev/sprints/Algoritms/taskF/input.txt", "rt")
    data = file.read()
    data = data.strip().translate(str.maketrans('', '', punctuation)).lower()
    print(is_palindrome(data))


if __name__ == '__main__':
    load_data()
    # import timeit
    # print(timeit.timeit("load_data()", number=1, setup="from __main__ import load_data"))
