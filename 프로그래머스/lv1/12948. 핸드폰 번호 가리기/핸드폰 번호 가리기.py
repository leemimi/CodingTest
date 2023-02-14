def solution(phone_number):
    answer = ''
    phone_number = str(phone_number)
    print(phone_number)
    for i in range(len(phone_number)-3):
        answer = "*" * i + phone_number[-4:]

    return answer