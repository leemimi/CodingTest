from itertools import product
def solution(users, emoticons):
             
    answer = []
    data = [10, 20, 30, 40]
    max_sub, max_sales = 0, 0
    for discount in product([10,20,30,40],repeat=len(emoticons)):
        curr_sub, curr_sales = 0,0
        for rate, total in users:
            res = 0
            for r,emo in zip(discount, emoticons):
                if r >= rate:
                    res += int(emo - emo*(r/100))
            if res >= total:
                curr_sub +=1
            else:
                curr_sales += res
        if curr_sub > max_sub:
            max_sub, max_sales = curr_sub, curr_sales
        elif curr_sub == max_sub and curr_sales > max_sales:
            max_sales = curr_sales

            
    return max_sub, max_sales