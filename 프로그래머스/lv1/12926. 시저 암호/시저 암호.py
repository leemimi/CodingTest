def solution(s, n):
    answer = ''
    
    bigarr = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    smallarr = "abcdefghijklmnopqrstuvwxyz"
    
    arr = []
    
    for i in s:
        if i in bigarr:
            idx = bigarr.index(i)
            arr.append(bigarr[(idx+n)%26])
        elif i in smallarr:
            idx = smallarr.index(i)
            arr.append(smallarr[(idx+n)%26])
        if i == " ":
            arr.append(" ")

    return "".join(arr)