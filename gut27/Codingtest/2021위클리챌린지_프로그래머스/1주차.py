def solution(price, money, count):
    answer = 0
    if count % 2 == 1:
        answer = money - (((price + price*(count-1)) * (count//2)) + (price*count))
    else:
        answer = money - (price + (price*count)) * (count//2)
    return abs(min(0,answer))
