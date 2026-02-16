A = list(map(int, input().split()))
B = list(map(int, input().split()))
flag = "PLAYER A"
while True:
    if A[1] <= 0 or B[1] <= 0:
        if(A[1] <= 0 and B[1] > 0 ) :
            flag = "PLAYER B"
        elif(A[1] <= 0 and B[1] <= 0):
            flag = "DRAW"
        break
    B[1] -= A[0]
    A[1] -= B[0]

print(flag)