
def check_op(op_start_time, op_end_time, cur_time):
    if op_start_time <= cur_time <= op_end_time:
        return True

    return False

def solution(video_len, pos, op_start, op_end, commands):
    video_min, video_sec = video_len.split(':')
    op_start_min, op_start_sec = op_start.split(':')
    op_end_min, op_end_sec = op_end.split(':')
    cur_min, cur_sec = pos.split(':')

    video_len_time = int(video_min) * 60 + int(video_sec)
    op_start_time = int(op_start_min) * 60 + int(op_start_sec)
    op_end_time = int(op_end_min) * 60 + int(op_end_sec)
    cur_time = int(cur_min) * 60 + int(cur_sec)

    if check_op(op_start_time, op_end_time, cur_time):
        cur_time = op_end_time

    for command in commands:
        if command == 'prev':
            cur_time = max(0, cur_time - 10)
        else:
            cur_time = min(video_len_time, cur_time + 10)

        if check_op(op_start_time, op_end_time, cur_time):
            cur_time = op_end_time

    return '{:02d}:{:02d}'.format(cur_time // 60, cur_time % 60)


# video_len	pos	op_start	op_end	commands	result
# "34:33"	"13:00"	"00:55"	"02:55"	["next", "prev"]	"13:00"
# "10:55"	"00:05"	"00:15"	"06:55"	["prev", "next", "next"]	"06:55"
# "07:22"	"04:05"	"00:15"	"04:07"	["next"]	"04:17"

print(solution("34:33", "13:00", "00:55", "02:55", ["next", "prev"])) # "13:00"
print(solution("10:55", "00:05", "00:15", "06:55", ["prev", "next", "next"])) # "06:55"
print(solution("07:22", "04:05", "00:15", "04:07", ["next"])) # "04:17"