T = int(input())
for t in range(1,T+1):
    mem = list(map(int, input()))
    cnt = 0
    now = [0]*len(mem)
    for i in range(len(mem)):
        if mem[i] != now[i] :
            for j in range(i,len(mem)):
                now[j] = 1-now[j]
            cnt+=1
        if mem == now:
            break


    print(f'#{t} {cnt}')