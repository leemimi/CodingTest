num = input()
mins = float('inf')
maxs = 0


def sums(new):
    tmp = 0
    for w in new:
        tmp += int(w)

    return tmp


def cnt_odd(num):
    return sum(1 for digit in str(num) if int(digit)%2!=0)

def dfs(n,odd):
    global mins, maxs
    odd += cnt_odd(n)

    if len(str(n)) ==1:
        mins = min(mins, odd)
        maxs = max(maxs, odd)
        return

    if len(str(n)) == 2:
        new_n = int(str(n)[0])+int(str(n)[1])
        dfs(new_n, odd)
        return

    str_n= str(n)
    for i in range(1,len(str_n)):
        for j in range(i+1,len(str_n)):
            first = int(str_n[:i])
            second = int(str_n[i:j])
            third = int(str_n[j:])
            dfs(first+second+third, odd)

dfs(num, 0)

print(mins, maxs)