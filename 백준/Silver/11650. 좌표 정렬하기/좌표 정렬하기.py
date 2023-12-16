import sys

def cord_sort(xy):
    x, y = xy.split()
    return int(x) + int(y) / 1000000

cordinates = sorted(sys.stdin.readlines()[1:], key = lambda x : cord_sort(x))
print("".join(cordinates))