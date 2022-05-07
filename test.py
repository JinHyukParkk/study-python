nums = list(map(int, input().split()))
sum = 0
err = False

for i in nums :
    if i < 0 or i >= 10:
        err = True
        break
    else :
        sum = sum + i

if err is False :
    print('총 합은' + str(sum) + '입니다.')
else :
    print('Error 10 미만의 양수만 입력해 주세요')



