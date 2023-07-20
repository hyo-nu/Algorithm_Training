N = list(map(int,list(input())))
print("LUCKY") if sum(N[:len(N)//2]) == sum(N[len(N)//2:]) else print("READY")

