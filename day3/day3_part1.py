import sys
import re
from typing import List

command = sys.stdin.read()


def mut_filter(command) -> List[str]:
    pattern = r"mul\(\d+,\d+\)"
    return re.findall(pattern, command)


def extract_and_multifly(mul):
    numbers = re.match(r"mul\((\d+),(\d+)\)", mul)
    n1, n2 = map(int, numbers.groups())
    return n1 * n2


mul_list = mut_filter(command)
print(sum(map(extract_and_multifly, mul_list)))
