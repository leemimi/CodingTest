ww = input()
key = input()

cnt = 0
k = len(key)
i = 0
while i < len(ww):
    if ww[i:i+k] == key:
        cnt+=1
        i += k
    else:
        i+=1
print(cnt)