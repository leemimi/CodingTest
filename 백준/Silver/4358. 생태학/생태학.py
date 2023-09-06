import sys
input = sys.stdin.readline

tree = {}
cnt = 0
while True:
    s = input().rstrip()
    if s == '':
        break
    if s not in tree:
        tree[s] =1
    else:
        tree[s] +=1
    cnt+=1
tree_list = list(tree.keys())
tree_list.sort()

for t in tree_list:
    print('%s %.4f' %(t, (tree[t]/cnt)*100))