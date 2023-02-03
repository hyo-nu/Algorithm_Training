Test = int(input())


for T in range(Test):
    money = int(input())
    money_lst = []
    coin = 0
    if money >= 50000:
        coin += (money//50000)
        money = money % 50000
    money_lst.append(coin)
    coin = 0
    if money >= 10000:
        coin += (money//10000)
        money = money % 10000
    money_lst.append(coin)
    coin = 0
    if money >= 5000:
        coin += (money//5000)
        money = money % 5000
    money_lst.append(coin)
    coin = 0
    if money >= 1000:
        coin += (money//1000)
        money = money % 1000
    money_lst.append(coin)
    coin = 0
    if money >= 500:
        coin += (money//500)
        money = money % 500
    money_lst.append(coin)
    coin = 0
    if money >= 100:
        coin += (money//100)
        money = money % 100
    money_lst.append(coin)
    coin = 0
    if money >= 50:
        coin += (money//50)
        money = money % 50
    money_lst.append(coin)
    coin = 0
    if money >= 10:
        coin += (money//10)
        money = money % 10
    money_lst.append(coin)
    coin = 0

    print(f'#{T+1}')
    for i in money_lst:
        print(i,end = ' ')
    print()
