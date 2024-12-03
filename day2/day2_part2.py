# https://adventofcode.com/2024/day/2
import sys


reports = [list(map(int, line.strip().split())) for line in sys.stdin]


def check_safe(report):
    diff = report[0] - report[1]
    is_increase = diff < 0  # init 방향 세팅
    for prev, nxt in zip(
        report, report[1:], strict=False
    ):  # zip 으로 묶이지 않은 건 잘림
        diff = prev - nxt
        if not 0 < abs(diff) <= 3 or is_increase != (diff < 0):
            return False
    return True


# 메모리 최적화
def create_subset(report):
    for idx in range(len(report)):
        yield report[:idx] + report[idx + 1 :]


def check_safe_report(report):
    if check_safe(report):
        return True
    return any(map(check_safe, create_subset(report)))


result = len(list(filter(check_safe_report, reports)))
print(result)


# 이전에 작성한 코드
# result = 0
# for report in reports:
#     if check_safe(report):
#         result += 1
#         continue
#     for idx in range(len(report)):
#         sub_report = report[:idx] + report[idx + 1 :]
#         if check_safe(sub_report):
#             result += 1
#             break
