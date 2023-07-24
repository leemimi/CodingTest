arr=[]
for _ in range(3):
    s = input()
    arr.append(s)

ans = ''
for i in range(3):
    if arr[i] == 'black':
        ans+='0'
    elif arr[i] == 'brown':
        ans+='1'
    elif arr[i] == 'red':
        ans+='2'
    elif arr[i] == 'orange':
        ans+='3'
    elif arr[i] == 'yellow':
        ans+='4'
    elif arr[i] == 'green':
        ans+='5'
    elif arr[i] == 'blue':
        ans+='6'
    elif arr[i] == 'violet':
        ans+='7'
    elif arr[i] == 'grey':
        ans+='8'
    else:
        ans+='9'

a = int(ans[:2])
result = a*10**int(ans[-1])
print(result)