
def solution(mats, park):
    answer = -1

    # sort 방법
    mats.sort(reverse=True)

    for mat in mats:
        for y in range(len(park)):
            for x in range(len(park[y])):
                if check_mat(x, y, mat, park):
                    answer = max(answer, mat)
                    break

    return answer

def check_mat(x, y, mat, park):
    for i in range(mat):
        for j in range(mat):
            if x+i >= len(park[y]) or y+j >= len(park):
                return False
            if park[y+j][x+i] != "-1":
                return False

    return True


print(solution([5,3,2],[["A", "A", "-1", "B", "B", "B", "B", "-1"], ["A", "A", "-1", "B", "B", "B", "B", "-1"], ["-1", "-1", "-1", "-1", "-1", "-1", "-1", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"], ["D", "D", "-1", "-1", "-1", "-1", "-1", "F"], ["D", "D", "-1", "-1", "-1", "-1", "E", "-1"]])) #3

