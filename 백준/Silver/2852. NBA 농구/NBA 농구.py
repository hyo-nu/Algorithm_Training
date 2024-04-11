import sys;
input = sys.stdin.readline

N = int(input())
info = [input().split() for _ in range(N) ]

Ascore = Bscore = 0
Atime = Btime = 0
for n in range(N):
    h, m = map(int,info[n][1].split(":"))
    if Ascore > Bscore :
        Atime += ( (h - int(info[n-1][1].split(":")[0])) * 60 ) + (m - int(info[n-1][1].split(":")[1]) )
    elif Ascore < Bscore :
        Btime += ( (h - int(info[n-1][1].split(":")[0])) * 60 ) + (m - int(info[n-1][1].split(":")[1]) )

    if info[n][0] == "1": Ascore += 1
    else : Bscore += 1


if Ascore > Bscore :
    Atime += ( (48 - h) * 60 ) + (0 - m)
elif Ascore < Bscore :
    Btime += ( (48 - h) * 60 ) + (0 - m)


print(f'{str(Atime // 60).zfill(2)}:{str(Atime % 60).zfill(2)}')
print(f'{str(Btime // 60).zfill(2)}:{str(Btime % 60).zfill(2)}')
