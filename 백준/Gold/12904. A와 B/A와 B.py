s = input()
t = input()


while True:
    possible = False

    if t[-1] == 'A':
        t = t[:-1]

    elif t[-1] == 'B':
        t = t[:-1]
        t = t[::-1]

    if t == s:
        possible = True
        break

    if len(s) > len(t):
        break


if possible == True:
    print(1)
else:
    print(0)