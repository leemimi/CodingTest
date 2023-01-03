word = list(input())

Number = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

sum = 0
for i in word:
    for j in Number:
        if i in j:
            sum += Number.index(j)+3

print(sum)