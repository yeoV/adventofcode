import sys
import re

command = sys.stdin.read()

def extract_instructions(command):
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"    # 어차피 순서대로 매칭됨
    return re.finditer(pattern, command)

def extract_and_multifly(mul):
    n1, n2 = map(int, re.findall(r"\d+", mul))
    return n1 * n2

result = 0
enabled = True

for match in extract_instructions(command):
    inst = match.group()

    if inst == "do()":
        enabled = True
    elif inst == "don't()":
        enabled = False
    elif enabled and inst.startswith("mul"):
        result += extract_and_multifly(inst)
print(result)