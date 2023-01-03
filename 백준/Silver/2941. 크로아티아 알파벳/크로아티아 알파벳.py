word = input()

cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in cro:
    if i in word:
        word = word.replace(i,"#")

print(len(word))