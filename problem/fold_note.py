

def solution(wallet, bill):
    answer = 0

    while max(bill) > max(wallet) or min(bill) > min(wallet):
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1

    return answer

# wallet	bill	result
# [30, 15]	[26, 17]	1
# [50, 50]	[100, 241]	4

print(solution([30, 15], [26, 17])) # 1
print(solution([50, 50], [100, 241])) # 4