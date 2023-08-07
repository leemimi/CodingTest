arr = []
for _ in range(8):
    arr.append(list(map(str, input())))

ans = 0
for i in range(8):
    for j in range(8):
        if i % 2 ==0 and j %2==0 :
            if arr[i][j] == 'F':
                ans+=1
        elif i%2!=0 and j%2!=0:
            if arr[i][j] == 'F':
                ans +=1
print(ans)
