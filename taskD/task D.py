from typing import List


def load_data() -> None:
    file = open("input.txt", "rt")
    data = file.read()
    data = [int(a) if a.isdigit() else list(map(int, a.split())) for a in data.split("\n")]
    chaotic_weather(data)


def chaotic_weather(weather: List) -> None:
    count = 0
    if weather[0] == 1:
        count += 1
    else:
        f = weather[1]
        for i, temp in enumerate(f):
            if (i+1) < weather[0]:
                next_temp = f[i + 1]
                past_temp = f[i - 1]
                if i == 0:
                    if temp > next_temp:
                        count += 1
                else:
                    if temp > next_temp and temp > past_temp:
                        count += 1
            if i == weather[0] - 1:
                past_temp = f[i - 1]
                if temp > past_temp:
                    count += 1
    print(count)


if __name__ == "__main__":
    load_data()
