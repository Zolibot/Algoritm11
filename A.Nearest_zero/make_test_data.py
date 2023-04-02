#!/usr/bin/python3
from random import randint
file = open("./input.txt", "wt")
count = 100
s = [randint(0, 10) for x in range(0, count)]
file.write(str(count)+"\n")
file.write(" ".join(map(str,s))+"\n")
file.close()
