t1 = ['a', 'i', 'e', 'o', 'u']
while True:
    word = input()
    if word == 'end':
        break


    ans = 0
    cnt = 0

    for i in word:
        if i in t1:
            cnt+=1

    if cnt < 1:
        print(f'<{word}> is not acceptable.')
        continue
    for i in range(len(word)-2):
        if word[i] in t1 and word[i+1] in t1 and word[i+2] in t1:
            ans = 1
        elif word[i] not in t1 and word[i+1] not in t1 and word[i+2] not in t1:
            ans = 1

    if ans == 1:
        print(f'<{word}> is not acceptable.')
        continue

    for i in range(len(word)-1):
        if word[i] == word[i+1]:
            if word[i] == 'o' or word[i] == 'e':
                continue
            else:
                ans = 1

    if ans == 1:
        print(f'<{word}> is not acceptable.')
        continue
    print(f'<{word}> is acceptable.')










