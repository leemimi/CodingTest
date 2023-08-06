import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    people = [i for i in range(1, n+1)]


    for i in range(k):
        a = []
        for j in range(n):
            a.append(sum(people[:j+1]))
        people = a.copy()
    print(people[-1])