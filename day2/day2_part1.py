# https://adventofcode.com/2024/day/2
import sys

reports = [list(map(int, report.strip().split())) for report in sys.stdin]


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


result = sum(map(lambda x: check_safe(x), reports))
print(result)
