import sys;
input = sys.stdin.readline

money = 1000 - int(input())
count = 0

def change(unit):
    global money,count
    if money // unit:
       count += (money // unit)
       money %= unit

while (money):
    change(500)
    change(100)
    change(50)
    change(10)
    change(5)
    change(1)

print(count)