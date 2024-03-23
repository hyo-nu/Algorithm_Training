number = sorted(list(input()),reverse=True)
print("".join(number) if int("".join(number)) % 30 == 0 else -1)