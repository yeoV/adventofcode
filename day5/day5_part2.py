import sys
from collections import defaultdict
from functools import cmp_to_key
from typing import List

read = sys.stdin.read

sections = read().split("\n\n")
rules = [tuple(map(int, x.split("|"))) for x in sections[0].split("\n")]
updates = [list(map(int, x.split(","))) for x in sections[1].split("\n")]


def build_graph(rules):
    graph = defaultdict(list)
    for x, y in rules:
        graph[x].append(y)
    return graph


def check_valid(update, rule_graph):
    # 맨 마지막 val 제외
    for idx, base in enumerate(update[:-1]):
        for nxt_val in update[idx + 1 :]:
            if nxt_val not in rule_graph[base]:
                return False
    return True


def sort_update(invalid_update, rule_graph):
    def compare(x, y):
        if y in rule_graph[x]:
            return -1
        elif x in rule_graph[y]:
            return 1
        return 0

    return sorted(invalid_update, key=cmp_to_key(compare))


def sum_mid(updates: List):
    return sum(updates[len(updates // 2)])


# main
rule_graph = build_graph(rules)
invalid_updates = [x for x in updates if not check_valid(x, rule_graph)]
sorted_updates = list(map(lambda x: sort_update(x, rule_graph), invalid_updates))
result = sum(map(lambda x: x[len(x) // 2], sorted_updates))
print(result)
