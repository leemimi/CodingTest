import sys, re
n = int(input())

arr = []
for _ in range(n):
    s = input().rstrip()
    arr.append(s)

ans = []
stack =[]

def s_split(strs):
    i = 0
    a = []
    while i < len(strs):
        new = ''
        if strs[i].isdigit():
            while i<len(strs) and strs[i].isdigit():
                new+=strs[i]
                i+=1
        else:
            while i<len(strs) and strs[i].isalpha():
                new+=strs[i]
                i+=1
        a.append(new)
    return a

def make_key(s):
    tokens = s_split(s)
    key = []

    for token in tokens:
        if token.isdigit():
            key.append((0, int(token),len(token)))
        else:
            letter = []
            for ch in token:
                letter.append((ord(ch.upper())-ord('A'), 0 if ch.isupper() else 1))
            key.append((1, letter))
    return key

arr.sort(key=make_key)
for s in arr:
    print(''.join(s))
    



        
