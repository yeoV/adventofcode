import sys
import re
from typing import List
from collections import deque
command = sys.stdin.read()


def mut_filter(command) -> List[str]:
    pattern = r"mul\(\d+,\d+\)"
    mut_text = re.finditer(pattern, command)
    return [(x.start(), x.group()) for x in mut_text]

def do_filter(command):
    pattern = r"(do\(\))"
    do_text = re.finditer(pattern, command)
    return [(x.start(), "do") for x in do_text]

def dont_filter(command):
    pattern = r"(don't\(\))"
    dont_text = re.finditer(pattern, command)
    return [(x.start(), "don't") for x in dont_text]

def extract_and_multifly(mul):
    numbers = re.match(r"mul\((\d+),(\d+)\)", mul)
    n1, n2 = map(int, numbers.groups())
    return n1 * n2

context = mut_filter(command) + do_filter(command) + dont_filter(command)
context = sorted(context, key=lambda x: x[0])
enabled = True # do, dont 
q = deque(context)
result = 0
while q:
    _, val = q.popleft()
    if val == "do":
        enabled = True
    elif val == "don't":
        enabled = False
    elif enabled:
        result += extract_and_multifly(val)
        
    
print(result)