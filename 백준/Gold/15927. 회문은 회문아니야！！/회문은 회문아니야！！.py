str = input()
if len(str) <=1 or len(str) == str.count(str[0]):
    print(-1)
else:
    s = list(str)
    if s != s[::-1]:
        print(len(str))
    else:
        print(len(s)-1)