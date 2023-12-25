N = int(input())
series, order = 666, 1

while order != N:
    series += 1
    for i in range(len(str(series))-2):
        if list(str(series))[i:i+3].count("6") >= 3:
            order += 1
            break

print(series)