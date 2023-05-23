def solution(phone_book):
    answer = True
    
    hashDict = {}
    
    for b in phone_book:
        hashDict[b] = 1
    
    for b in phone_book:
        temp = ""
        for num in b:
            temp +=num
            if temp in hashDict and temp !=b:
                answer = False
    return answer