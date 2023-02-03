Test = int(input())

for T in range(Test):
    N, M = map(int,input().split())
    pari_kill = []
    pari_kill_dict = {}
    
    for n in range(1,N+1):
        pari = list(map(int,input().split()))
        pari_kill_dict.setdefault(n,pari)

    for c in range(1,n-M+2):
        for d in range(n-M+1):
            pari_cnt = 0
            for m in range(M):
                pari_cnt += sum(pari_kill_dict.get(c+m)[d:d+M])
                pari_kill.append(pari_cnt)

    pari_kill.sort()
    print(f'#{T+1} {pari_kill[-1]}')