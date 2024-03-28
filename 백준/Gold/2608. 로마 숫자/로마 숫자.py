r1 = input()
r2 = input()

roma = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
roma2 = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

roman_map = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]
def convert(ss):
    res = 0
    i =0
    while i<len(ss):

        if i+1 < len(ss):
            if ss[i:i+2] in roma2:
                res += roma2[ss[i:i+2]]
                i+=2
                continue
        if ss[i] in roma:
            res += roma[ss[i]]
            i+=1
    return res
def convert2(num):
    tmp = ""
    while num > 0:
        for k,v in roman_map:
            while num >= k:
                tmp += v
                num -= k
    return tmp


result = convert(r1) + convert(r2)
res2 = convert2(result)
print(result)
print(res2)