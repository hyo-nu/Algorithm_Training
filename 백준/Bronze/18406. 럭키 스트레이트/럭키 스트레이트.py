score = list(map(int,list(input())))
half = len(score)//2
left, right = score[:half], score[half:]
print("LUCKY") if sum(left) == sum(right) else print("READY")