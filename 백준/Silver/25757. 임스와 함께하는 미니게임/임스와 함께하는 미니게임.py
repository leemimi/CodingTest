n, game = map(str, input().split())
people = set()
for _ in range(int(n)):
    p = input()
    people.add(p)

people = list(people)

if game == 'Y':
    print(len(people))
elif game == 'F':
    print(len(people)//2)
else:
    print(len(people)//3)