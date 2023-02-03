Test = int(input())

for c in range(0, Test):
    number = int(input())
    grades = list(map(int, input().split()))
    freq = [0] * 101
    mode = 0
    for grade in grades:
        freq[grade] += 1

    for grade in range(101):
        if freq[grade] >= mode:
            mode = freq[grade]
            result = grade

    print(f"#{c + 1} {result}")