def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)

def lcm(x,y):
    return (x*y)//gcd(x,y)

a,b = map(int, input().split())
print(gcd(a,b))
print(lcm(a,b))