def calc(ans):
    tmp = ans.replace(" ", "")
    if eval(tmp) == 0:
        print(ans)

def oper(now,ans):
    global answer
    if now == n+1:
        calc(ans)
        return
    oper(now+1, ans+' '+str(now))
    oper(now+1, ans+'+'+str(now))
    oper(now+1, ans+'-'+str(now))

t = int(input())
for _ in range(t):
    n = int(input())
    answer = []
    oper(2,'1')
    print()