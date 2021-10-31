def solution(phone_book):
    phone_book.sort()
    answer=True
    for i in range(len(phone_book)-1):
        l=len(phone_book[i])
        if phone_book[i]==phone_book[i+1][:l]:
            answer=False
    return answer
