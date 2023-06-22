def solution(new_id):
    new_id=new_id.lower()
    ids = ''
    for id in new_id:
        if id.isalpha() or id.isdigit() or id in "-_.":
            ids+=id

    while '..' in ids:
        ids = ids.replace('..','.')

    if ids and ids[0] == '.':
        ids = ids[1:]
    if ids and ids[-1] =='.':
        ids = ids[:-1]
    if ids == '':
        ids ='a'
    ids = ids[:15]
    if ids[-1] =='.':
        ids = ids[:-1]
    while len(ids)<3:
        ids+=ids[-1]
    return ids