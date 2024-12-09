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
    return all(
        y in rule_graph[x]
        for idx, x in enumerate(update[:-1])
        for y in update[idx + 1 :]
    )


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
sorted_updates = [sort_update(x, rule_graph) for x in invalid_updates]
result = sum([x[len(x) // 2] for x in sorted_updates])
print(result)

# Claude 방식
# 가장 연결된 노드가 많은 값부터 순서대로 연결 -> 그렇게 하면 가장 선행되어야 하는 값이 맨 앞으로 올 수 있음
# def sort_update_(invalid_update, rule_graph):
#     # 람다 함수로 대체 가능
#     return sorted(
#         invalid_update,
#         key=lambda x: (-sum(y in rule_graph.get(x, set()) for y in invalid_update), x),
#     )
