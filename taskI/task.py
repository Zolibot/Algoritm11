def check_pow(d: int) -> bool:
    if d == 1:
        return True
    while d % 10 in [6, 4] or d > 1:
        d /= 4
    if d == 1:
        return True
    return False


# assert check_pow(16) == True
# assert check_pow(32) == False
# assert check_pow(1) == True
# assert check_pow(1) == True
# assert check_pow(1) == True
# assert check_pow(64) == True
# assert check_pow(256) == True
# assert check_pow(1) == True


def load_data() -> None:
    digit = int(input())
    print(check_pow(digit))


if __name__ == "__main__":
    load_data()
    #
    # import timeit
    #
    # msg = timeit.timeit("load_data()", number=1, setup="from __main__ import load_data")
    # print(msg)
