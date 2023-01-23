from collections import deque

n = int(input())

card = deque(range(1,n+1))

while True:
    if len(card) == 1:
        print(card[0])
        break

    card.popleft()
    cur = card.popleft()
    card.append(cur)