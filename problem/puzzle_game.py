
def cal_solving_time(diff, time_cur, time_prev, level):
    if diff <= level:
        return time_cur
    else:
        fail_count = diff - level
        return fail_count * (time_cur + time_prev) + time_cur

def possible_level(level, diffs, times, limit):
    solving_time = 0

    for index, diff in enumerate(diffs):
        time_cur = times[index]

        if index == 0:
            solving_time += time_cur
            continue

        time_prev = times[index - 1]
        solving_time += cal_solving_time(diff, time_cur, time_prev, level)

    return solving_time <= limit

def solution(diffs, times, limit):
    answer = 0
    start, level, end = min(diffs), 0, max(diffs)

    while start <= end:
        level = (start + end) // 2

        if possible_level(level, diffs, times, limit):
            answer = level
            end = level - 1
        else:
            start = level + 1

    return answer


print(solution([1, 5, 3], [2,4,7], 30)) # 3
print(solution([1, 4, 4, 2], [6, 3, 8, 2], 59))  # 2
print(solution([1, 328, 467, 209, 54], [2, 7, 1, 4, 3], 1723)) # 294
print(solution([1, 99999, 100000, 99995], [9999, 9001, 9999, 9001], 3456789012)) # 39354


# 첫 시도는 Linear 하게 했으나 시간 초과가 났다.
# 이분 탐색으로 풀어야 하는 문제는 이분 탐색을 적용해야 한다.

