import re
def solution(word, pages):
    answer = []
    word=word.lower()
    basic = {}
    ex = {}
    linkScore ={}
    for page in pages:
        url = re.search('<meta property="og:url" content="(https://\S+)"',page).group(1)
        basic[url] = 0
        ex[url] = 0
        for find in re.findall('[a-zA-Z]+',page):
            if find.lower() == word:
                basic[url] +=1
        for link in re.findall('<a href="(https://\S+)"',page):
            ex[url]+=1
            if link in linkScore:
                linkScore[link].append(url)
            else:
                linkScore[link] = [url]
    for b in basic:
        cnt = 0
        if b in linkScore:
            for l in linkScore[b]:
                cnt += basic[l]/ex[l]
        answer.append(basic[b]+cnt)
    return answer.index(max(answer))