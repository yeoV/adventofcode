# https://adventofcode.com/2024/day/2
import sys


reports = [list(map(int, line.strip().split())) for line in sys.stdin]


def check_safe(report):
    diff = report[0] - report[1]
    is_increase = diff < 0  # init 방향 세팅
    for prev, nxt in zip(report, report[1:]):  # zip 으로 묶이지 않은 건 잘림
        diff = prev - nxt
        if not 0 < abs(diff) <= 3:
            return False
        if is_increase != (diff < 0):
            return False
    return True


result = 0
for report in reports:
    if check_safe(report):
        result += 1
        continue
    for idx in range(len(report)):
        sub_report = report[:idx] + report[idx + 1 :]
        if check_safe(sub_report):
            result += 1
            break
print(result)
