import math
h,w,n,m = map(int, input().split())


a = math.ceil(h/(n+1))
b = math.ceil(w/(m+1))

print(a*b)
