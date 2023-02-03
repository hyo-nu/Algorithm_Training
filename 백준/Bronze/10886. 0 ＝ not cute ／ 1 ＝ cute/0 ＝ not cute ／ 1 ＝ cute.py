n = int(input())

yes_cute = 0
no_cute = 0

for c in range(n):
    cute = int(input())

    if cute == 1:
        yes_cute += 1
    elif cute == 0:
        no_cute += 1

if yes_cute > no_cute:
    print("Junhee is cute!")
elif yes_cute < no_cute:
    print("Junhee is not cute!")
