import sys


def hello():
    print("Hello World")
    sys.setrecursionlimit(10)
    hello()


hello()