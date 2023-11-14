import sys
input = sys.stdin.readline
left = list(input().rstrip())
right = []
m = int(input())
for _ in range(m):
    ps = input().split()

    if ps[0] == 'L' and left:
        right.append(left.pop())
    elif ps[0] == 'D' and right:
        left.append(right.pop())
    elif ps[0] == 'B' and left:
        left.pop()
    elif ps[0] == 'P':
        left.append(ps[1])

ans = left + right[::-1]
print(''.join(ans))