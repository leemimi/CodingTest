import sys
input = sys.stdin.readline
import heapq

n = int(input())
lst = input()

arr = lst.split()
dict = {}
for i in range(n):
    if arr[i][-6:] == 'Cheese':
        if arr[i] not in dict:
            dict[arr[i]] = 1
        else:
            dict[arr[i]] +=1

if len(dict) >= 4:
    print('yummy')
else:
    print('sad')