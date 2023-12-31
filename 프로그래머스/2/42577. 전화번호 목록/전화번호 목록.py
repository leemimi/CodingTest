def solution(phone_book):
    answer = True
    phone_book.sort()
    
    for i in range(len(phone_book)-1):
        prev = phone_book[i]
        if phone_book[i+1][:len(prev)] == prev:
            answer = False
            break
        
                
        
    
    return answer