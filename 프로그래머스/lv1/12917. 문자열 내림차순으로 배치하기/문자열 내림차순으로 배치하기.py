def solution(s):
    answer = ''
    s = list(s)
#     slist = list(map(lambda x: str(x),s))
#     slist.sort(reverse=True)
#     for i in slist:
#         if(i.islower()):
#             answer+=i
    
#     for i in slist:
#         if(i.isupper()):
#             answer+=i
    answer = ''.join(sorted(s, reverse=True))
    return answer