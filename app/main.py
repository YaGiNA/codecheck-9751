#!/usr/bin/env python3
import requests
import sys

url = 'http://challenge-server.code-check.io/api/recursive/ask'
cache = {}


def askServer(n, seed):
    if n not in cache:
        query = {"seed": seed, "n": n}
        r = requests.get(url, params=query).json()
        cache[n] = r["result"]
    return cache[n]


def call(n, seed):
    if n == 0:
        return 1
    elif n == 2:
        return n
    elif n % 2 == 0:
        nlist = [call(i, seed) for i in range(n-1, n-5, -1)]
        return sum(nlist)
    else:
        return askServer(n, seed)


def main(argv):
    try:
        seed = argv[0]
        print(call(int(argv[1]), seed))
    except IndexError:
        print("Values is not inputed correctly.")
        sys.exit(1)
