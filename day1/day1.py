"""
생각의 흐름
- Heapq로 할까 했는데 데이터 적어서 굳이..?
- 정렬된 상태라면 l < r 경우에는 무시해도 되는거 아닌가? -> 일단 구현 2)
- 그럼 맨 마지막 값은 어차피 풀스캔하고, 정렬된거면 이분탐색 써도 되는거 아닌가? 2_1)

time 비교)
answer2 time : 0.004448890686035156
answer2_1 time : 0.0002181529998779297

"""
import sys
import time # 시간 측정
from bisect import bisect_left, bisect_right

left_list,right_list = [], []
# ReadLines 
for line in sys.stdin:
    if line.strip():    # avoid blank
        left, right = tuple(map(int, line.split()))
        left_list.append(left)
        right_list.append(right)

left_list.sort()
right_list.sort()

def calc_distance():
    result = 0
    for l, r in zip(left_list, right_list):
        result += abs(l-r)
    return result

def calc_similarity():
    s_time = time.time()
    result = 0
    for l in left_list:
        cnt = 0
        for r in right_list:
            if l < r:
                break
            if l == r:
                cnt += 1
        
        result += l * cnt
    return result, time.time() - s_time

# Using bisect
def calc_similarity_bisect():
    s_time = time.time()
    result = 0
    for l in left_list:
        left_idx = bisect_left(right_list, l)
        right_idx = bisect_right(right_list, l)
        cnt = right_idx - left_idx
        result += l * cnt
    return result, time.time() - s_time


answer1 = calc_distance()
answer2, time2 = calc_similarity()
answer2_1, time2_1 = calc_similarity_bisect()
print(answer1, answer2, answer2_1)
print(f"answer2 time : {time2}")
print(f"answer2_1 time : {time2_1}")